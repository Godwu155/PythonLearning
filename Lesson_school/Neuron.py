import numpy


def relu(x):
    return max(0, x)


class Neuron:
    def __init__(self, weight, bias):
        self.weight = weight
        self.bias = bias

    def forward(self, inputs):
        weighted_sum = 0
        for i in range(len(self.weight)):
            weighted_sum += inputs[i] * self.weight[i]

        total = weighted_sum + self.bias
        output = relu(total)

        return output


weights = [0.5, 0.3, 0.2]
bias = 0.1
inputs = [0.2,0.4,0.6]

neuron = Neuron(weights, bias)
output = neuron.forward(inputs)
print("Output:%.2f" % output)
