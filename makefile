generate_split:
	@echo "Making renamed version"
	@python3 -c "from src.data.load_data import create_renamed_data; create_renamed_data()"
	@echo "Splitting data"
	@python3 -c "from src.features.prepare_dataset import generate_split; from src import config; generate_split(config.data_path_renamed)"

generate_report_raw:
	@echo "Generating Profile Report of the raw data"
	@python3 -c "from src.visualization.visualization_eda import make_report_eda_raw; make_report_eda_raw()"

compare_models:
	@echo "Comparing models"
	@python3 -c "from src.models.train import compare_models; compare_models()"

tune_random_forest:
	@echo "Tuning Random Forest"
	@python3 -c "from src.models.test import tune_model; tune_model('RandomForest')"

test_random_forest:
	@echo "Testing Random Forest"
	@python3 -c "from src.models.test import test_model; test_model('RandomForest')"

compare_tune_test_random_forest:
	$(MAKE) compare_models
	$(MAKE) tune_random_forest
	$(MAKE) test_random_forest
