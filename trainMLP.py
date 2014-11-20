from __future__ import division

import sys
import mlp
import pickle
import csv_data
import metal_parts

BREAKPOINTS = [0, 10, 100, 1000, 10000]

CLASSES = {
    metal_parts.BOLT:  [1, 0, 0, 0],
    metal_parts.NUT:   [0, 1, 0, 0],
    metal_parts.RING:  [0, 0, 1, 0],
    metal_parts.SCRAP: [0, 0, 0, 1],
}

def output_vector_for_class(klass):
    return CLASSES[klass]

def class_for_output_vector(output):
    return output.index(max(output)) + 1

def new_mlp():
    return mlp.MLP(2, 5, 4)

training_data = csv_data.load_file(sys.argv[1])
test_data     = csv_data.load_file('test_data.csv')

mlps = [new_mlp() for _ in range(len(BREAKPOINTS))]

for breakpoint, mlp in zip(BREAKPOINTS, mlps):
    for _ in range(breakpoint):
        for record in training_data:
            mlp.train(record[0], output_vector_for_class(record[1]))

    pickle.dump(mlp, open('nets/net_%d' % breakpoint, 'wb'))
