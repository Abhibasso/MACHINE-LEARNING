# Data Preprocessing Template

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('50_Startups.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values
# Encoding categorical data - transforming all text into numbers for consistency
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder() #instantiating class to transform each country into numbers
X[:, 3] = labelencoder_X.fit_transform(X[:, 3])
onehotencoder = OneHotEncoder(categorical_features = [3])
X = onehotencoder.fit_transform(X).toarray() #transforms numbers into binary code
# Avoiding the dummy variable trap by removing 1st dummy, but why?
X = X[:, 1:]
# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
# Feature Scaling
"""from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)"""
# Fitting Multiple Linear Regression To Training Set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)
# Predicting test set results
y_pred = regressor.predict(X_test)
# Building optimal model using Backwards Elimination 
import statsmodels.formula.api as sm 
X = np.append(arr = np.ones((50, 1)).astype(int), values = X, axis = 1) #adding ones column?
X_opt = X[:, [0,1,2,3,4,5]] #X_opt ideally contains only features that correlate well 
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit() #Fit full model with all possible predictors, 
#minimizing sum of the squares of dataset vs predicted by a linear function of a set of explanatory variables 
regressor_OLS.summary()
X_opt = X[:, [0,1,3,4,5]] # remove feature with highest p-value
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit() 
regressor_OLS.summary()
X_opt = X[:, [0,1,3,4,5]] # remove feature with highest p-value
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit() 
regressor_OLS.summary()
X_opt = X[:, [0,3,4,5]] # remove feature with highest p-value
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit() 
regressor_OLS.summary()
X_opt = X[:, [0,3,5]] # remove feature with highest p-value
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit() 
regressor_OLS.summary()
X_opt = X[:, [0,3]] # remove feature with highest p-value
regressor_OLS = sm.OLS(endog = y, exog = X_opt).fit() 
regressor_OLS.summary()


#Questions: 
# What is p-value again? why must remove if p-value < 0.05?
# How to interpret all OLS summary results?
# What happens after backwards elimination? The model we use only has 1 feature?
