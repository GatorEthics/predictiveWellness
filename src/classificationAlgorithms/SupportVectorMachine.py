"""A program for Support Vector Machine classification with individual health data."""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
dataset = pd.read_csv("testingData.csv")

X = dataset.drop("Health", axis=1)
y = dataset["Health"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

classifier = SVC(kernel="linear")
classifier.fit(x_train, y_train)

prediction = classifier.predit(x_test)

print(confusion_matrix(y_test, prediction))
print(classification_report(y_test, prediction))
