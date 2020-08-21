"""A program to create a Streamlit web interface for Vigor."""
import decision_tree
import naive_bayes
import support_vector_machine as svm
import health_query
from createData import comprehensive_individual_labeling as label
from createData import create_custom_individual as custom_individual
from createData import create_individual_data as provided_individual
from dataGeneration import create_custom_data as customized_data

import streamlit as st
import pandas as pd


def individual_analysis_type():
    """Determine what type of individual data should be analyzed."""
    individual_data = st.selectbox(
        "Would you like to analyze provided or customized data?",
        ["Provided", "Customized"],
    )
    return individual_data


def customized_setup():
    """Input and store personal information for data generation."""
    age = st.number_input("Please enter your age (in years)", min_value=1)
    weight = st.number_input("Please enter your weight (in pounds)", min_value=1.0)
    height = st.number_input("Please enter your height (in inches)", min_value=1.0)
    activity_level = st.slider(
        "Please enter your activity level", min_value=1, max_value=5, value=None
    )
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
    """Create data for provided individual info."""
    with st.spinner("Wait for it..."):
        individual_data = pd.read_csv(
            "/home/maddykapfhammer/Documents/Allegheny/MozillaFellows/predictiveWellness/vigor/dataFiles/individual_data.csv"
        )
        data = provided_individual.main(individual_data)
        # st.dataframe(data)
        st.bar_chart(data)
        individual_data.to_csv(
            "/home/maddykapfhammer/Documents/Allegheny/MozillaFellows/predictiveWellness/vigor/dataFiles/individual_data.csv"
        )
    st.success("Complete!")
    return data


def create_custom_individual(age, activity_level):
    """Create data for personalized individual info."""
    with st.spinner("Wait for it..."):
        custom_data = pd.read_csv(
            "/home/maddykapfhammer/Documents/Allegheny/MozillaFellows/predictiveWellness/vigor/dataFiles/customIndividual.csv",
            index_col=[0],
        )
        # Create individual data and print dataframe
        st.header("Generating customized individual data....")
        data = custom_individual.main(age, activity_level, custom_data)
        st.bar_chart(data)
        custom_data.to_csv(
            "/home/maddykapfhammer/Documents/Allegheny/MozillaFellows/predictiveWellness/vigor/dataFiles/customIndividual.csv"
        )
    st.success("Complete!")
    return data


def label_data(data, data_type):
    """Label the data in the dataframe with health risks."""
    with st.spinner("Preparing labeled data..."):
        st.header("Labeling data with health risks....")
        labeled_data = label.main(data)
        if data_type == "Provided":
            labeled_data.to_csv("/home/maddykapfhammer/Documents/Allegheny/MozillaFellows/predictiveWellness/vigor/dataFiles/individual_data.csv")
        if data_type == "Customized":
            labeled_data.to_csv("/home/maddykapfhammer/Documents/Allegheny/MozillaFellows/predictiveWellness/vigor/dataFiles/customIndividual.csv")
        st.dataframe(labeled_data)
        st.success("Complete!")
    return label_data


def classify_data(dataset, data_type):
    """Classify data and health risks with selected classification."""
    interpretation = ""
    naive = False
    gini = False
    entropy = False
    support_vector = False

    # classification_type = 0
    st.header("Please Choose Your Method of Classification:")
    naive_classification = st.button("Naive Bayes Classification")
    gini_classification = st.button("Gini Index Decision Tree Classification")
    entropy_classification = st.button("Entropy Decision Tree Classification")
    svm_classification = st.button("Support Vector Machine Classification")

    if naive_classification:
        with st.spinner("Classifying with Naive Bayes..."):
            new_data = naive_bayes.import_data(data_type)
            st.area_chart(new_data["Health"])
            interpretation = naive_bayes.perform_methods(data_type)
            # classification_type = 1
            naive = True
        st.success("Complete!")

    if gini_classification:
        with st.spinner("Classifying with Gini Index..."):
            new_data = decision_tree.import_data(data_type)
            st.area_chart(new_data["Health"])
            interpretation = decision_tree.perform_gini_index(data_type)
            # classification_type = 2
            gini = True
        st.success("Complete!")

    if entropy_classification:
        with st.spinner("Classifying with Entropy..."):
            new_data = decision_tree.import_data(data_type)
            st.area_chart(new_data["Health"])
            interpretation = decision_tree.perform_entropy(data_type)
            entropy = True
            # classification_type = 3
        st.success("Complete!")

    if svm_classification:
        with st.spinner("Classifying with Support Vector Machine..."):
            new_data = svm.import_data(data_type)
            st.area_chart(new_data["Health"])
            interpretation = svm.perform_methods(data_type)
            support_vector = True
            # classification_type = 4
        st.success("Complete!")

    st.header("Health Risks:")
    st.write(interpretation)
    return naive , gini, entropy, support_vector


def query_pubmed(classification, data_type):
    st.header("Discovery with PubMed")
    filename = st.text_input('Enter a file path:')
    try:
        with open(filename) as input:
            st.text(input.read())
    except FileNotFoundError:
        st.error('File not found.')
    # classification = st.text_input("What classification would you like to query results from?")
    amount = st.number_input("How many articles would you like to read?", min_value=1)
    start_query = st.button("Perform search for health risks")
    if start_query:
        results = health_query.perform_methods(filename, classification, data_type, amount)
        # st.dataframe(results)

    for i, j in results.iterrows():
        st.header(j["Titles"])
        st.write(j["Date Published"])
        st.write(j["Abstract"])


def individual_analysis():
    """Perform analysis for individual data."""
    individual_data = individual_analysis_type()
    # classification_name = ""
    if individual_data == "Customized":
        age, weight, height, activity_level, bmi = customized_setup()
        data = create_custom_individual(age, activity_level)
        labeled_data = label_data(data, individual_data)
        naive, gini, entropy, support_vector = classify_data(labeled_data, individual_data)
        if naive is True:
            query_pubmed(1, individual_data)
        if gini is True:
            query_pubmed(2, individual_data)
        if entropy is True:
            query_pubmed(3, individual_data)
        if svm is True:
            query_pubmed(4, individual_data)
    if individual_data == "Provided":
        data = create_provided_individual()
        labeled_data = label_data(data, individual_data)
        classify_data(labeled_data, individual_data)
        query_pubmed(individual_data)


def create_personalized_data():
    filename = st.text_input('Enter a file path:')
    try:
        with open(filename) as input:
            st.text(input.read())
    except FileNotFoundError:
        st.error('File not found.')

    data = pd.read_csv(filename, index_col=0)
    data_type = st.selectbox("What type of data would you like to produce?", ["Individual", "Community"])
    amount = st.number_input("How much data would you like to be produced?", min_value=1)

    if data_type == "Community":
        create_community_data(data, amount)

    if data_type == "Individual":
        create_individual_data(data, amount)

    customized_data.remove_empty_columns(data)
    data.to_csv(filename)
    st.dataframe(data)


def create_community_data(data, amount):
    time_box = st.checkbox("Time")
    age_box = st.checkbox("Age")
    first_name_box = st.checkbox("First Name")
    last_name_box = st.checkbox("Last Name")
    ssn_box = st.checkbox("Social Security Number (SSN)")
    insurance_box = st.checkbox("Insurance Type")
    blood_type_box = st.checkbox("Blood Type")
    medication_box = st.checkbox("Medications")
    sitting_box = st.checkbox("Minutes Sitting Daily")
    active_box = st.checkbox("Minutes Active Daily")
    temperature_box = st.checkbox("Temperature")
    bp_box = st.checkbox("Blood Pressure")
    hr_box = st.checkbox("Heart Rate")
    steps_box = st.checkbox("Steps")

    if time_box is True:
        customized_data.create_time(data, amount)
    else:
        data.drop("Time", axis=1, inplace=True)
    if age_box is True:
        customized_data.create_age(data, amount)
    else:
        data.drop("Age", axis=1, inplace=True)
    if first_name_box is True:
        customized_data.create_first_name(data, amount)
    else:
        data.drop("First Name", axis=1, inplace=True)
    if last_name_box is True:
        customized_data.create_last_name(data, amount)
    else:
        data.drop("Last Name", axis=1, inplace=True)
    if ssn_box is True:
        customized_data.create_ssn(data, amount)
    else:
        data.drop("SSN", axis=1, inplace=True)
    if insurance_box is True:
        customized_data.create_insurance(data, amount)
    else:
        data.drop("Insurance", axis=1, inplace=True)
    if blood_type_box is True:
        customized_data.create_blood_type(data, amount)
    else:
        data.drop("Blood Type", axis=1, inplace=True)
    if medication_box is True:
        customized_data.create_medications(data, amount)
    else:
        data.drop("Medications", axis=1, inplace=True)
    # if sitting_box is True:
    #     customized_data.create_minutes_sitting()


def create_individual_data(data, amount):
    age = st.number_input("How old is the individual?", min_value=1)
    activity_level = st.slider(
        "What is the individual's activity level?", min_value=1, max_value=5, value=None
    )
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
    date_box = st.checkbox("Date")
    time_box = st.checkbox("Time")
    medication_box = st.checkbox("Medications")
    sitting_box = st.checkbox("Minutes Sitting Daily")
    active_box = st.checkbox("Minutes Active Daily")
    temperature_box = st.checkbox("Temperature")
    bp_box = st.checkbox("Blood Pressure")
    hr_box = st.checkbox("Heart Rate")
    steps_box = st.checkbox("Steps")

    if date_box is True:
        customized_data.create_date(data, amount)
    else:
        data.drop("Date", axis=1, inplace=True)
    if time_box is True:
        customized_data.create_time(data, amount)
    else:
        data.drop("Time", axis=1, inplace=True)
    if medication_box is True:
        customized_data.create_medications(data, amount)
    else:
        data.drop("Medications", axis=1, inplace=True)
    if sitting_box is True:
        customized_data.create_minutes_sitting(data, activity_level, amount)
    else:
        data.drop("Minutes Sitting", axis=1, inplace=True)
    if active_box is True:
        customized_data.create_minutes_active(data, age, activity_level, amount)
    else:
        data.drop("Physical Activity", axis=1, inplace=True)
    if temperature_box is True:
        customized_data.create_temperature(data, age, amount)
    else:
        data.drop("Temperature", axis=1, inplace=True)
    if bp_box is True:
        customized_data.create_blood_pressure(data, age, activity_level, amount)
    else:
        data.drop("Blood Pressure", axis=1, inplace=True)
    if hr_box is True:
        customized_data.create_heart_rate(data, age, activity_level, amount)
    else:
        data.drop("Heart Rate", axis=1, inplace=True)
    if steps_box is True:
        customized_data.create_steps(data, activity_level, amount)
    else:
        data.drop("Daily Steps", axis=1, inplace=True)


def perform_pubmed_discovery():
    filename = st.text_input('Enter a file path:')
    try:
        with open(filename) as input:
            st.text(input.read())
    except FileNotFoundError:
        st.error('File not found.')
    st.header("Discovery with PubMed")
    # classification = st.text_input("What classification would you like to query results from?")
    amount = st.number_input("How many articles would you like to read?", min_value=1)
    keywords = st.text_input("What keywords would you like to search for?")
    start_query = st.button("Perform search for health risks")
    if start_query:
        results = health_query.perform_methods_for_discovery(filename, keywords, amount)
        # st.dataframe(results)

    for i, j in results.iterrows():
        st.header(j["Titles"])
        st.write(j["Date Published"])
        st.write(j["Abstract"])


def follow():
    """Give contact information with images."""
    st.title("Follow Us")
    st.image(
        # pylint: disable=C0301
        "/home/maddykapfhammer/Documents/Allegheny/MozillaFellows/predictiveWellness/vigor/writing/VigorImages/github.png",
        width=500,
    )
    st.image(
        # pylint: disable=C0301
        "/home/maddykapfhammer/Documents/Allegheny/MozillaFellows/predictiveWellness/vigor/writing/VigorImages/instagram.png",
        width=300,
    )
    st.image(
        # pylint: disable=C0301
        "/home/maddykapfhammer/Documents/Allegheny/MozillaFellows/predictiveWellness/vigor/writing/VigorImages/website.png",
        width=400,
    )


def setup():
    """Perform setup for Streamlit webinterface."""
    st.image(
        # pylint: disable=C0301
        "/home/maddykapfhammer/Documents/Allegheny/MozillaFellows/predictiveWellness/vigor/writing/VigorImages/vigor.png",
        width=900,
    )
    st.sidebar.title("Welcome to Vigor!")
    initial_menu = st.selectbox(
        "Menu",
        [
            "Home",
            "Data Generation with Faker",
            "Discovery with PubMed",
            "Vigor's Predictive Wellness",
            "About Vigor",

        ]
    )
    if initial_menu == "Home":
        with open(
            # pylint: disable=C0301
            "/home/maddykapfhammer/Documents/Allegheny/MozillaFellows/predictiveWellness/vigor/writing/home_page.md"
        ) as home_file:
            st.markdown(home_file.read())
        follow()
    if initial_menu == "Data Generation with Faker":
        st.write("Faker")
        faker_menu = st.selectbox(
            "Faker Menu",
            [
                "Using Faker",
                "Customized Data Generation",
            ]
        )
    if initial_menu == "Discovery with PubMed":
        with open(
            # pylint: disable=C0301
            "/home/maddykapfhammer/Documents/Allegheny/MozillaFellows/predictiveWellness/vigor/writing/about_pubmed.md"
        ) as pubmed:
            st.markdown(pubmed.read())
        perform_pubmed_discovery()
        follow()
    if initial_menu == "Vigor's Predictive Wellness":
        wellness_menu = st.selectbox(
            "Predictive Wellness Menu",
            [
                "Understanding Classification Algorithms",
                "Individual Health Analysis",
                "Community Health Analysis",
            ]
        )
    if initial_menu == "About Vigor":
        with open(
            # pylint: disable=C0301
            "/home/maddykapfhammer/Documents/Allegheny/MozillaFellows/predictiveWellness/vigor/writing/about.md"
        ) as about:
            st.markdown(about.read())
        follow()

    if faker_menu == "Using Faker":
        with open(
            # pylint: disable=C0301
            "/home/maddykapfhammer/Documents/Allegheny/MozillaFellows/predictiveWellness/vigor/dataGeneration/faker_instructions.md"
        ) as faker_file:
            st.markdown(faker_file.read())
        follow()
    if faker_menu == "Customized Data Generation":
        create_personalized_data()
        follow()
    if wellness_menu == "Understanding Classification Algorithms":
        with open(
            # pylint: disable=C0301
            "/home/maddykapfhammer/Documents/Allegheny/MozillaFellows/predictiveWellness/vigor/writing/classification_description.md"
        ) as classification:
            st.markdown(classification.read())
        follow()
    if wellness_menu == "Individual Health Analysis":
        individual_analysis()
        follow()
    if wellness_menu == "Community Health Analysis":
        st.write("Comming Soon!")
        follow()


if __name__ == "__main__":
    setup()
