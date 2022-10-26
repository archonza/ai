# Convention we use is as follows:
# s_ : Scalar
# v_ : Vector
# m_ : Matrix
# w : weight
# p : input
# b : bias
# n : NetInput
# a : NeuronOutput
# f : TransferFunction

# n = m_w * v_p + s_b
# a = f(m_w * v_p + b)
#from lib.NeuralNet.TransferFunction import TransferFunction
import sys
import os
from array import array
from sqlite3 import Row
from lib.NeuralNet.TransferFunction import TransferFunction
from lib.NeuralNet.TransferFunction import TransferFunctionType

class MultipleInputNeuron:
    # Class variable
    v_p = None
    w_row = 0   # number of rows for a single neuron is 1
    w_col = 0
    m_w = None
    b = 0.0
    netInput = 0.0
    hardLimitTransferFunctionResult = 0
    linearTransferFunctionResult = 0.0
    logSigmoidTransferFunctionResult = 0.0
    neuronOutput = 0.0

    # tf     : The desired Transfer Function object
    # tfType : The desired Transfer Function Type
    # ivector : A vector (array) of inputs, where number of inputs are user defined
    # wmatrix : A matrix of weights where row's are determined by number of neurons
    def __init__(self) -> None:
         #self.v_p = [0.0]*len(inputs)
        #self.m_w = [[0.0]*1]*len(inputs)
        pass

    # [In]   v_p : A vector (array) of inputs, where number of inputs are user defined
    # [In]   m_w : A matrix of weights where row's are determined by number of neurons
    # [In]     b : The desired bias
    # [Return] v_n : Net input
    def calculateNetInput(self, v_p, m_w, b) :
        n = 0.0
        for idx in range(len(v_p)):
            for row in (range(len(m_w))):
                for col in (range(len(m_w[row]))):
                    n = v_p[idx] * m_w[row][col] + b
        n = n + b
        return n

    def calculateNeuronOutput(self, n, tf : TransferFunction, tfType : TransferFunctionType):
        a = tf.calculateNeuronOutput(n, tfType)
        return a

    def calculateOptimalBias(self, v_p, m_w, tf, tfType: TransferFunctionType) -> float:
        for b in range(0, -1000000, -1):
            n = multiInputNeuron.calculateNetInput(v_p, m_w, b)
            a = multiInputNeuron.calculateNeuronOutput(n, tf, tfType)
            if (a == 0.0):
                b = b + 1
                return float(b)

multiInputNeuron = MultipleInputNeuron()
#inputs = [1]
#weights = [1][1]
idx = 2
inputs = [0] * idx
col = 2
row = 1
weights = [ [0] * col ] * row
inputs[0] = 3.0
#optimalWaveSize = 3.0
inputs[1] = 30.0
#optimalWindSpeed = 30.0
weights[0][0] = 3.0
weights[0][1] = 30.0
transferFunction = TransferFunction()
transferFunctionType = TransferFunctionType.HARD_LIMIT
#bias = multiInputNeuron.calculateOptimalBias(inputs, weights, transferFunction, transferFunctionType)
#print(bias)
bias = -450.0
netInput = multiInputNeuron.calculateNetInput(inputs, weights, bias)
neuronOutput = multiInputNeuron.calculateNeuronOutput(netInput, transferFunction, transferFunctionType)
print("neuronOutput: {:.2f}".format(neuronOutput))
