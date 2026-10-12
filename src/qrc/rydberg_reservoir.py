"""
Quantum Reservoir Computing (QRC) via Rydberg Neutral Atom Simulators (Bloqade).
Encodes sequential time-series inputs into detuning waveforms and extracts
high-order Rydberg density observables for linear readout.
"""

from typing import List, Tuple, Optional
import numpy as np
from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_squared_error, mean_absolute_error


def generate_synthetic_time_series(
    n_points: int = 90,
    random_state: int = 7
) -> Tuple[np.ndarray, np.ndarray]:
    """
    Generate synthetic non-linear multi-frequency time series with Gaussian noise.
    s(t) = 0.65 * sin(2*pi*t / 18) + 0.25 * sin(2*pi*t / 7) + noise
    """
    rng = np.random.RandomState(random_state)
    t = np.arange(n_points)
    signal = (
        0.65 * np.sin(2 * np.pi * t / 18.0)
        + 0.25 * np.sin(2 * np.pi * t / 7.0)
        + 0.03 * rng.normal(size=n_points)
    )
    return t, signal


class RydbergReservoir:
    """
    Analog Quantum Reservoir on Neutral Atom Array.
    Uses Bloqade Analog simulation to evolve a chain of Rydberg atoms under
    constant Rabi driving and input-modulated detuning.
    """

    def __init__(
        self,
        n_atoms: int = 5,
        spacing: float = 6.0,
        segment_duration: float = 0.20,
        rabi_amplitude: float = 2.5,
        detuning_scale: float = 2.0,
        shots: int = 120,
    ):
        self.n_atoms = n_atoms
        self.spacing = spacing
        self.segment_duration = segment_duration
        self.rabi_amplitude = rabi_amplitude
        self.detuning_scale = detuning_scale
        self.shots = shots
        self.positions = [(i * spacing, 0.0) for i in range(n_atoms)]
        self.readout_model = make_pipeline(StandardScaler(), Ridge(alpha=1.0))

    def build_program(self, input_window: np.ndarray):
        """
        Compile input window into a Bloqade analog pulse schedule.
        """
        from bloqade.analog import start

        detunings = (self.detuning_scale * np.asarray(input_window, dtype=float)).tolist()
        durations = [self.segment_duration] * len(detunings)

        program = start.add_position(self.positions)
        program = (
            program
            .rydberg.rabi.amplitude.uniform
            .constant(duration=sum(durations), value=self.rabi_amplitude)
            .detuning.uniform
            .piecewise_constant(durations=durations, values=detunings)
        )
        return program

    def extract_features(self, input_window: np.ndarray) -> np.ndarray:
        """
        Simulate analog Hamiltonian dynamics and extract 1-body and 2-body Rydberg observables.
        Returns:
            np.ndarray: Concatenation of [single_atom_means, pair_correlations].
                        Dimension = N_ATOMS + (N_ATOMS * (N_ATOMS - 1)) / 2
        """
        program = self.build_program(input_window)
        result = program.bloqade.python().run(self.shots)
        report = result.report()

        # In Bloqade analog convention: 0 is Rydberg (|r>), 1 is ground (|g>)
        measured_bits = np.asarray(report.bitstrings()[0], dtype=float)
        rydberg_occupations = 1.0 - measured_bits

        single_atom_means = rydberg_occupations.mean(axis=0)

        pair_features = []
        for i in range(self.n_atoms):
            for j in range(i + 1, self.n_atoms):
                pair_features.append(
                    np.mean(rydberg_occupations[:, i] * rydberg_occupations[:, j])
                )

        return np.concatenate([single_atom_means, np.asarray(pair_features)])

    def transform_windows(self, windows: np.ndarray, verbose: bool = False) -> np.ndarray:
        """Process multiple input windows through the quantum reservoir."""
        feature_rows = []
        total = len(windows)
        for idx, w in enumerate(windows):
            feature_rows.append(self.extract_features(w))
            if verbose and ((idx + 1) % 10 == 0 or idx + 1 == total):
                print(f"Processed {idx + 1}/{total} reservoir windows")
        return np.vstack(feature_rows)

    def fit_readout(self, X_reservoir: np.ndarray, y_train: np.ndarray):
        """Train classical Ridge regression layer on top of extracted quantum features."""
        self.readout_model.fit(X_reservoir, y_train)
        return self

    def predict(self, X_reservoir: np.ndarray) -> np.ndarray:
        """Predict target values from reservoir features."""
        return self.readout_model.predict(X_reservoir)

    def evaluate(self, y_true: np.ndarray, y_pred: np.ndarray) -> dict:
        """Compute regression metrics (RMSE, MAE)."""
        rmse = float(np.sqrt(mean_squared_error(y_true, y_pred)))
        mae = float(mean_absolute_error(y_true, y_pred))
        return {"rmse": rmse, "mae": mae}
