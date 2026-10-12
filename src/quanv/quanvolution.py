"""
Quanvolutional (Quantum Convolutional) Filter and Hybrid Classifier.
Applies parameterized random quantum circuits over 2x2 spatial image patches
to construct rich non-linear quantum feature maps.
"""

from typing import Optional, List, Tuple
import os
import numpy as np


class QuanvolutionFilter:
    """
    Quantum Convolutional filter using PennyLane.
    Maps 2x2 spatial receptive fields to 4 qubits via angle embedding,
    applies random entangling unitary layers, and measures Pauli-Z expectation values.
    """

    def __init__(self, n_layers: int = 1, seed: int = 0, device_name: str = "default.qubit"):
        import pennylane as qml
        from pennylane.templates import RandomLayers

        self.n_layers = n_layers
        self.dev = qml.device(device_name, wires=4)
        rng = np.random.RandomState(seed)
        self.rand_params = rng.uniform(high=2 * np.pi, size=(n_layers, 4))

        @qml.qnode(self.dev)
        def _circuit(phi):
            for j in range(4):
                qml.RY(np.pi * phi[j], wires=j)
            RandomLayers(self.rand_params, wires=list(range(4)))
            return [qml.expval(qml.PauliZ(j)) for j in range(4)]

        self.circuit = _circuit

    def transform_image(self, image: np.ndarray, stride: int = 2) -> np.ndarray:
        """
        Convolve a 2D single-channel image with the quantum circuit.
        Input shape: (H, W, 1) or (H, W)
        Output shape: (H // stride, W // stride, 4)
        """
        if image.ndim == 3:
            img = image[:, :, 0]
        else:
            img = image

        h, w = img.shape
        out_h, out_w = h // stride, w // stride
        out = np.zeros((out_h, out_w, 4), dtype=np.float32)

        for j in range(0, h - (stride - 1), stride):
            for k in range(0, w - (stride - 1), stride):
                patch = [
                    float(img[j, k]),
                    float(img[j, k + 1]),
                    float(img[j + 1, k]),
                    float(img[j + 1, k + 1]),
                ]
                q_res = self.circuit(patch)
                for c in range(4):
                    out[j // stride, k // stride, c] = float(q_res[c])

        return out

    def transform_batch(
        self,
        images: np.ndarray,
        cache_path: Optional[str] = None,
        verbose: bool = True
    ) -> np.ndarray:
        """
        Transform a batch of images. If cache_path exists, load from disk.
        """
        if cache_path and os.path.exists(cache_path):
            if verbose:
                print(f"Loading cached quanvolved data from: {cache_path}")
            return np.load(cache_path)

        transformed = []
        n_samples = len(images)
        for idx, img in enumerate(images):
            if verbose:
                print(f"Quanvolving image {idx + 1}/{n_samples}...", end="\r", flush=True)
            transformed.append(self.transform_image(img))

        if verbose:
            print(f"\nCompleted quanvolution for {n_samples} images.")

        result = np.asarray(transformed, dtype=np.float32)
        if cache_path:
            np.save(cache_path, result)
            if verbose:
                print(f"Saved preprocessed features to: {cache_path}")

        return result


def build_keras_classifier(num_classes: int = 2, learning_rate: float = 0.001):
    """
    Construct downstream Keras classifier on top of flattened feature maps.
    """
    import tensorflow as tf
    from tensorflow import keras

    model = keras.models.Sequential([
        keras.layers.Flatten(),
        keras.layers.Dense(num_classes, activation="softmax")
    ])

    optimizer = keras.optimizers.Adam(learning_rate=learning_rate)
    model.compile(
        optimizer=optimizer,
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"],
    )
    return model
