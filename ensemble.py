from __future__  import division
from itertools   import groupby
from math        import log
from collections import Counter

import scipy.stats
import numpy as np

class Forest:
    def __init__(n_trees, n_training_records):
        self.n_trees = n_trees
        self.n_training_records = n_training_records

def derive_tree(training_samples):
    if not training_samples:
        pass
    elif all_same_class(training_samples):
        return training_samples[0][1]
    elif no_attributes(training_samples):
        return Counter(classifications(training_samples)).most_common(1)
    else:
        best = best_attribute(training_samples)

def all_same_class(samples):
    return len(set(classifications(samples))) == 1

def no_attributes(samples):
    return not samples[0][0]

def classifications(samples):
    return [sample[1] for sample in samples]

def attributes(samples):
    return np.transpose([sample[0] for sample in samples])

def best_attribute(samples, threshold=0.5):
    classif = classifications(samples)
    total_entropy = entropy(classifications(samples))

    attrs = attributes(samples)

    for attr in attrs:
        splits = split_attr(zip(attr, classif), 0.5)
        for split in splits:
            print list(split)

        # print groupby(np.sort(s, axis=1), lambda x: x[-1])

        # for key, value in groupby(zip(attr, classif), lambda pair: pair[-1]):
        #     print key, len([pair[0] for pair in list(value)])

    print total_entropy

def entropy(samples):
    return scipy.stats.entropy(probabilities(samples))

def probabilities(samples):
    return [
        len(list(samples_subset)) / len(samples)
        for klass, samples_subset
        in groupby(np.sort(samples))]

def split_attr(classified_attrs, threshold):
    return [group[1]
            for group in
            groupby(np.sort(classified_attrs, axis=0), lambda pair: pair[0] < threshold)]

def pp(arg):
    print arg

    return arg
