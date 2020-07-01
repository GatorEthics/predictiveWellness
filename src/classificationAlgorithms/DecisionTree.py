"""A program for decision tree classification with individual health data."""

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

individual_data = pd.read_csv("individual_data.csv")


feature_columns = ["Steps", "Minutes_sitting", "Minutes_moderate_activity", "Minutes_intense_activity"]

independent = individual_data[feature_columns]

dependent = individual_data.label

independent_train, independent_test, dependent_train, dependent_test = train_test_split(independent, dependent, test_size = 0.3)

classifier = DecisionTreeClassifier()

classifier = classifier.fit(independent_train, dependent_train)

dependent_prediction = classifier.predict(independent_test)

print("Accuracy: ",metrics.accuracy_score(dependent_test, dependent_prediction))