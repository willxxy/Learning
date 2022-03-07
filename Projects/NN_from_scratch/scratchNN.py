import numpy as np

def sigmoid(x):
    return 1/(1+ np.exp(-x))

def deriv_sigmoid(x):
    #derivative of sigmoid
    fx = sigmoid(x)
    return fx * (1-fx)

def mse(y_true, y_pred):
    #y_true and y_pred are np arrays of same length
    return ((y_true  - y_pred)**2).mean()

class Neuron:
    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias

    def feedforward(self, inputs):
        total = np.dot(self.weights, inputs) + self.bias
        return sigmoid(total)

weights = np.array([0, 1]) #w1 = 0 ; w2 = 0
bias = 0
n = Neuron(weights, bias)

x = np.array([2, 3]) #x1 = 2 ; x2 = 3
#print("Without hidden layers: " , n.feedforward(x)) #0.9990889488055994 for b=4; 0.9525741268224334 for b = 0


class OurNN:
    '''
    nn with 2 inputs, hidden layers (h1, h2), output layer with 1 neuron (o1)
    each neuron has w = [0,1] and b = 0
    '''

    def __init__(self):
        #weights
        self.w1 = np.random.normal()
        self.w2 = np.random.normal()
        self.w3 = np.random.normal()
        self.w4 = np.random.normal()
        self.w5 = np.random.normal()
        self.w6 = np.random.normal()

        #bias
        self.b1 = np.random.normal()
        self.b2 = np.random.normal()
        self.b3 = np.random.normal()

        # using neuron class
        #self.h1 = Neuron(weights, bias)
        #self.h2 = Neuron(weights, bias)
        #self.o1 = Neuron(weights, bias)
        

    def feedforward(self, x):
        #x is np array with 2 elements
        h1 = sigmoid(self.w1 * x[0] + self.w2 * x[1] + self.b1)
        h2 = sigmoid(self.w3 * x[0] + self.w4 * x[1] + self.b2)

        #the inputs for o1 are the outputs from h1 and h2
        o1 = sigmoid(self.w5 * h1 + self.w6 * h2 + self.b3)

        return o1

    def train(self, data, all_y_trues):
        '''
        data is a (n x 2) np array ; n = # of samples in dataset
        all_y_trues is a np array with n elements
        '''
        learn_rate = 0.0001
        epochs = 1000

        for epoch in range(epochs):
            for x, y_true in zip(data, all_y_trues):
                # --- do a feedforward
                sum_h1 = self.w1 * x[0] + self.w2 * x[1] + self.b1
                h1 = sigmoid(sum_h1)

                sum_h2 = self.w3 * x[0] + self.w4 * x[1] + self.b2
                h2 = sigmoid(sum_h2)

                sum_o1 = self.w5 * h1 + self.w6 * h2 + self.b3
                o1 = sigmoid(sum_o1)
                y_pred= o1

                #calculate partial derivatives
                #d_L_d_ypred = partial L/ partial ypred

                d_L_d_ypred = -2 * (y_true - y_pred)

                #Neuron o1
                d_ypred_d_w5 = h1 * deriv_sigmoid(sum_o1)
                d_ypred_d_w6 = h2 * deriv_sigmoid(sum_o1)
                d_ypred_d_b3 = deriv_sigmoid(sum_o1)

                d_ypred_d_h1 = self.w5 * deriv_sigmoid(sum_o1)
                d_ypred_d_h2 = self.w6 * deriv_sigmoid(sum_o1)

                # Neuron h1
                d_h1_d_w1 = x[0] * deriv_sigmoid(sum_h1)
                d_h1_d_w2 = x[1] * deriv_sigmoid(sum_h1)
                d_h1_d_b1 = deriv_sigmoid(sum_h1)

                # Neuron h2
                d_h2_d_w3 = x[0] * deriv_sigmoid(sum_h2)
                d_h2_d_w4 = x[1] * deriv_sigmoid(sum_h2)
                d_h2_d_b2 = deriv_sigmoid(sum_h2)

                #update weights and biases
                #Neuron h1
                self.w1 -= learn_rate * d_L_d_ypred * d_ypred_d_h1 * d_h1_d_w1
                self.w2 -= learn_rate * d_L_d_ypred * d_ypred_d_h1 * d_h1_d_w2
                self.b1 -= learn_rate * d_L_d_ypred * d_ypred_d_h1 * d_h1_d_b1

                #Neuron h2
                self.w3 -= learn_rate * d_L_d_ypred * d_ypred_d_h2 * d_h2_d_w3
                self.w4 -= learn_rate * d_L_d_ypred * d_ypred_d_h2 * d_h2_d_w4
                self.b2 -= learn_rate * d_L_d_ypred * d_ypred_d_h2 * d_h2_d_b2

                #Neuron o1
                self.w5 -= learn_rate * d_L_d_ypred * d_ypred_d_w5
                self.w6 -= learn_rate * d_L_d_ypred * d_ypred_d_w6
                self.b3 -= learn_rate * d_L_d_ypred * d_ypred_d_b3

                #calculate total loss at the end of each epoch
            if epoch % 10 == 0:
                y_preds = np.apply_along_axis(self.feedforward, 1, data)
                loss = mse(all_y_trues, y_pred)
                print("Epoch %d loss: %.3f" % (epoch, loss))




#define dataset
data = np.array([
    [-2, -1], #Alice
    [25, 6],  #Bob
    [17, 4],  #Charlie
    [-15, -6] #Diana
    ])

all_y_trues = np.array([
    1, #Alice
    0, #Bob
    0, #Charlie
    1 #Diana
    ])

#train nn
network = OurNN()
network.train(data, all_y_trues)


# Make some predictions
emily = np.array([-7, -3]) # 128 pounds, 63 inches
frank = np.array([20, 2])  # 155 pounds, 68 inches
print("Emily: %.3f" % network.feedforward(emily)) # 0.951 - F
print("Frank: %.3f" % network.feedforward(frank)) # 0.039 - M




network = OurNN()
x = np.array([2,3])
#print("With 2 hidden layers: ", network.feedforward(x)) # 0.7216325609518421




y_true = np.array([1, 0, 0, 1])
y_pred = np.array([0, 0, 0, 0])

#print(mse(y_true, y_pred)) #0.5
        




