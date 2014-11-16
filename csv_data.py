import csv

def load(file):
    return [[[float(row[0]), float(row[1])], int(row[2])] for row in csv.reader(file)]

def load_file(filename):
    return load(open(filename, 'r'))
