from pathlib import Path

from pyprojroot.here import (
    here,
)  # This package is useful to track the root directory of the package

# Useful locations of files

root_folder = here()

# Data folders
data_id = "varshitanalluri/crop-recommendation-dataset"
data_name = "Crop_Recommendation.csv"
data_dir = root_folder / "data"
data_dir_raw = data_dir / "raw"
data_dir_interim = data_dir / "interim"
data_path_raw = data_dir_raw / "Crop_Recommendation.csv"
data_path_renamed = data_dir_interim / "crop_recommendation_renamed.csv"
data_path_train = data_dir_interim / "crop_recommendation_train.csv"
data_path_val = data_dir_interim / "crop_recommendation_val.csv"

# Output folders
report_dir = root_folder / "reports"
eda_profile_raw = report_dir / "profile_eda_raw.html"
path_hyperparameters = root_folder / "models/hyperparameters"

random_state = 314159  # Random state for reproducibility
target = "crop"  # Target column
features = [
    "nitrogen",
    "phosphorus",
    "potassium",
    "temperature",
    "humidity",
    "ph_value",
    "rainfall",
]
features_std = [f + "_std" for f in features]
features_minmax = [f + "_minmax" for f in features]
# We store the possible labels in the target. This accounts for our limited knowledge of what crops should be.
labels = [
    "Rice",
    "Maize",
    "ChickPea",
    "KidneyBeans",
    "PigeonPeas",
    "MothBeans",
    "MungBean",
    "Blackgram",
    "Lentil",
    "Pomegranate",
    "Banana",
    "Mango",
    "Grapes",
    "Watermelon",
    "Muskmelon",
    "Apple",
    "Orange",
    "Papaya",
    "Coconut",
    "Cotton",
    "Jute",
    "Coffee",
]
labels_map = {label: i for i, label in enumerate(labels)}
