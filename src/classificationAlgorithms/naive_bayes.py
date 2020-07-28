"""A program for Naieve Bayes classification with individual health data."""

import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics


def import_data():
    # Import csv file of individual data as pandas dataframe to use for training/testing data
    dataset = pd.read_csv("/home/maddykapfhammer/Documents/Allegheny/MozillaFellows/predictiveWellness/src/dataFiles/customIndividual.csv")
    # dataset.drop("MS")
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


def predict(classifier, x_test, y_test):
    # Make predictions on the testing set
    prediction = classifier.predict(x_test)
    # print(overall)
    print("Gaussian Naive Bayes model accuracy(in %):", metrics.accuracy_score(y_test, prediction) * 100)
    return prediction


def interpret_prediction(prediction):
    good_health = 0
    cd = 0
    ms = 0
    diabetes = 0
    cd_ms_diabetes = 0
    cd_ms = 0
    cd_diabetes = 0
    ms_diabetes = 0
    prediction_list = []
    for i in prediction:
        if i == 0:
            good_health += 1
        if i == 9:
            cd_ms_diabetes += 1
        if i == 5:
            cd_ms += 1
        if i == 6:
            cd_diabetes += 1
        if i == 7:
            ms_diabetes += 1
        if i == 4:
            cd += 1
        if i == 3:
            ms += 1
        if i == 2:
            diabetes += 1
    prediction_list.append(good_health)
    prediction_list.append(cd_ms_diabetes)
    prediction_list.append(cd_ms)
    prediction_list.append(cd_diabetes)
    prediction_list.append(ms_diabetes)
    prediction_list.append(cd)
    prediction_list.append(ms)
    prediction_list.append(diabetes)
    largest = max(prediction_list)
    if largest == good_health:
        health = "Good health"
    if largest == cd_ms_diabetes:
        health = "Cardiovascular disease, Metabolic syndrome, Type II diabetes"
    if largest == cd_ms:
        health = "Cardiovascular disease, Metabolic syndrome"
    if largest == cd_diabetes:
        health = "Cardiovascular disease, Type II diabetes"
    if largest == ms_diabetes:
        health = "Metabolic syndrome, Type II diabetes"
    if largest == cd:
        health = "Cardiovascular disease"
    if largest == ms:
        health = "Metabolic syndrome"
    if largest == diabetes:
        health = "Type II diabetes"
    return health


def perform_methods():
    data = import_data()
    X, Y, x_train, x_test, y_train, y_test = split_data(data)
    classifier = classify(x_train, y_train)
    prediction = predict(classifier, x_test, y_test)
    interpretation = interpret_prediction(prediction)
    print(interpretation)
    return interpretation


if __name__ == "__main__":
    perform_methods()
