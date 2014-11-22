TRAINING_DATA_FILE = train_data.csv
TEST_DATA_FILE     = test_data.csv

TRAINING_DATA_DISTRIBUTION_IMG_FILE = imgs/training_data_distribution.png
TEST_DATA_DISTRIBUTION_IMG_FILE     = imgs/test_data_distribution.png

CLASSIFICATION_REGIONS_IMG_FILE_PREFIX = imgs/net_classification_region_

NET_FILE_PREFIX = nets/net_

default: dt

mlp: train_mlp execute_mlp

dt: train_dt execute_dt

train_mlp:
	python trainMLP.py $(TRAINING_DATA_FILE)

execute_mlp:
	python executeMLP.py $(NET_FILE_PREFIX)$(EPOCHS) $(DATA_FILE)

train_dt:
	python trainDT.py $(TRAINING_DATA_FILE)

execute_dt:

plot_training_data:
	python plot_classification_distribution.py $(TRAINING_DATA_FILE) 'Training Data Distribution' $(TRAINING_DATA_DISTRIBUTION_IMG_FILE)
	open $(TRAINING_DATA_DISTRIBUTION_IMG_FILE)

plot_test_data:
	python plot_classification_distribution.py $(TEST_DATA_FILE) 'Test Data Distribution' $(TEST_DATA_DISTRIBUTION_IMG_FILE)
	open $(TEST_DATA_DISTRIBUTION_IMG_FILE)

plot_classification_regions:
	python plot_classification_regions.py $(NET_FILE_PREFIX)$(EPOCHS) "$(EPOCHS) epochs MLP" $(CLASSIFICATION_REGIONS_IMG_FILE_PREFIX)$(EPOCHS).png
