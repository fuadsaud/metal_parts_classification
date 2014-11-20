default: mlp
mlp: train_mlp execute_mlp
dt: train_dt execute_dt
train_mlp:
	python trainMLP.py train_data.csv
execute_mlp:
	python executeMLP.py nets/net_10000 test_data.csv
train_dt:
	python trainDT.py train_data.csv
execute_dt:
