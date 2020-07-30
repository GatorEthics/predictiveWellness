"""A program for decision tree classification with individual health data."""
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


def import_data(data_type):
    """Read a csv file as pandas dataframe."""
    # Import csv file of individual data as pandas dataframe to use for training/testing data
    if data_type == "Provided":
        dataset = pd.read_csv(
            "/home/maddykapfhammer/Documents/Allegheny/MozillaFellows/predictiveWellness/vigor/dataFiles/individual_data.csv"
        )
    if data_type == "Customized":
        dataset = pd.read_csv(
            "/home/maddykapfhammer/Documents/Allegheny/MozillaFellows/predictiveWellness/vigor/dataFiles/customIndividual.csv"
        )
    # Import csv file of individual data as pandas dataframe to use for training/testing data
    selected_columns = dataset[["Steps_taken", "Minutes_physical_activity", "Minutes_sitting", "HR", "BP", "Health"]]
    tree_data = selected_columns.copy()

    # Print the dataset shape
    # print("Dataset Length: ", len(individual_data))
    # print("Dataset Shape: ", individual_data)
    # Return data
    return tree_data


def split_dataset(individual_data):
    """Split the pandas dataframe for features and target variables."""
    # Define features and target variable
    # Separate the dataset based on attributes and the target variable

    data_predictors = [
        "Steps_taken",
        "Minutes_sitting",
        "Minutes_physical_activity",
        "HR",
        "BP",
    ]
    X = individual_data[data_predictors]
    Y = individual_data.Health

    # Split the dataset for training and testing purposes
    # Ratio of training to testing is 70:30, this can be changed with test_size
    x_train, x_test, y_train, y_test = train_test_split(X, Y, random_state=0)

    return X, Y, x_train, y_train, x_test, y_test


def train_with_gini(x_train, y_train):
    """A function to perform training with the giniIndex."""
    # Create the classifier object
    classifier = DecisionTreeClassifier(
        criterion="gini", random_state=100, max_depth=3, min_samples_leaf=5
    )
    # Perform training
    classifier.fit(x_train, y_train)
    return classifier


def entropy_train(x_train, y_train):
    """A function to perform training with entropy."""
    # Create classifier object
    entropy_classifier = DecisionTreeClassifier(
        criterion="entropy", random_state=100, max_depth=3, min_samples_leaf=5
    )
    # Perform training
    entropy_classifier.fit(x_train, y_train)
    return entropy_classifier


def predict(x_test, classifier):
    """Make a prediction based on training."""
    target_prediction = classifier.predict(x_test)
    print("Predicted values:")
    print(target_prediction)
    return target_prediction


def interpret_prediction(prediction):
    """Interpret a prediction and determine health risks."""
    prediction_list = []
    good_health = 0
    cd = 0
    ms = 0
    diabetes = 0
    cd_ms_diabetes = 0
    cd_ms = 0
    cd_diabetes = 0
    ms_diabetes = 0
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


def calculate_accuracy(y_test, target_prediction):
    """Calculate accuracy and print visuals."""
    print("Confusion Matrix: ", confusion_matrix(y_test, target_prediction))
    print("Accuracy: ", accuracy_score(y_test, target_prediction))
    print("Report: ", classification_report(y_test, target_prediction))


def perform_methods(data_type):
    """Perform all functions for classification."""
    # Build
    data = import_data(data_type)
    X, Y, x_train, y_train, x_test, y_test = split_dataset(data)
    gini_classifier = train_with_gini(x_train, y_train)
    entropy_classifier = entropy_train(x_train, y_train)

    # Prediction with gini
    gini_prediction = predict(x_test, gini_classifier)
    calculate_accuracy(y_test, gini_prediction)
    gini_interpretation = interpret_prediction(gini_prediction)
    # print(gini_interpretation)

    # Prediction with entropy
    entropy_prediction = predict(x_test, entropy_classifier)
    calculate_accuracy(y_test, entropy_prediction)
    entropy_interpretation = interpret_prediction(entropy_prediction)
    # print(entropy_interpretation)

    return gini_interpretation, entropy_interpretation


if __name__ == "__main__":
    perform_methods()
