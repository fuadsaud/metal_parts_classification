from __future__  import division
# from scipy.stats import entropy
from itertools   import groupby
from math        import log

import collections
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
        return collections.Counter(classifications(training_samples)).most_common(1)
    else:
        best = best_attribute(training_samples)

def all_same_class(samples):
    return len(set(classifications(samples))) == 1

def no_attributes(samples):
    return not samples[0][0]

def classifications(samples):
    return [sample[1] for sample in samples]

def attributes(samples):
    return [sample[0] for sample in samples]

def best_attribute(samples):
    total_entropy = entropy(classifications(samples))

    print total_entropy

def entropy(samples):
    return sum([
        -probability * log(probability, 2)
        for probability
        in [
            len(s) / len(samples)
            for s
            in groupby(np.sort(samples))]])
