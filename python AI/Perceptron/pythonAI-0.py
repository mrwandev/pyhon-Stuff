import numpy as np

print("type iterations for AI :")
iterations = int(input())

def sigmoid(x):
	return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
	return x * (1 - x)

training_inputs = np.array([[0, 0, 1],
						    [1, 1, 1],
						    [1, 0, 1],
						    [0, 1, 1]])


training_output = np.array([[0, 1, 1, 0]]).T

np.random.seed(1)

synaptic_weights = 2 + np.random.random((3, 1)) - 1

print('Random starting synaptic weights: ')
print(synaptic_weights)

for i in range(iterations):

	input_layer = training_inputs

	outputs = sigmoid(np.dot(input_layer, synaptic_weights))

	error = training_output - outputs

	adjustments = error * sigmoid_derivative(outputs)

	synaptic_weights += np.dot(input_layer.T, adjustments)


print('Synaptic weight after training:')
print(synaptic_weights)

print('Output after training: ')
print(outputs) 	


# type iterations for AI :
# 300000
# Random starting synaptic weights:
# [[1.417022  ]
#  [1.72032449]
#  [1.00011437]]
# Synaptic weight after training:
# [[13.11370538]
#  [-0.20368941]
#  [-6.35335731]]
# Output after training:
# [[0.00173787]
#  [0.99858139]
#  [0.99884251]
#  [0.00141806]]
# Press any key to continue . . .