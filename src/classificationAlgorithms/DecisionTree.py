"""A program for decision tree classification with individual health data."""

import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report


def import_data():
    # Import csv file of individual data as pandas dataframe to use for training/testing data
    individual_data = pd.read_csv("testingData.csv")
    # Print the dataset shape
    print("Dataset Length: ", len(individual_data))
    print("Dataset Shape: ", individual_data)
    # Return data
    return individual_data


def split_dataset(individual_data):
    # Define features and target variable
    # feature_columns = ["Steps", "Minutes_sitting", "Minutes_physical_activity", "HR", "BP"]
    # target_column = ["Health"]

    # Separate the dataset based on attributes and the target variable
    # X contains attributes
    # Y contains target variable
    # X = individual_data[feature_columns].values
    # Y = individual_data[target_column].values
    X = individual_data.drop("Health", axis=1)
    Y = individual_data["Health"]
    # Split the dataset for training and testing purposes
    # Ratio of training to testing is 70:30, this can be changed with test_size
    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=100)

    return X, Y, x_train, y_train, x_test, y_test


def train_with_gini(x_train, x_test, y_train):
    """A function to perform training with the giniIndex."""
    # Create the classifier object
    classifier = DecisionTreeClassifier(criterion="gini", random_state=100, max_depth=3, min_samples_leaf=5)
    # Perform training
    classifier.fit(x_train, y_train)
    return classifier


def entropy_train(x_train, x_test, y_train):
    """A function to perform training with entropy."""
    # Create classifier object
    entropy_classifier = DecisionTreeClassifier(criterion="entropy", random_state=100, max_depth=3, min_samples_leaf=5)
    # Perform training
    entropy_classifier.fit(x_train, y_train)
    return entropy_classifier


def predict(x_test, classifier):
    """Make a prediction based on training."""
    target_prediction = classifier.predict(x_test)
    print("Predicted values:")
    print(target_prediction)
    return target_prediction


def calculate_accuracy(y_test, target_prediction):
    print("Confusion Matrix: ", confusion_matrix(y_test, target_prediction))
    print("Accuracy: ", accuracy_score(y_test, target_prediction))
    print("Report: ", classification_report(y_test, target_prediction))


if __name__ == "__main__":
    # Build
    data = import_data()
    X, Y, x_train, x_test, y_train, y_test = split_dataset(data)
    gini_classifier = train_with_gini(x_train, x_test, y_train)
    entropy_classifier = entropy_train(x_train, x_test, y_train)

    # Prediction with gini
    print("Results Using Gini Index: ")
    gini_prediction = predict(x_test, gini_classifier)
    calculate_accuracy(y_test, gini_prediction)

    # Prediction with entropy
    print("Results Using Entropy: ")
    entropy_prediction = predict(x_test, entropy_classifier)
    calculate_accuracy(y_test, entropy_prediction)
