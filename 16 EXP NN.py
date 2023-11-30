import numpy as np
import matplotlib.pyplot as plt
import networkx as nx

class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        self.weights_input_hidden = np.random.rand(input_size, hidden_size)
        self.bias_hidden = np.zeros((1, hidden_size))
        self.weights_hidden_output = np.random.rand(hidden_size, output_size)
        self.bias_output = np.zeros((1, output_size))

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        return x * (1 - x)

    def forward(self, inputs):
        # Forward pass through the network
        self.hidden_activation = self.sigmoid(np.dot(inputs, self.weights_input_hidden) + self.bias_hidden)
        self.output = self.sigmoid(np.dot(self.hidden_activation, self.weights_hidden_output) + self.bias_output)
        return self.output

    def train(self, inputs, targets, learning_rate, epochs):
        for epoch in range(epochs):
            # Forward pass
            self.forward(inputs)

            # Backpropagation
            output_error = targets - self.output
            output_delta = output_error * self.sigmoid_derivative(self.output)

            hidden_error = output_delta.dot(self.weights_hidden_output.T)
            hidden_delta = hidden_error * self.sigmoid_derivative(self.hidden_activation)

            # Update weights and biases
            self.weights_hidden_output += self.hidden_activation.T.dot(output_delta) * learning_rate
            self.bias_output += np.sum(output_delta, axis=0, keepdims=True) * learning_rate

            self.weights_input_hidden += inputs.T.dot(hidden_delta) * learning_rate
            self.bias_hidden += np.sum(hidden_delta, axis=0, keepdims=True) * learning_rate

            if epoch % 100 == 0:
                error = np.mean(np.abs(output_error))
                print(f"Epoch {epoch}, Error: {error}")

    def plot_structure(self):
        G = nx.DiGraph()

        # Add nodes
        for i in range(self.weights_input_hidden.shape[0]):
            G.add_node(f'Input {i+1}')

        for i in range(self.weights_input_hidden.shape[1]):
            G.add_node(f'Hidden {i+1}')

        G.add_node('Output')

        # Add edges
        for i in range(self.weights_input_hidden.shape[0]):
            for j in range(self.weights_input_hidden.shape[1]):
                G.add_edge(f'Input {i+1}', f'Hidden {j+1}', weight=self.weights_input_hidden[i, j])

        for i in range(self.weights_hidden_output.shape[0]):
            G.add_edge(f'Hidden {i+1}', 'Output', weight=self.weights_hidden_output[i, 0])

        # Draw the graph
        pos = nx.spring_layout(G)
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=1000, node_color='skyblue')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

        plt.show()

if __name__ == "__main__":
    # Example usage
    input_size = 2
    hidden_size = 4
    output_size = 1

    neural_network = NeuralNetwork(input_size, hidden_size, output_size)

    # Example training data (XOR problem)
    inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    targets = np.array([[0], [1], [1], [0]])

    # Train the neural network
    neural_network.train(inputs, targets, learning_rate=0.1, epochs=1000)

    # Test the trained network
    for i in range(len(inputs)):
        prediction = neural_network.forward(inputs[i])
        print(f"Input: {inputs[i]}, Prediction: {prediction}")

    # Plot the neural network structure
    neural_network.plot_structure()
