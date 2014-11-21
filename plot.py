import sys
import csv_data
import matplotlib.pylab as plt

def classification_distribution(data, img_file_name):
    x_axis = [record[0][0] for record in data]
    y_axis = [record[0][1] for record in data]
    color  = [record[1]    for record in data]

    plt.scatter(x_axis, y_axis, s=100,  c=color)

    plt.xlim((0, 1))
    plt.ylim((0, 1))

    plt.title('Records classification distribution')
    plt.xlabel('Six-fold rotational symmetry')
    plt.ylabel('Eccentricity')

    plt.savefig(img_file_name)

classification_distribution(csv_data.load_file(sys.argv[1]), sys.argv[2])
