"""A program for Naieve Bayes classification with individual health data."""

import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics


def import_data():
    # Import csv file of individual data as pandas dataframe to use for training/testing data
    dataset = pd.read_csv("testingData.csv")
    # Print the dataset shape
    print("Dataset Length: ", len(dataset))
    print("Dataset Shape: ", dataset)
    # Return data
    return dataset


def split_data(dataset):
    X = dataset.drop("Health", axis=1)
    y = dataset["Health"]

    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    return X, y, x_train, x_test, y_train, y_test


def classify(x_train, y_train):
    # Train the model with the training set
    gaussian = GaussianNB()
    gaussian = gaussian.fit(x_train, y_train)

    return gaussian


def predict(classifier, x_test):
    GH = 0
    MS = 0
    # Make predictions on the testing set
    prediction = classifier.predict(x_test)

    for i in prediction:
        if i == 0:
            GH = GH + 1
        if i == 1:
            MS = MS + 1

    if GH > MS:
        print("Overall good health")
    else:
        print("Overall Metabolic Syndrome")

    print("Gaussian Naive Bayes model accuracy(in %):", metrics.accuracy_score(y_test, prediction)*100)


if __name__ == "__main__":
    data = import_data()
    X, Y, x_train, x_test, y_train, y_test = split_data(data)
    classifier = classify(x_train, y_train)
    predict(classifier, x_test)
