import streamlit as st
import createData.custom_individual as custom_individual
import createData.createIndividualData as provided_individual
import createData.comprehensiveIndividualLabeling as label
import classificationAlgorithms.SupportVectorMachine as svm
import classificationAlgorithms.NaiveBayes as naive_bayes


def individual_analysis_type():
    individual_data = st.selectbox(
        "Would you like to analyze provided or customized data?",
        [
            "Provided",
            "Customized"
        ],
    )
    return individual_data


def customized_setup():
    age = st.number_input("Please enter your age (in years)", min_value=1)
    weight = st.number_input("Please enter your weight (in pounds)", min_value=1.0)
    height = st.number_input("Please enter your height (in inches", min_value=1.0)
    activity_level = st.slider("Please enter your activity level", min_value=1, max_value=5, value=None)
    if activity_level == 1:
        st.write("Level 1: Extremely inactive")
    if activity_level == 2:
        st.write("Level 2: Sedentary lifestyle (little to no exercise)")
    if activity_level == 3:
        st.write("Level 3: Moderately active")
    if activity_level == 4:
        st.write("Level 4: Vigorously active")
    if activity_level == 5:
        st.write("Level 5: Extremely active (competitive athlete)")
    kilograms = weight * 0.453592
    meters_squared = height * 0.00064516
    bmi = kilograms / meters_squared
    return age, weight, height, activity_level, bmi


def create_provided_individual():
    data = provided_individual.main()
    st.dataframe(data)
    return data


def create_custom_individual(age, activity_level):
    # Create individual data and print dataframe
    data = custom_individual.main(age, activity_level)
    st.dataframe(data)
    return data


def label_data(data):
    label.main(data)
    st.dataframe(data)


def classify_data(data):
    classification_method = st.multiselect(
        "Please select preferred classification",
        [
            "Naive Bayes Classification",
            "Support Vector Machine Classification",
            "Decision Tree Classification"
        ]
    )
    if(classification_method == "Naive Bayes Classification"):
        data = naive_bayes.import_data(data)
        st.dataframe(data)


def setup():
    st.title("Welcome to Vigor!")
    st.sidebar.title("Welcome to Vigor!")
    menu = st.sidebar.selectbox(
        "Menu",
        [
            "Home",
            "Data Generation with Faker",
            "Classification Algorithms",
            "Individual Health Analysis",
            "Community Health Analysis"
        ],
    )
    if menu == "Home":
        with open("README.md") as readme_file:
            st.markdown(readme_file.read())
    if menu == "Data Generation with Faker":
        with open("/home/maddykapfhammer/Documents/Allegheny/MozillaFellows/predictiveWellness/src/faker/fakerInstructions.md") as faker_file:
            st.markdown(faker_file.read())
    if menu == "Classification Algorithms":
        with open("/home/maddykapfhammer/Documents/Allegheny/MozillaFellows/predictiveWellness/src/classificationAlgorithms/classificationAlgorithms.md") as classification:
            st.markdown(classification.read())
    if menu == "Individual Health Analysis":
        individual_data = individual_analysis_type()
        if individual_data == "Customized":
            age, weight, height, activity_level, bmi = customized_setup()
            data = create_custom_individual(age, activity_level)
            labeled_data = label_data(data)
            classify_data(labeled_data)
        if individual_data == "Provided":
            data = create_provided_individual()
            labeled_data = label_data(data)
            classify_data(labeled_data)
    if menu == "Community Health Analysis":
        st.write("Comming Soon!")


if __name__ == "__main__":
    setup()
