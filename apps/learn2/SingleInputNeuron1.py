#The scalar input p is multiplied by the scalar weight w to form wp, one of the terms that is sent to the 
#summer. The other input, 1, is multiplied by a bias b and then passed to 
#the summer. The summer output n, often referred to as the net input, goes 
#into a transfer function f, which produces the scalar neuron output a. 
#(Some authors use the term “activation function” rather than transfer function and “offset” rather than bias.)

# p : scalar input
# w : scalar weight
# a : activation function or offset
# b : bias
# n : summer output or net input
# f : transfer function
# a = f(wp + b)
# Summer has 2 inputs, namely w*p and 1*b
# The summer output n, ofetn referred to as the net input, goes into a transfer function f, which producess the scalar neuron outpu a.
# Thus (p*w) + (1*b) = net input
# Let p  = 2
# Let w = 3
# Let b = -1.5
# Therefor
# a = f(p*w + 1*b)
# a = f(2*3 + 1*-1.5)
# a = f(6 -1.5)
# a = f(4.5)

#The actual output depends on the particular transfer function that is chosen
#bias is like a weight expect it has a constant input 1... bias can be ommited

#Three most popluar transfer functions:
# 1) Hard limit transfer function
# 2) Liniar tranfer function
# 3) Log Sigmoid tranfer function

# Scalar small italic letters
# Vectors small non italic bold letters
# Matrices capital Bold nonitalic letters

# Scalar 4
# Vector: 4,1
# Matrix: 1, 4, 3
#         2, 2, 4
#         9, 2, 4

# Imports
import sys
import os
import math

base_dir = os.path.dirname(__file__) or '.'
print (base_dir)
# Import lib trade functionality
neuralNetDir = os.path.join(base_dir, '..\\..\\lib\\NeuralNet')
sys.path.insert(1, neuralNetDir)
from TransferFunction import *

#from 
##from lib import TransferFunctionType
#from lib.NeuralNet.TransferFunction import TransferFunction

class SingleInputNeuron:
    # Class variable
    p = 0.0
    w = 0.0
    b = 0.0
    netInput = 0.0
    hardLimitTransferFunctionResult = 0
    linearTransferFunctionResult = 0.0
    logSigmoidTransferFunctionResult = 0.0
    neuronOutput = 0.0
    tf = None
    tfType = TransferFunctionType.NOT_SELECTED

    #def  p(self, p: int):
    #    self.p = p
    def __init__(self, tf : TransferFunction, tfType : TransferFunctionType) -> None:
        self.tf = tf
        self.tfType = tfType
        pass

    def calculateNetInput(self, input, weight, bias) ->  float:
        self.p = input
        self.w = weight
        self.b = bias
        self.netInput = (self.w * self.p) + (self.b * 1)
        return self.netInput

    def printNetInputFormula():
        print("(w*p) + (b*1)")

    def getNeuronOuput(self, netInput) -> float:
        if (self.tfType == TransferFunctionType.HARD_LIMIT):
            self.neuronOutput = self.tf.hardLimit(netInput)
        elif (self.tfType == TransferFunctionType.LINEAR):
            self.neuronOutput = self.tf.linear(netInput)
        elif (self.tfType == TransferFunctionType.LOG_SIGMOID):
            self.neuronOutput = self.tf.logSigmoid(netInput)
        else:
            raise Exception("TransferFunction Type not defined")

        return self.neuronOutput

def CalculateOutputWithHardLimitTransferFunction1():
    tf = TransferFunction()
    tfType = TransferFunctionType.HARD_LIMIT
    sin = SingleInputNeuron(tf, tfType)
    shouldIGoSurf = 0
    # input1... the current wave size
    waveSize = 1.0
    # The bias here lets the transfer function know about my preference in size of wave
    bias = -100.0
    for input in range(110):
        optimalSize = 100.0
        weight = input/optimalSize
        netInput = sin.calculateNetInput(input, weight , bias)
        neuronOutput = sin.getNeuronOuput(netInput)
        print("neuronOutput: CalculateOutputWithHardLimitTransferFunction1: {:.2f}".format(neuronOutput))

def CalculateOutputWithHardLimitTransferFunction2():
    tf = TransferFunction()
    tfType = TransferFunctionType.HARD_LIMIT
    sin = SingleInputNeuron(tf, tfType)
    shouldIGoSurf = 0
    # input1... the current wave size
    waveSize = 1.0
    # input2... the weight... what weight does input1 have
    # input1's weight or importance is determined by the size of the wave vs what size is a wave that is optimal
    optimalSize = 3.0
    weight = waveSize/optimalSize
    # The bias here lets the transfer function know about my preference in size of wave
    bias = -3.0
    netInput = sin.calculateNetInput(waveSize, weight , bias)
    neuronOutput = sin.getNeuronOuput(netInput)
    print("neuronOutput: {:.2f}".format(neuronOutput))

def CalculateOutputWithHardLimitTransferFunction3():
    tf = TransferFunction()
    tfType = TransferFunctionType.HARD_LIMIT
    sin = SingleInputNeuron(tf, tfType)
    # input1... the current wave size
    shouldIGiveTheComputerToAnita = 5.0
    # input2... the weight... what weight does input1 have
    # input1's weight or importance is determined by the size of the wave vs what size is a wave that is optimal
    theBestTimeToGiveComputerToAnita = 5.0
    weight = shouldIGiveTheComputerToAnita/theBestTimeToGiveComputerToAnita
    # The bias here lets the transfer function know about my preference in size of wave
    bias = -5.0
    netInput = sin.calculateNetInput(shouldIGiveTheComputerToAnita, weight , bias)
    neuronOutput = sin.getNeuronOuput(netInput)
    print("neuronOutput: {:.2f}".format(neuronOutput))

def CalculateOutputWithLinearTransferFunction1():
    tf = TransferFunction()
    tfType = TransferFunctionType.LINEAR
    sin = SingleInputNeuron(tf, tfType)
    shouldIGoSurf = 0
    # input1... the current wave size
    waveSize = 4.0
    # input2... the weight... what weight does input1 have
    # input1's weight or importance is determined by the size of the wave vs what size is a wave that is optimal
    optimalSize = 3.0
    weight = waveSize/optimalSize
    # The bias here lets the transfer function know about my preference in size of wave
    bias = -3.0
    netInput = sin.calculateNetInput(waveSize, weight , bias)
    neuronOutput = sin.getNeuronOuput(netInput)
    print("neuronOutput: {:.2f}".format(neuronOutput))

def CalculateOutputWithLogSigmoidTransferFunction1():
    tf = TransferFunction()
    tfType = TransferFunctionType.LOG_SIGMOID
    sin = SingleInputNeuron(tf, tfType)
    shouldIGoSurf = 0
    # input1... the current wave size
    waveSize = 3.0
    # input2... the weight... what weight does input1 have
    # input1's weight or importance is determined by the size of the wave vs what size is a wave that is optimal
    optimalSize = 3.0
    weight = waveSize/optimalSize
    # The bias here lets the transfer function know about my preference in size of wave
    bias = -3.0
    netInput = sin.calculateNetInput(waveSize, weight , bias)
    neuronOutput = sin.getNeuronOuput(netInput)
    print("neuronOutput: {:.2f}".format(neuronOutput))

def CalculateOutputWithLogSigmoidTransferFunction2():
    tf = TransferFunction()
    tfType = TransferFunctionType.LOG_SIGMOID
    sin = SingleInputNeuron(tf, tfType)
    waveSize = 1.0
    # The bias here lets the transfer function know about my preference in size of wave
    bias = -100.0
    for waveSize in range(105):
        optimalSize = 100.0
        weight = waveSize/optimalSize
        netInput = sin.calculateNetInput(waveSize, weight , bias)
        neuronOutput = sin.getNeuronOuput(netInput)
        print("neuronOutput: {:.2f}".format(neuronOutput))

CalculateOutputWithHardLimitTransferFunction1()
CalculateOutputWithHardLimitTransferFunction2()
CalculateOutputWithHardLimitTransferFunction3()
CalculateOutputWithLinearTransferFunction1()
CalculateOutputWithLogSigmoidTransferFunction1()
CalculateOutputWithLogSigmoidTransferFunction2()