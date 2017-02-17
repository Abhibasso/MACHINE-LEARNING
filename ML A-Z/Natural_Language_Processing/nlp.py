# Natural Language Processing

import numpy as np # mathematical/ statistical  models 
import matplotlib.pyplot as plt #Great visual graphs plotting 
import pandas as pd # importing & managing datasets 

# Importing dataset
dataset = pd.read_csv('Restaurant_Reviews.tsv', delimiter = '\t', quoting = 3) #ignoring double quotes

# Cleaning the texts - removing numbers, punctuation, useless words, stemming
import re 
import nltk
nltk.download('stopwords') # list of useless words 
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
corpus  = []
for i in range(0, 1000):
    review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i]) # what you want to keep, replace rest w space
    review = review.lower() # change all letters to lowercase
    review = review.split() # changing each sentence into a list of words
    ps = PorterStemmer() # Stemming - keep only the root of the word, removing tenses
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))] #for loop to keep only words that are not in stopwords
    review = ' '.join(review) #joining the word list back together, with spacing
    corpus.append(review)
              
# Creating the Bag-Of-Words Model (Minimising Sparcity via Tolkenization)
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500) # creating the maxtrix but keeping most freq 1500 words
X = cv.fit_transform(corpus).toarray()
y = dataset.iloc[:, 1].values

# Using Training Naive Bayes To Predict

# Splitting the dataset into the Training set and Test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Fitting classifier to the Training set
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

# Visualising the Training set results
from matplotlib.colors import ListedColormap
X_set, y_set = X_train, y_train
X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),
                     np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))
plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.75, cmap = ListedColormap(('red', 'green')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
                c = ListedColormap(('red', 'green'))(i), label = j)
plt.title('Maive bayes Classifier (Training set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()

# Visualising the Test set results
from matplotlib.colors import ListedColormap
X_set, y_set = X_test, y_test
X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 1, stop = X_set[:, 0].max() + 1, step = 0.01),
                     np.arange(start = X_set[:, 1].min() - 1, stop = X_set[:, 1].max() + 1, step = 0.01))
plt.contourf(X1, X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.75, cmap = ListedColormap(('red', 'green')))
plt.xlim(X1.min(), X1.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(y_set)):
    plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1],
                c = ListedColormap(('red', 'green'))(i), label = j)
plt.title('Maive Bayes Classifier (Test set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()