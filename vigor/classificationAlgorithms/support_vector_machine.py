"""A program for Support Vector Machine classification with individual health data."""
import pandas as pd
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC


def import_data():
    """Read a csv file as pandas dataframe."""
    # Import csv file of individual data as pandas dataframe to use for training/testing data
    dataset = pd.read_csv(
        "/home/maddykapfhammer/Documents/Allegheny/MozillaFellows/predictiveWellness/src/dataFiles/customIndividual.csv"
    )
    # Print the dataset shape
    print("Dataset Length: ", len(dataset))
    print("Dataset Shape: ", dataset)
    # Return data
    return dataset


def split_data(dataset):
    """Split dataset into testing and training data."""
    X = dataset.drop("Health", axis=1)
    y = dataset["Health"]

    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    return X, y, x_train, x_test, y_train, y_test


def classify(x_train, x_test, y_train, y_test):
    """Create a classifier."""
    classifier = SVC(kernel="linear")
    classifier.fit(x_train, y_train)
    return classifier


def predict(classifier, x_test, y_test):
    """Make prediction based on classifier and testing data."""
    prediction = classifier.predict(x_test)

    matrix = confusion_matrix(y_test, prediction)
    report = classification_report(y_test, prediction)

    return prediction, matrix, report


def interpret_prediction(prediction):
    """Interpret a prediction and determine health risks."""
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


def perform_methods(data):
    """Perform all functions for classification."""
    # data = import_data()
    X, Y, x_train, x_test, y_train, y_test = split_data(data)
    classifier = classify(x_train, x_test, y_train, y_test)
    prediction, matrix, report = predict(classifier, x_test, y_test)
    interpretation = interpret_prediction(prediction)
    print(matrix)
    print(report)
    print(interpretation)
    return interpretation


if __name__ == "__main__":
    perform_methods()
