import ensemble
import sys
import csv_data

training_data = csv_data.load_file(sys.argv[1])

ensemble.derive_tree(training_data)
