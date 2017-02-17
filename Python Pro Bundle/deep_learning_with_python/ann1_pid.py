# Importing the libraries
from keras.models import Sequential 
from keras.layers import Dense
import numpy as np
seed = 7 # fix random seed for reproducibility?
np.random.seed(seed)

# Importing the dataset
dataset = np.loadtxt("pima-indians-diabetes.csv", delimiter = ",")

# Splitting into independent and dependent variables 
X = dataset[:, 0:8] # Selecting all rows from cloumns 0-7 [8 columns] as input
Y = dataset[:, 8] # Selecting all rows of column 8 as output 

# Creating Model - # https://en.wikipedia.org/wiki/Activation_function
model = Sequential()
model.add(Dense(12, input_dim = 8, init = 'uniform', activation = 'relu'))
model.add(Dense(8, init = 'uniform', activation = 'relu'))
model.add(Dense(1, init = 'uniform', activation = 'sigmoid'))

# Compile Model -  what do all parameters mean? Why choose them? Other use cases? 
model.compile(loss = 'binary_crossentropy', optimizer = 'adam', metrics = ['accuracy'])        

# Fit Model - mini-batch gradient descent to update weights every 10/150 feedforward paths
model.fit(X, Y, nb_epoch = 150, batch_size = 10) 

# Evaluate Model
scores = model.evaluate(X, Y)
print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

