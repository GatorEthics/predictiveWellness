![Vigor](vigor/writing/VigorImages/vigor.png)

[![Actions Status](https://github.com/Allegheny-Mozilla-Fellows/predictiveWellness/workflows/build/badge.svg)](https://github.com/Allegheny-Mozilla-Fellows/predictiveWellness/actions)

# Predictive Analysis with Health and Wellness Data

Allegheny College Mozilla Fellows

Dr. Jumadinova and Madelyn Kapfhammer

## Table of Contents

* [About Vigor](#about-vigor)

* [Features](#features)

* [Installing Vigor](#installing-vigor)

* [Running Vigor](#running-vigor)

* [Information for Developers](#information-for-developers)

* [Testing](#testing)
  * [Automated Testing](#automated-testing)
  * [Code Linting](#code-linting)

* [Contributing](#contributing)

* [Reading Material](#reading-material)
  * [Basics of Fitness Tracking and Wellness Apps](#basics-of-fitness-tracking-and-wellness-apps)
  * [Ethical Implications](#ethical-implications)

* [Ethical Discussions](#ethical-discussions)

* [Data and Packages Used](#data-and-packages-used)
  * [Data](#data)
  * [Packages](#packages)

* [Contact Us](#contact-us)

## About Vigor

One in five adults living in the United States use fitness trackers and health-realted apps on a daily basis. With this continuously growing statistic arise ethical concerns of big data collection, and how fitness data can be used. This project will explore and show the impacts of releasing personal data to health and exercise apps. With an artifical intelligence program, students will be able to choose what physical health data is accessible and then see what other medical information can be determined from these small pieces of recorded data. Physical health data will include calorie intake, heart rate, step count, distance walked, minutes of activity, and minutes of rest inlcuding possible other factors. Predicitive analytics will be used in combination with connection to a medical database in the Python programming language for specific medical predictions according to small pieces of information. This tool will allow students to see how health and wellness data can be used, giving them the opportunity to understand and further discuss the ethics of releasing personal information to fitness trackers and health-related applications.

The purpose of this tool is to specifically aid students in having complex conversations about data collection and the ethics surrounding it. Specifically, this tool focuses on the impact of releasing personal health and wellness information. Artifical intelligence is a quickly growing field, raising ethical debates daily. In the case of healthcare, AI is beginning to be used for both diagnostics, and personalized medicine. However, with this growing field, arise concerns related to privacy, informed consent, and patient autonomy. This tool will give students insight into how personal health data can, and often is used, allowing them to form opinions about the ethics surrounding this field. In an artifical intelligence course, one of the most important ideas is to integrate the teaching of ethics, and allow students to form their own opinions about the use and growth of AI. This program will aid in incorporating ethics into courses at Allegheny College.

## Features

## Installing Vigor

**1. Clone the Vigor repository onto your machine.**

In the appropriate directory, clone the repository with `git clone` and a following web URL or SSH key.

With HTTPS:

```
git clone https://github.com/Allegheny-Mozilla-Fellows/predictiveWellness.git
```

With SSH Key:

``` 
git clone git@github.com:Allegheny-Mozilla-Fellows/predictiveWellness.git
```

**2. Install pipenv and dependencies**

The documentation and instructions on installing pipenv can be found [Here.](https://pipenv.kennethreitz.org/en/latest/#install-pipenv-today)

`pipenv` allows dependency installation with ease. After cloning the Vigor repository, install all necessary dependencies for the tool with the command:

`pipenv install --dev`

## Running Vigor

Vigor is run in a web-based interface aided by [Streamlit](https://github.com/streamlit). For more information on designing web applications with Streamlit, please navigate to their extensive [documentation.](https://www.streamlit.io/)

In the `vigor` folder of Vigor, run `webInterface.py`, which will navigate to a web tab with the Vigor application.

`cd src`

`streamlit run web_interface.py`

## Information for Developers

When developing, install the dependencies with `pipenv install --dev` and run the program of your choice with the command: `pipenv run python program_name.py`

You can add new dependencies to `Pipfile` manually, ensuring that you place the dependency in the correct section of dependency type.

## Testing

### Automated Testing

Developers of this program can run the test suite with [Pytest](https://docs.pytest.org/en/stable/) with the command:

`pipenv run pytest`

### Code Linting

Run `pipenv run lint` to check the code of this project with linters.

Currently Vigor uses the following linters:

* [pylint](https://www.pylint.org/)
* [flake8](https://flake8.pycqa.org/en/latest/)
* [black](https://black.readthedocs.io/en/stable/)
* [pydocstyle](http://www.pydocstyle.org/en/5.0.1/)

## Contributing

We welcome everyone who is interested in helping improve Vigor! If you are interested in being a contributor, please review our [Code of Conduct](https://github.com/Allegheny-Mozilla-Fellows/predictiveWellness/blob/master/development/code_of_conduct.md) and [Guidelines for Contributors](https://github.com/Allegheny-Mozilla-Fellows/predictiveWellness/blob/master/CONTRIBUTING.md) before raising an issue, or beginning a contribution.

To raise an issue in [Vigor's Issue Tracker](https://github.com/Allegheny-Mozilla-Fellows/predictiveWellness/issues) please follow these templates:

* [bug_report.md](https://github.com/Allegheny-Mozilla-Fellows/predictiveWellness/blob/master/.github/ISSUE_TEMPLATE/bug_report.md)

* [feature_request.md](https://github.com/Allegheny-Mozilla-Fellows/predictiveWellness/blob/master/.github/ISSUE_TEMPLATE/feature_request.md)

To create a pull request please follow this template:

* [pull_request_template.md](https://github.com/Allegheny-Mozilla-Fellows/predictiveWellness/blob/master/.github/pull_request_template.md)

## Reading Material

Here is a list of articles that may give more insight into the risks of sharing your health data with online applications, and fitness companies:

**[Sharing and utilizing health data for AI applications](https://www.hhs.gov/sites/default/files/sharing-and-utilizing-health-data-for-ai-applications.pdf)**

### Basics of Fitness Tracking and Wellness Apps

* [Downside of fitness trackers and health apps is loss of privacy](https://theconversation.com/downside-of-fitness-trackers-and-health-apps-is-loss-of-privacy-69870)
@@ -50,21 +52,79 @@
* [The emerging artificial intelligence wellness landscape: Opportunities and areas of ethical debate](https://medium.com/@lkcyber/the-emerging-artificial-intelligence-wellness-landscape-802caf9638de)
* [Artificial intelligence in medicine raises legal and ethical concerns](https://theconversation.com/artificial-intelligence-in-medicine-raises-legal-and-ethical-concerns-122504#:~:text=AI%20can%20draw%20upon%20purchasing,information%20about%20an%20individual's%20health.&text=Researchers%20are%20already%20using%20AI,opioid%20abuse%20and%20even%20suicide.)
* [Sharing and utilizing health data for AI applications](https://www.hhs.gov/sites/default/files/sharing-and-utilizing-health-data-for-ai-applications.pdf)
* [Predictive analytics in health care](https://www2.deloitte.com/us/en/insights/topics/analytics/predictive-analytics-health-care-value-risks.html)
* [That mental health app might share your data without telling you](https://www.theverge.com/2019/4/20/18508382/apps-mental-health-smoking-cessation-data-sharing-privacy-facebook-google-advertising)

### Ethical Implications

* [Ethical dimensions of using artifical intelligence in Health Care](https://journalofethics.ama-assn.org/article/ethical-dimensions-using-artificial-intelligence-health-care/2019-02)
* [Privacy, compliance, and ethical issues with predictive people analytics](https://paulvanderlaken.com/2018/11/12/privacy-compliance-ethical-issues-predictive-people-analytics/)
* [Artificial intelligence in medicine raises legal and ethical concerns](https://theconversation.com/artificial-intelligence-in-medicine-raises-legal-and-ethical-concerns-122504#:~:text=AI%20can%20draw%20upon%20purchasing,information%20about%20an%20individual's%20health.&text=Researchers%20are%20already%20using%20AI,opioid%20abuse%20and%20even%20suicide.)
* [The legal and ethical concerns that arise from using complex predictive analytics in health care](https://pubmed.ncbi.nlm.nih.gov/25006139/)

## Data and Packages Used

### Data

All health and wellness data was found on [Kaggle](https://www.kaggle.com/datasets?utm_medium=paid&utm_source=google.com+search&utm_campaign=datasets&gclid=CjwKCAjwsan5BRAOEiwALzomX0ojbaAIJuDtBLWVXK-fqjFzL8ouC9YPXnfzpLCCwzwOKH4helhYcBoCzJQQAvD_BwE) and was used as an accurate basis for data generation.

* [National Institute of Health & National Library of Medicine's PubMed](https://pubmed.ncbi.nlm.nih.gov/)

* [One year of FitBit ChargeHR data by Alket Cacaj](https://www.kaggle.com/alketcecaj/one-year-of-fitbit-chargehr-data)

* [2013-2014 National Health and Nutrition Examination Survey by the CDC](https://www.kaggle.com/cdc/national-health-and-nutrition-examination-survey)

* [2017-2018 National Health and Nutrition Examination Survey](https://www.kaggle.com/moradnejad/nhanes-questionnaires-datasets-20172018-csv?)

### Packages

* [PyMed, PubMed Access Through Python](https://github.com/gijswobben/pymed)
  * A package which allows the access of informationa and articles from the [PubMed Database](https://pubmed.ncbi.nlm.nih.gov/). For full instructions on using PyMed please visit here.

* [Faker](https://faker.readthedocs.io/en/master/)
  * A package which allows the generation of fake data. For instructions on using Faker please visit [here](https://github.com/Allegheny-Mozilla-Fellows/predictiveWellness/blob/master/faker/fakerInstructions.md)

* [scikit-learn](https://scikit-learn.org/stable/)
  * An open-source package for machine learning in Python.

## Contact Us

If you have any questions or concerns about Vigor please contact:

* Dr. Jumadinova (jjumadinova@allegheny.edu)
* Madelyn Kapfhammer (kapfhammerm@allegheny.edu)

![GitHub Information](vigor/writing/VigorImages/github.png)

![Mozilla Fellows Website](vigor/writing/VigorImages/website.png)

![Allegheny Computer Science Instagram](vigor/writing/VigorImages/instagram.png)
