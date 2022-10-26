import sys
import io
#from apps.learn2 import SingleInputNeuron1
#from apps.learn3 import MultipleInputNeuron1

def main(argv):
    if (len(argv) == 2 and argv[0] == '--app' and argv[1] == 'learn2.SingleInputNeuron1'):
        from apps.learn2 import SingleInputNeuron1
    elif (len(argv) == 2 and argv[0] == '--app' and argv[1] == 'learn3.MultipleInputNeuron1'):
        from apps.learn3 import MultipleInputNeuron1
    else:
        raise Exception("Invalid Argument")

main(sys.argv[1:])