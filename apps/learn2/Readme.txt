


# Read inputs
#
# -> Input1
# -> Input2
# -> Input3
# -> Input4

# Apply weigth to each input (help determine the importance of each input)

# Inputs are thn multiplied by their respective weigths and then summed.

# Afterwards the output is passed though an activation function, which determines the output.

# If that output exceeds a given threshold, it "fires" (or activates) the node, 
# passing data to the next layer in the network.
# The results in the output of one node becoming in the input of the next node.
# The process of passing data from one layer to the next layer defined this neural network
# as a feedforward network.

# Lets go surfing
# Input 1
# Are the waves good? (Yes: 1, No: 0)
# Is the line-up empty? (Yes:1, No: 0)
# Has there been a recent shark attack? (Yes: 0, No: 1)

# X1 = 1
# X2 = 0
# X3 = 1

# Now, we need to assign some weights to determine importance.
# Larger weigths signify that particular variables are of greater importance to the
# decision or outcome

# W1 = 5
# W2 = 2
# W3 = 4

# We assume a threshold value of 3, which would translate to a bias value of -3.

# Y-hat - (1*5) + (0*2) + (1*4) - 3

# Think of each individual node as its own linear regression model, 
# composed of input data, weights, a bias (or threshold), and an 
# output. The formula would look something like this:
# ∑wixi + bias = w1x1 + w2x2 + w3x3 + bias
# output = f(x) = 1 if ∑w1x1 + b>= 0; 0 if ∑w1x1 + b < 0

# i represents the index of the sample,
# y-hat is the predicted outcome,
# y is the actual value, and
# m is the number of samples.
# 𝐶𝑜𝑠𝑡 𝐹𝑢𝑛𝑐𝑡𝑖𝑜𝑛= 𝑀𝑆𝐸=1/2𝑚 ∑129_(𝑖=1)^𝑚▒(𝑦 ̂^((𝑖) )−𝑦^((𝑖) ) )^2

# Ultimately, the goal is to minimize our cost function to ensure correctness of fit for any given observation. As the model adjusts its weights and bias, it uses the cost function and reinforcement learning to reach the point of convergence, or the local minimum. The process in which the algorithm adjusts its weights is through gradient descent, allowing the model to determine the direction to take to reduce errors (or minimize the cost function). With each training example, the parameters of the model adjust to gradually converge at the minimum.  
# Most deep neural networks are feedforward, meaning they flow in one direction only, from input to output. However, you can also train your model through backpropagation; that is, move in the opposite direction from output to input. Backpropagation allows us to calculate and attribute the error associated with each neuron, allowing us to adjust and fit the parameters of the model(s) appropriately.

# Bias in Neural Networks can be thought of as analogous to the role of a constant in a linear function, whereby the line is effectively transposed by the constant value. In a scenario with no bias, the input to the activation function is 'x' multiplied by the connection weight 'w0'.
#  think that biases are almost always helpful. In effect, a bias value allows you to shift the activation function to the left or right, which may be critical for successful learning.
# The main function of a bias is to provide every node with a trainable constant value (in addition to the normal inputs that the node recieves). You can achieve that with a single bias node with connections to N nodes, or with N bias nodes each with a single connection; the result should be the same.
# A simpler way to understand what the bias is: it is somehow similar to the constant b of a linear function
# y = ax + b
# It allows you to move the line up and down to fit the prediction with the data better.
# Without b, the line always goes through the origin (0, 0) and you may get a poorer fit.