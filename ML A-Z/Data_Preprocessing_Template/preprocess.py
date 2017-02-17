# Importing libraries
import numpy as np # mathematical/ statistical  models 
import matplotlib.pyplot as plt #Great visual graphs plotting 
import pandas as pd # importing & managing datasets 

# Importing dataset
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values #creating a matrix from all rows, and all columns except last 
y = dataset.iloc[:, 3].values #dependent variables

# Handling missing data - filling up blanks with mean value
from sklearn.preprocessing import Imputer 
imputer = Imputer(missing_values = 'NaN', strategy = "mean", axis = 0) #cmd I to view class args 
imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3]) #but why 1:3?

# Encoding categorical data - transforming all text into numbers for consistency 
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder() #instantiating class to transform each country into numbers
X[:, 0] = labelencoder_X.fit_transform(X[:, 0]) 
onehotencoder = OneHotEncoder(categorical_features = [0])
X = onehotencoder.fit_transform(X).toarray() #transforms numbers into binary code 
labelencoder_y = LabelEncoder() #instantiating class to transform each country into numbers
y = labelencoder_y.fit_transform(y) #dummy variable concept 

# Creating training-set & test-set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2, random_state = 0) #80% train, 20% test

# Feature Scaling - normalising attributes to minimise effect of squares in cost function
from sklearn.preprocessing import StandardScaler 
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test) #why no need to fit? 





