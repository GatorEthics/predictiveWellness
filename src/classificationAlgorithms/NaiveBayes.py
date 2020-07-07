"""A program for Naieve Bayes classification with individual health data."""

import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics


def import_data():
    # Import csv file of individual data as pandas dataframe to use for training/testing data
    dataset = pd.read_csv("/home/maddykapfhammer/Documents/Allegheny/MozillaFellows/predictiveWellness/src/customIndividual.csv")
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


def predict(classifier, x_test):
    good_health = 0
    cd = 0
    ms = 0
    diabetes = 0
    cd_ms_diabetes = 0
    cd_ms = 0
    cd_diabetes = 0
    ms_diabetes = 0
    prediction_list = []
    # Make predictions on the testing set
    prediction = classifier.predict(x_test)
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
        overall = "Good health"
    if largest == cd_ms_diabetes:
        overall = "Cardiovascular disease, Metabolic syndrome, Type II diabetes"
    if largest == cd_ms:
        overall = "Cardiovascular disease, Metabolic syndrome"
    if largest == cd_diabetes:
        overall = "Cardiovascular disease, Type II diabetes"
    if largest == ms_diabetes:
        overall = "Metabolic syndrome, Type II diabetes"
    if largest == cd:
        overall = "Cardiovascular disease"
    if largest == ms:
        overall = "Metabolic syndrome"
    if largest == diabetes:
        overall = "Type II diabetes"

    print(overall)

    print("Gaussian Naive Bayes model accuracy(in %):", metrics.accuracy_score(y_test, prediction)*100)


if __name__ == "__main__":
    data = import_data()
    X, Y, x_train, x_test, y_train, y_test = split_data(data)
    classifier = classify(x_train, y_train)
    predict(classifier, x_test)
