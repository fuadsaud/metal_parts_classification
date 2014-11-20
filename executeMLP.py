from __future__ import division

import mlp
import pickle
import sys
import csv_data
import metal_parts

def class_for_output_vector(output):
    return output.index(max(output)) + 1

mlp = pickle.load(open(sys.argv[1], 'rb'))

test_data = csv_data.load_file(sys.argv[2])

errors = 0
profit = 0

confusion_matrix = {
        metal_parts.BOLT:  [],
        metal_parts.NUT:   [],
        metal_parts.RING:  [],
        metal_parts.SCRAP: [],
}

for record in test_data:
    actual_class = record[1]

    output = mlp.run(record[0])

    print record, output

    assigned_class = class_for_output_vector(output)

    if assigned_class != actual_class: errors += 1

    profit += metal_parts.PROFIT[assigned_class][actual_class]

    confusion_matrix[assigned_class].append(actual_class)

recognition_rate = (len(test_data) - errors) / len(test_data) * 100

print 'CLASSIFICATION ERRORS: %d' % errors
print 'RECOGNITION RATE: %.2f%%' % recognition_rate
print 'PROFIT: %.3f' % profit
print 'CONFUSION_MATRIX: ', confusion_matrix
