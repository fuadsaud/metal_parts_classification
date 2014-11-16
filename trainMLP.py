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

data = csv_data.load_file(sys.argv[1])

mlp = mlp.MLP(2, 3, 4)

for i in range(10001):
    # if i in BREAKPOINTS:
    #     pickle.dump(mlp, open('nets/net_%d' % i, 'wb'))

    for j, record in enumerate(data):
        mlp.train(record[0], output_vector_for_class(record[1]))
