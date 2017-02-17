# Natural Language Processing

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('mbti_data.tsv', delimiter = '\t', quoting = 3)

# Cleaning the Tweets
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
corpus = []
for i in range(0, 1200):
    review = re.sub('[^a-zA-Z]', ' ', dataset['Tweet'][i])
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)

# Creating the Bag of Words model
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500) #How does this affect?
X = cv.fit_transform(corpus).toarray()
y = dataset.iloc[:, 2].values

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)


# ------- NAIVE BAYES -------- ACCURACY ~ 41.25% 

# Fitting Naive Bayes to training set
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix #How to interpret 4 x 4 confusion matrix?
cm = confusion_matrix(y_test, y_pred)

# ------- KERNEL SVM -------- ACCURACY ~ 35.83%% 

# Fitting SVM to the Training set
from sklearn.svm import SVC
classifier = SVC(kernel = 'linear', random_state = 0) #what do all the different kernels do?
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

# ------- RANDOM FOREST -------- ACCURACY ~ 44.58%% 

# Fitting classifier to the Training set
from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators = 300, criterion = 'entropy', random_state = 0)
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

# ------- K NEAREST NEIGHBOURS -------- ACCURACY ~ 25.83%% 

# Fitting classifier to the Training set
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p = 2)
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

# ------- LOGISTIC REGRESSION CLASSIFIER -------- ACCURACY ~ 25.83%% 

# Fitting a Logistic Regression To The Training Set
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)
classifier.fit(X_train, y_train)

# Predicting the test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred) # true = (65 + 24), false = (8 + 3)

# ------- ARTIFICAL NEURAL NETWORKS --------

# Importing the Keras libraries & packages
import keras
from keras.models import Sequential
from keras.layers import Dense

# Intialise ANN, adding input layer, 2 hidden layers & output layer, Compiling ANN
classifier = Sequential()
classifier.add(Dense(output_dim = 6, init = 'uniform', activation = 'relu', input_dim = 1500 )) #avg of features & output layer
classifier.add(Dense(output_dim = 6, init = 'uniform', activation = 'relu')) # 2nd hidden layer using rectifier function
classifier.add(Dense(output_dim = 1, init = 'uniform', activation = 'sigmoid')) # output layer using sigmoid function
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy'])

# Fitting ANN to training set
classifier.fit(X_train, y_train, batch_size = 10, nb_epoch = 10) # how to choose & interpret??

# Predicting the Test set results
y_pred = classifier.predict(X_test)
y_pred = (y_pred > 0.5)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)