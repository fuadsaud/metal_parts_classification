from __future__ import division

import sys
import mlp
import pickle
import csv_data
import metal_parts
import matplotlib.pylab as plt

BREAKPOINTS = [0, 10, 100, 1000, 10000]

CLASSES = {
    metal_parts.BOLT:  [1, 0, 0, 0],
    metal_parts.NUT:   [0, 1, 0, 0],
    metal_parts.RING:  [0, 0, 1, 0],
    metal_parts.SCRAP: [0, 0, 0, 1],
}

def output_vector_for_class(klass):
    return CLASSES[klass]

training_data = csv_data.load_file(sys.argv[1])

net = mlp.MLP(2, 5, 4)

sses = []

for epoch in range(BREAKPOINTS[-1] + 1):
    if epoch in BREAKPOINTS:
        pickle.dump(net, open('nets/net_%d' % epoch, 'wb'))

    sse = sum([
        net.train(record[0], output_vector_for_class(record[1]))
        for record
        in training_data])

    sses.append(sse)

plt.plot(range(len(sses)), sses, 'ro')
plt.xlim((0, len(sses)))
plt.ylim((0, max(sses)))

plt.title('SSE over Epochs')
plt.xlabel('Epochs')
plt.ylabel('SSE')

plt.savefig('mlp_sse.png')
