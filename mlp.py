from __future__ import division

import math
import numpy as np

LEARNING_RATE = 0.1

class MLP:
    def __init__(self, n_in, n_hid, n_out):
        self.n_in  = n_in
        self.n_hid = n_hid
        self.n_out = n_out

        self.in_values  = [1.0] * self.n_in
        self.hid_values = [1.0] * self.n_hid
        self.out_values = [1.0] * self.n_out

        self.w_in  = np.random.rand(self.n_in,  self.n_hid)
        self.w_out = np.random.rand(self.n_hid, self.n_out)

    def train(self, inputs, target):
        self.run(inputs)

        return self.__update_weights(target)

    def run(self, inputs):
        if len(inputs) != self.n_in: raise ValueError('wrong number of inputs')

        self.in_values = inputs

        self.hid_values = [
                self.__sigmoid(
                    sum([
                        self.in_values[j] * self.w_in[j][i]
                        for j
                        in range(self.n_in)]))
                    for i
                    in range(self.n_hid)]


        self.out_values = [
                self.__sigmoid(
                    sum([
                        self.hid_values[j] * self.w_out[j][i]
                        for j
                        in range(self.n_hid)]))
                    for i
                    in range(self.n_out)]


        return self.out_values[:]

    def __update_weights(self, targets, learning_rate=LEARNING_RATE):
        if len(targets) != self.n_out: raise ValueError('wrong number of targets')

        output_deltas = [
                self.__dsigmoid(out_value) * out_value * (target - out_value)
                for target, out_value
                in zip(targets, self.out_values)]

        hidden_deltas = [
            self.__dsigmoid(self.hid_values[i]) * self.hid_values[i] * sum(
                [output_deltas[j] * self.w_out[i][j]
                 for j
                 in range(self.n_out)])
            for i
            in range(self.n_hid)]

        for i in range(self.n_hid):
            for j in range(self.n_out):
                self.w_out[i][j] += learning_rate * output_deltas[j] * self.hid_values[i]

        for i in range(self.n_in):
            for j in range(self.n_hid):
                self.w_in[i][j] += learning_rate * hidden_deltas[j] * self.in_values[i]

        return sum([
            (target - out_value) ** 2
            for target, out_value
            in zip(targets, self.out_values)])

    def __sigmoid(self, x):
        return 1 / (1 + math.exp(x * -1))

    def __dsigmoid(self, x):
        return 1 - x
