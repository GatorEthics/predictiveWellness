"""A program to create a Streamlit web interface for Vigor."""
import decision_tree
import naive_bayes
import support_vector_machine as svm
import health_query
from createData import comprehensive_individual_labeling as label
from createData import create_custom_individual as custom_individual
from createData import create_individual_data as provided_individual


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
    height = st.number_input("Please enter your height (in inche)s", min_value=1.0)
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
    # classification = st.text_input("What classification would you like to query results from?")
    amount = st.number_input("How many articles would you like to read?", min_value=1)
    start_query = st.button("Perform search for health risks")
    if start_query:
        results = health_query.perform_methods(classification, data_type, amount)
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


def follow():
    """Give contact information with images."""
    st.title("Follow Us")
    st.image(
        # pylint: disable=C0301
        "/home/maddykapfhammer/Documents/Allegheny/MozillaFellows/predictiveWellness/vigor/webInterface/VigorImages/github.png",
        width=500,
    )
    st.image(
        # pylint: disable=C0301
        "/home/maddykapfhammer/Documents/Allegheny/MozillaFellows/predictiveWellness/vigor/webInterface/VigorImages/instagram.png",
        width=300,
    )
    st.image(
        # pylint: disable=C0301
        "/home/maddykapfhammer/Documents/Allegheny/MozillaFellows/predictiveWellness/vigor/webInterface/VigorImages/website.png",
        width=400,
    )


def setup():
    """Perform setup for Streamlit webinterface."""
    st.image(
        # pylint: disable=C0301
        "/home/maddykapfhammer/Documents/Allegheny/MozillaFellows/predictiveWellness/vigor/webInterface/VigorImages/vigor.png",
        width=900,
    )
    st.sidebar.title("Welcome to Vigor!")
    home_menu = st.selectbox(
        "Menu",
        [
            "Home",
            "Data Generation with Faker",
            "Understanding Classification Algorithms",
            "Individual Health Analysis",
            "Community Health Analysis",
            "About Vigor",
        ],
    )
    if home_menu == "Home":
        with open(
            # pylint: disable=C0301
            "/home/maddykapfhammer/Documents/Allegheny/MozillaFellows/predictiveWellness/vigor/webInterface/home_page.md"
        ) as home_file:
            st.markdown(home_file.read())
        follow()
    if home_menu == "Data Generation with Faker":
        with open(
            # pylint: disable=C0301
            "/home/maddykapfhammer/Documents/Allegheny/MozillaFellows/predictiveWellness/vigor/dataGenerationWithFaker/faker_instructions.md"
        ) as faker_file:
            st.markdown(faker_file.read())
        follow()
    if home_menu == "Understanding Classification Algorithms":
        with open(
            # pylint: disable=C0301
            "/home/maddykapfhammer/Documents/Allegheny/MozillaFellows/predictiveWellness/vigor/classificationAlgorithms/classification_description.md"
        ) as classification:
            st.markdown(classification.read())
        follow()
    if home_menu == "Individual Health Analysis":
        individual_analysis()
        follow()
    if home_menu == "Community Health Analysis":
        st.write("Comming Soon!")
        follow()
    if home_menu == "About Vigor":
        with open(
            # pylint: disable=C0301
            "/home/maddykapfhammer/Documents/Allegheny/MozillaFellows/predictiveWellness/vigor/webInterface/about.md"
        ) as about:
            st.markdown(about.read())
        follow()


if __name__ == "__main__":
    setup()
