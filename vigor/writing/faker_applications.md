# Data Generation with Faker

## Using Faker

Vigor utilizes a Python package called [Faker](https://faker.readthedocs.io/en/master/) to generate appropriate health data and vitals based on personal information. Faker is an *extremely helpful* package, that is easy to install, understand, and use for general and customzied data generation. If you are interested in learning more about Faker's providers and viewing a step-by-step tutorial, please choose the **Using Faker** menu option.

## Customized Data Generation

As a feature of Vigor, create your own csv file of customized data. This feature allows you to select an option for either individual or community data generation. Within this selection the user is able to choose the amount of data which should be produced, and what data points will be generated, including options for:

* Date
* Time
* Last Name
* First Name
* Social Security Number
* Age
* Activity Level (1-5)
* Insurance (Medicare or private)
* Medications
* Temperature
* Heart Rate
* Blood Pressure
* Physical Activity
* Minutes Sitting Daily
* Steps Taken Daily

This data is then produced in a dataframe, and also modifies the specified `.csv` file for future data usage. If you are interested in using this feature, please choose the **Customized Data Generation** menu option.
