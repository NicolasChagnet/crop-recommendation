from pathlib import Path

import kaggle
import pandas as pd

from src import config


def create_renamed_data():
    """Given the raw dataset, exports a copy with columns normalized (lower case, underscores instead of spaces)"""
    data_raw = pd.read_csv(config.data_path_raw)
    data_raw.columns = data_raw.columns.str.lower()
    data_raw.columns = data_raw.columns.str.replace(" ", "_")
    print(f"Exporting dataset after basic cleaning to {config.data_path_renamed}")
    data_raw.to_csv(config.data_path_renamed, index=False)
