import streamlit as st
import custom_individual as custom_individual
import createData.comprehensiveIndividualLabeling as label
import classificationAlgorithms.SupportVectorMachine as svm


def individual_setup():
    individual_data = st.selectbox(
        "Would you like to analyze provided or customized data?",
        [
            "Provided",
            "Customized"
        ],
    )
    if individual_data == "Customized":
        age = st.number_input("Please enter your age (in years)", min_value=1)
        weight = st.number_input("Please enter your weight (in pounds)", min_value=1.0)
        height = st.number_input("Please enter your height (in inches", min_value=1.0)
        activity_level = st.slider("Please enter your activity level", min_value=1, max_value=5)
        st.write("Level 1:")
        st.write("Level 2:")
        st.write("Level 3:")
        st.write("Level 4:")
        st.write("Level 5:")
        kilograms = weight * 0.453592
        meters_squared = height * 0.00064516
        bmi = kilograms / meters_squared
    return age, weight, height, activity_level, bmi


def create_custom_individual(age, activity_level):
    # Create individual data and print dataframe
    data = custom_individual.main(age, activity_level)
    st.dataframe(data)
    return data


def label_custom_individual(data):
    label.main(data)
    st.dataframe(data)


def custom_individual_classification(data):
    classification = st.multiselect(
        "Please select preferred classification",
        [
            "Naive Bayes Classification",
            "Support Vector Machine Classification",
            "Decision Tree Classification"
        ]
    )


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
        age, weight, height, activity_level, bmi = individual_setup()
        data = create_custom_individual(age, activity_level)
        label_custom_individual(data)
        

    if menu == "Community Health Analysis":
        st.write("Comming Soon!")


if __name__ == "__main__":
    setup()



