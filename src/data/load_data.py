from pathlib import Path

import kaggle
import pandas as pd

from src import config


def check_existing_data():
    """Verifies whether the raw data is present in the data folder, otherwise downloads it"""
    if not config.data_path_raw.is_file():
        print("Raw dataset missing! Downloading from Kaggle...")
        download_raw_data()


def download_raw_data():
    """Downloads the `Crop Recommendation` dataset from Kaggle"""
    kaggle.api.authenticate()
    print(f"Downloading dataset to {config.data_dir_raw}")
    kaggle.api.dataset_download_file(
        dataset=config.data_id,
        file_name=config.data_name,
        force=True,
        path=config.data_dir_raw,
    )


def create_renamed_data():
    """Given the raw dataset, exports a copy with columns normalized (lower case, underscores instead of spaces)"""
    data_raw = pd.read_csv(config.data_path_raw)
    data_raw.columns = data_raw.columns.str.lower()
    data_raw.columns = data_raw.columns.str.replace(" ", "_")
    print(f"Exporting dataset after basic cleaning to {config.data_path_renamed}")
    data_raw.to_csv(config.data_path_renamed, index=False)
