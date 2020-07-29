"""A program to create a Streamlit web interface for Vigor."""
import classificationAlgorithms.decision_tree as decision_tree
import classificationAlgorithms.naive_bayes as naive_bayes
import classificationAlgorithms.support_vector_machine as svm
import createData.comprehensive_individual_labeling as label
import createData.create_custom_individual as custom_individual
import createData.create_individual_data as provided_individual
import streamlit as st


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
    height = st.number_input("Please enter your height (in inches", min_value=1.0)
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
    data = provided_individual.main()
    st.dataframe(data)
    return data


def create_custom_individual(age, activity_level):
    """Create data for personalized individual info."""
    # Create individual data and print dataframe
    data = custom_individual.main(age, activity_level)
    st.dataframe(data)
    return data


def label_data(data):
    """Label the data in the dataframe with health risks."""
    label.main()
    st.dataframe(data)


def classify_data(data):
    """Classify data and health risks with selected classification."""
    classification_method = st.multiselect(
        "Please select preferred classification",
        [
            "Naive Bayes Classification",
            "Support Vector Machine Classification",
            "Decision Tree Classification",
        ],
    )
    if classification_method == "Naive Bayes Classification":
        data = naive_bayes.import_data(data)
        st.dataframe(data)


def individual_analysis():
    """Perform analysis for individual data."""
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


def follow():
    """Give contact information with images."""
    st.title("Follow Us")
    st.image(
        # pylint: disable=C0301
        "/home/maddykapfhammer/Documents/Allegheny/MozillaFellows/predictiveWellness/src/webInterface/VigorImages/github.png",
        width=500,
    )
    st.image(
        # pylint: disable=C0301
        "/home/maddykapfhammer/Documents/Allegheny/MozillaFellows/predictiveWellness/src/webInterface/VigorImages/instagram.png",
        width=300,
    )
    st.image(
        # pylint: disable=C0301
        "/home/maddykapfhammer/Documents/Allegheny/MozillaFellows/predictiveWellness/src/webInterface/VigorImages/website.png",
        width=400,
    )


def setup():
    """Perform setup for Streamlit webinterface."""
    st.image(
        # pylint: disable=C0301
        "/home/maddykapfhammer/Documents/Allegheny/MozillaFellows/predictiveWellness/src/webInterface/VigorImages/vigor.png",
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
            "/home/maddykapfhammer/Documents/Allegheny/MozillaFellows/predictiveWellness/src/webInterface/home_page.md"
        ) as home_file:
            st.markdown(home_file.read())
        follow()
    if home_menu == "Data Generation with Faker":
        with open(
            # pylint: disable=C0301
            "/home/maddykapfhammer/Documents/Allegheny/MozillaFellows/predictiveWellness/src/dataGenerationWithFaker/faker_instructions.md"
        ) as faker_file:
            st.markdown(faker_file.read())
        follow()
    if home_menu == "Understanding Classification Algorithms":
        with open(
            # pylint: disable=C0301
            "/home/maddykapfhammer/Documents/Allegheny/MozillaFellows/predictiveWellness/src/classificationAlgorithms/classification_description.md"
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
            "/home/maddykapfhammer/Documents/Allegheny/MozillaFellows/predictiveWellness/src/webInterface/about.md"
        ) as about:
            st.markdown(about.read())
        follow()


if __name__ == "__main__":
    setup()
