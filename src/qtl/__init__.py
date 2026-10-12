"""Quantum Transfer Learning (QTL) module using PyTorch and PennyLane."""

from .dressed_quantum_net import DressedQuantumNet, create_hybrid_resnet

__all__ = ["DressedQuantumNet", "create_hybrid_resnet"]
