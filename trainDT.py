import sys
import csv_data

training_data = csv_data.load_file(sys.argv[1])

print training_data
