# Artificial Neural Network

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Churn_Modelling.csv')
X = dataset.iloc[:, 3:13].values
y = dataset.iloc[:, 13].values

# Encoding categorical data - transforming all text into numbers for consistency
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X_1 = LabelEncoder() 
X[:, 1] = labelencoder_X_1.fit_transform(X[:, 1])
labelencoder_X_2 = LabelEncoder() 
X[:, 2] = labelencoder_X_2.fit_transform(X[:, 2])
onehotencoder = OneHotEncoder(categorical_features = [1])
X = onehotencoder.fit_transform(X).toarray() 
X = X[:, 1:] # removing the 1st dummy variable

# Splitting the dataset into the Training set and Test set --> Cross Validation Set!?
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Importing the Keras libraries & packages
import keras
from keras.models import Sequential
from keras.layers import Dense

# Intialise ANN, adding input layer, 2 hidden layers & output layer, Compiling ANN
classifier = Sequential()
classifier.add(Dense(output_dim = 6, init = 'uniform', activation = 'relu', input_dim = 11 )) #avg of features & output layer 
classifier.add(Dense(output_dim = 6, init = 'uniform', activation = 'relu')) # 2nd hidden layer using rectifier function
classifier.add(Dense(output_dim = 1, init = 'uniform', activation = 'sigmoid')) # output layer using sigmoid function
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

# Fitting ANN to training set
classifier.fit(X_train, y_train, batch_size = 10, nb_epoch = 100) # how to choose & interpret??

# Predicting the Test set results
y_pred = classifier.predict(X_test)
y_pred = (y_pred > 0.5)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
