"""A program for Naieve Bayes classification with individual health data."""

import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GuassianNB
from sklearn import metrics


dataset = pd.read_csv("testingData.csv")

# TODO: Split data in target and features

# Split features and target (x, y) into training and testing
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.4)

# Train the model with the training set
guassian = GuassianNB()
guassian = guassian.fit(x_train, y_train)

# Make predictions on the testing set
prediction = guassian.predict(x_test)
print("Gaussian Naive Bayes model accuracy(in %):", metrics.accuracy_score(y_test, prediction)*100)
