from __future__ import division

import sys
import csv_data
import pickle
import mlp
import metal_parts
import matplotlib.pylab as plt

def classification_regions(network, title, img_file_name, interval=100):
    coords = [
        (i / interval, j / interval)
        for j
        in range(0, interval + 1, 1)
        for i
        in range(0, interval + 1, 1)]

    classified_records = []

    for coord in coords:
        output = network.run(coord)

        classified_records.append(
            [coord, output.index(max(output)) + 1])

    plt.scatter(
        [record[0][0] for record in classified_records],
        [record[0][1] for record in classified_records],
        c=[record[1]    for record in classified_records],
    )

    plt.xlim((0, 1))
    plt.ylim((0, 1))

    plt.title(title)
    plt.xlabel('Six-fold rotational symmetry')
    plt.ylabel('Eccentricity')

    plt.savefig(img_file_name)

classification_regions(
    pickle.load(open(sys.argv[1], 'rb')),
    sys.argv[2],
    sys.argv[3],
)
