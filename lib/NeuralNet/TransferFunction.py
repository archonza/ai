from array import array
import math
from enum import Enum

class TransferFunctionType(Enum):
    NOT_SELECTED = -1
    HARD_LIMIT = 0
    LINEAR = 1
    LOG_SIGMOID = 2

class TransferFunction:
    def __init__(self) -> None:
        pass

    def calculateNeuronOutput(self, n, tfType : TransferFunctionType):
        a = 0.0
        if (tfType == TransferFunctionType.HARD_LIMIT):
            a = self.hardLimit(n)
        elif (tfType == TransferFunctionType.LINEAR):
            a = self.linear(n)
        elif (tfType == TransferFunctionType.LOG_SIGMOID):
            a = self.logSigmoid(n)
        else:
            raise Exception("TransferFunction Type not defined")
        return a

    # Seems like its good for yes/no, true/false, answers with < 0 being no or false and > 0 being yes or true
    def hardLimit(self, netInput) -> int:
        if (netInput < 0.0):
            result = 0
        else:
            result = 1
        return result

    # Seems like its good for no its to small, no its to big, yes, its perfect answers, with 0.0 being the perfect answer
    def linear(self, netInput) -> float:
        result = netInput
        return result

    # Seems like its good for providing a estimatation and multiple inputs... need some more investigation
    def logSigmoid(self, netInput) -> float:
        result = 1 / 1 + math.pow(math.e, -(netInput))
        return result