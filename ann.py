import math
import random

def SIGMOID(x):
    return 1 / (1 + math.exp(x * -1))

def IDENTITY(x):
    return x

class Neuron:
    def __init__(self, n_inputs, activation_function):
        self.n_inputs = n_inputs
        self.activation_function = activation_function
        self.weights = [random.uniform(-1, 1) for n in range(n_inputs + 1)]

    def activate(self, inputs):
        return self.activation_function(self._sum(inputs))

    def _sum(self, inputs):
        return sum([input * weight for input, weight in zip(inputs, self.weights)])

class Layer:
    def __init__(self, neurons):
        self.neurons = neurons

    def activate(self, inputs):
        return [neuron.activate(inputs) for neuron in self.neurons]

class Network:
    def __init__(self, activation_function):
        self.output_layer = Layer([Neuron(5, activation_function) for i in range(0, 4)])
        self.hidden_layer = Layer([Neuron(2, activation_function) for i in range(0, 5)])
        self.input_layer  = Layer([Neuron(1, IDENTITY) for i in range(0, 2)])

    def train(self, x, y):
        i_result = self.input_layer.activate(x)
        h_result = self.hidden_layer.activate(i_result)
        o_result = self.output_layer.activate(h_result)

        output_deltas = self._output_layer_deltas(o_result, y)

        print output_deltas

    def run(self, x):
        return self.output_layer.activate(
                self.hidden_layer.activate(
                    self.input_layer.activate(x)))

    def _output_layer_deltas(self, results, expected_results):
       return [(result - expected_result) * result * (1 - result)
                for neuron, result, expected_result
                in zip(self.output_layer.neurons, results, expected_results)]

    def _hidden_layer_deltas(self, output_deltas):
        hidden_deltas = []
        for neuron in self.hidden_layer.neurons:
            error = 0.0

            for output_delta in output_deltas:
                error += output_delta * weight

            hidden_deltas.append(dsigmoid(neuron.activate())
