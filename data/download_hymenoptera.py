#!/usr/bin/env python3
"""
Utility script to verify or download the Hymenoptera dataset (Ants & Bees).
Used for Quantum Transfer Learning experiments.
"""

import os
import sys
import zipfile
import urllib.request
from pathlib import Path

DATA_URL = "https://download.pytorch.org/tutorial/hymenoptera_data.zip"
TARGET_DIR = Path(__file__).resolve().parent / "hymenoptera_data"


def verify_dataset(data_dir: Path) -> bool:
    """Check if train and val splits contain ants and bees images."""
    if not data_dir.exists():
        return False
    
    splits = ["train", "val"]
    classes = ["ants", "bees"]
    total_images = 0
    
    for split in splits:
        for cls in classes:
            folder = data_dir / split / cls
            if not folder.is_dir():
                return False
            count = len(list(folder.glob("*.jpg")) + list(folder.glob("*.jpeg")) + list(folder.glob("*.png")))
            if count == 0:
                return False
            total_images += count
            
    print(f"[OK] Hymenoptera dataset verified at {data_dir} ({total_images} total images).")
    return True


def download_and_extract(target_dir: Path):
    """Download and extract hymenoptera_data if not already present."""
    if verify_dataset(target_dir):
        return

    parent_dir = target_dir.parent
    zip_path = parent_dir / "hymenoptera_data.zip"

    print(f"Downloading dataset from {DATA_URL}...")
    urllib.request.urlretrieve(DATA_URL, zip_path)

    print("Extracting dataset...")
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(parent_dir)

    if zip_path.exists():
        zip_path.unlink()

    if verify_dataset(target_dir):
        print("Dataset ready for Quantum Transfer Learning.")
    else:
        print("[Error] Failed to verify downloaded dataset.", file=sys.stderr)


if __name__ == "__main__":
    download_and_extract(TARGET_DIR)
