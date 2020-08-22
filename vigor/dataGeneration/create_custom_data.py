"""A program to create customized data, based on user selection."""

import numpy as np
import pandas as pd
from faker import Faker
from faker.providers import python
from faker.providers import date_time

fake = Faker()
fake.add_provider(python)
fake.add_provider(date_time)
Faker.seed(0)


def randomize_int(min, max, amount):
    """Create a list of random numbers, based on specific parameters."""
    integer_list = []
    Faker.seed(0)
    for x in range(amount):
        integer = fake.pyint(min_value=min, max_value=max, step=1)
        integer_list.append(integer)
    return integer_list


def create_age(df, amount):
    if "Age" not in df.columns:
        df["Age"] = ""
    min = 1
    max = 103
    age_list = randomize_int(min, max, amount)
    age_array = np.array(age_list)
    df["Age"] = age_array
    return age_list


def create_activity_level(df, amount):
    if "Activity Level" not in df.columns:
        df["Activity Level"] = ""
    min = 1
    max = 5
    activity_level_list = randomize_int(min, max, amount)
    activity_level_array = np.array(activity_level_list)
    df["Activity Level"] = activity_level_array
    return activity_level_list


def create_date(df, amount):
    if "Date" not in df.columns:
        df["Date"] = ""
    date_list = []
    Faker.seed(0)
    for x in range(amount):
        date = fake.date_between()
        date_list.append(date)
    date_array = np.array(date_list)
    df["Date"] = date_array


def create_time(df, amount):
    if "Time" not in df.columns:
        df["Time"] = ""
    time_list = []
    Faker.seed(0)
    for x in range(amount):
        time = fake.time()
        time_list.append(time)
    time_array = np.array(time_list)
    df["Time"] = time_array


def create_first_name(df, amount):
    if "First Name" not in df.columns:
        df["First Name"] = ""
    first_name_list = []
    Faker.seed(0)
    for x in range(amount):
        first_name = fake.first_name()
        first_name_list.append(first_name)
    first_name_array = np.array(first_name_list)
    df["First Name"] = first_name_array


def create_last_name(df, amount):
    if "Last Name" not in df.columns:
        df["Last Name"] = ""
    last_name_list = []
    Faker.seed(0)
    for x in range(amount):
        last_name = fake.last_name()
        last_name_list.append(last_name)
    last_name_array = np.array(last_name_list)
    df["Last Name"] = last_name_array


def create_ssn(df, amount):
    if "SSN" not in df.columns:
        df["SSN"] = ""
    ssn_list = []
    Faker.seed(0)
    for x in range(amount):
        ssn = fake.ssn()
        ssn_list.append(ssn)
    ssn_array = np.array(ssn_list)
    df["SSN"] = ssn_array


def create_insurance(df, amount):
    if "Insurance" not in df.columns:
        df["Insurance"] = ""
    insurance_list = []
    Faker.seed(0)
    for x in range(amount):
        insurance = fake.random_element(elements=("Medicare", "Private Insurance"))
        insurance_list.append(insurance)
    insurance_array = np.array(insurance_list)
    df["Insurance"] = insurance_array


def create_medications(df, amount):
    if "Medications" not in df.columns:
        df["Medications"] = ""
    medication_list = []
    Faker.seed(0)
    for x in range(amount):
        medication = fake.random_element(elements=("None", "Levothyroxine", "Lisinopril", "Atorvastin", "Metformin", "Amlodipine", "Metoprolol", "Omeprazole", "Simvastatin", "Losartan", "Albuterol"))
        medication_list.append(medication)
    medication_array = np.array(medication_list)
    df["Medications"] = medication_array


def create_blood_type(df, amount):
    if "Blood Type" not in df.columns:
        df["Blood Type"] = ""
    type_list = []
    # Faker.seed(0)
    for x in range(amount):
        blood_type = fake.random_element(elements=("O Positive", "O Negative", "A Positive", "A Negative", "B Positive", "B Negative", "AB Positive", "AB Negative"))
        type_list.append(blood_type)
    type_array = np.array(type_list)
    df["Blood Type"] = type_array


def create_minutes_sitting(df, activity_level, amount):
    """Create minutes sitting based on activity level."""
    if "Minutes Sitting" not in df.columns:
        df["Minutes Sitting"] = ""
    # age, activity_level = get_individual_information()
    # Minutes sitting for sedentary lifestyle
    if activity_level == 1:
        min = 660
        max = 1000
        integer_list = randomize_int(min, max, amount)
        sitting_array = np.array(integer_list)
        df["Minutes Sitting"] = sitting_array
    # Steps for low activity lifestyle
    if activity_level == 2:
        min = 480
        max = 660
        integer_list = randomize_int(min, max, amount)
        sitting_array = np.array(integer_list)
        df["Minutes Sitting"] = sitting_array
    # Steps for somewhat active lifestyle
    if activity_level == 3:
        min = 240
        max = 480
        integer_list = randomize_int(min, max, amount)
        sitting_array = np.array(integer_list)
        df["Minutes Sitting"] = sitting_array
    # Steps for active lifestyle
    if activity_level == 4:
        min = 100
        max = 240
        integer_list = randomize_int(min, max, amount)
        sitting_array = np.array(integer_list)
        df["Minutes Sitting"] = sitting_array
    # Steps for highly active lifestyle
    if activity_level == 5:
        min = 0
        max = 240
        integer_list = randomize_int(min, max, amount)
        sitting_array = np.array(integer_list)
        df["Minutes Sitting"] = sitting_array


def create_minutes_active(df, age, activity_level, amount):
    """Create physical activity based on age and activity."""
    if "Physical Activity" not in df.columns:
        df["Physical Activity"] = ""
    # age, activity_level = get_individual_information()
    # physical activity for school-aged children and adolescents (6-17)
    if 6 < age < 17:
        if 3 < activity_level < 5:
            min = 50
            max = 100
        if 1 < activity_level < 3:
            min = 30
            max = 60
        integer_list = randomize_int(min, max, amount)
        activity_array = np.array(integer_list)
        df["Physical Activity"] = activity_array
    # physical activity for adults (18-64)
    if 18 < age < 64:
        if 3 < activity_level < 5:
            min = 30
            max = 100
        if 1 < activity_level < 3:
            min = 15
            max = 454
        integer_list = randomize_int(min, max, amount)
        activity_array = np.array(integer_list)
        df["Physical Activity"] = activity_array
    # physical activity for older adults (65 and older)
    if age >= 65:
        if 3 < activity_level < 5:
            min = 30
            max = 70
        if 1 < activity_level < 3:
            min = 10
            max = 30
        integer_list = randomize_int(min, max, amount)
        activity_array = np.array(integer_list)
        df["Physical Activity"] = activity_array


def create_temperature(df, age, amount):
    if "Temperature" not in df.columns:
        df["Temperature"] = ""
    temperature_list = []
    Faker.seed(0)
    if 6 < age < 17:
        for x in range(amount):
            temperature = fake.pydecimal(right_digits=1, positive=True, min_value=97.9, max_value=99.0)
            temperature_list.append(temperature)
    if 18 < age < 64:
        for x in range(amount):
            temperature = fake.pydecimal(right_digits=1, positive=True, min_value=97.0, max_value=99.0)
            temperature_list.append(temperature)
    if age >= 65:
        for x in range(amount):
            temperature = fake.pydecimal(right_digit=1, positive=True, min_value=96.0, max_value=98.6)
            temperature_list.append(temperature)

    temperature_array = np.array(temperature_list)
    df["Temperature"] = temperature_array


def create_blood_pressure(df, age, activity_level, amount):
    """Create blood pressure based on age and activity level."""
    if "Blood Pressure" not in df.columns:
        df["Blood Pressure"] = ""
    # Systolic Blood Pressure
    if 6 < age < 13:
        if 3 < activity_level < 5:
            min = 60
            max = 115
        if 1 < activity_level < 3:
            min = 90
            max = 135
        integer_list = randomize_int(min, max, amount)
        blood_pressure_array = np.array(integer_list)
        df["Blood Pressure"] = blood_pressure_array
    if 14 < age < 18:
        if 3 < activity_level < 5:
            min = 70
            max = 120
        if 1 < activity_level < 3:
            min = 100
            max = 140
        integer_list = randomize_int(min, max, amount)
        blood_pressure_array = np.array(integer_list)
        df["Blood Pressure"] = blood_pressure_array
    if 19 < age < 40:
        if 3 < activity_level < 5:
            min = 75
            max = 135
        if 1 < activity_level < 3:
            min = 95
            max = 155
        integer_list = randomize_int(min, max, amount)
        blood_pressure_array = np.array(integer_list)
        df["Blood Pressure"] = blood_pressure_array
    if 41 < age < 60:
        if 3 < activity_level < 5:
            min = 90
            max = 145
        if 1 < activity_level < 3:
            min = 110
            max = 165
        integer_list = randomize_int(min, max, amount)
        blood_pressure_array = np.array(integer_list)
        df["Blood Pressure"] = blood_pressure_array
    if age >= 61:
        if 3 < activity_level < 5:
            min = 75
            max = 145
        if 1 < activity_level < 3:
            min = 95
            max = 165
        integer_list = randomize_int(min, max, amount)
        blood_pressure_array = np.array(integer_list)
        df["Blood Pressure"] = blood_pressure_array


def create_heart_rate(df, age, activity_level, amount):
    """Create heart rate based on age and activity level."""
    if "Heart Rate" not in df.columns:
        df["Heart Rate"] = ""
    if age <= 20:
        if 3 < activity_level < 5:
            min = 100
            max = 170
        if 1 < activity_level < 3:
            min = 130
            max = 200
        integer_list = randomize_int(min, max, amount)
        heart_array = np.array(integer_list)
        df["Heart Rate"] = heart_array
    if 20 < age < 30:
        if 3 < activity_level < 5:
            min = 100
            max = 162
        if 1 < activity_level < 3:
            min = 130
            max = 205
        integer_list = randomize_int(min, max, amount)
        heart_array = np.array(integer_list)
        df["Heart Rate"] = heart_array
    if 30 < age < 40:
        if 3 < activity_level < 5:
            min = 95
            max = 153
        if 1 < activity_level < 3:
            min = 125
            max = 190
        integer_list = randomize_int(min, max, amount)
        heart_array = np.array(integer_list)
        df["Heart Rate"] = heart_array
    if 40 < age < 50:
        if 3 < activity_level < 5:
            min = 90
            max = 145
        if 1 < activity_level < 3:
            min = 120
            max = 185
        integer_list = randomize_int(min, max, amount)
        heart_array = np.array(integer_list)
        df["Heart Rate"] = heart_array
    if 50 < age < 60:
        if 3 < activity_level < 5:
            min = 85
            max = 136
        if 1 < activity_level < 3:
            min = 115
            max = 175
        integer_list = randomize_int(min, max, amount)
        heart_array = np.array(integer_list)
        df["Heart Rate"] = heart_array
    if 60 < age < 70:
        if 3 < activity_level < 5:
            min = 80
            max = 128
        if 1 < activity_level < 3:
            min = 110
            max = 165
        integer_list = randomize_int(min, max, amount)
        heart_array = np.array(integer_list)
        df["Heart Rate"] = heart_array
    if age >= 70:
        if 3 < activity_level < 5:
            min = 75
            max = 128
        if 1 < activity_level < 3:
            min = 105
            max = 160
        integer_list = randomize_int(min, max, amount)
        heart_array = np.array(integer_list)
        df["Heart Rate"] = heart_array


def create_steps(df, activity_level, amount):
    """Create steps based on activity level."""
    if "Daily Steps" not in df.columns:
        df["Daily Steps"] = ""
    # age, activity_level = get_individual_information()
    # Steps for sedentary lifestyle
    if activity_level == 1:
        min = 0
        max = 5000
        integer_list = randomize_int(min, max, amount)
        steps_array = np.array(integer_list)
        df["Daily Steps"] = steps_array
    # Steps for low activity lifestyle
    if activity_level == 2:
        min = 5000
        max = 7499
        integer_list = randomize_int(min, max, amount)
        steps_array = np.array(integer_list)
        df["Daily Steps"] = steps_array
    # Steps for somewhat active lifestyle
    if activity_level == 3:
        min = 7500
        max = 9999
        integer_list = randomize_int(min, max, amount)
        steps_array = np.array(integer_list)
        df["Daily Steps"] = steps_array
    # Steps for active lifestyle
    if activity_level == 4:
        min = 10000
        max = 12500
        integer_list = randomize_int(min, max, amount)
        steps_array = np.array(integer_list)
        df["Daily Steps"] = steps_array
    # Steps for highly active lifestyle
    if activity_level == 5:
        min = 12500
        max = 35000
        integer_list = randomize_int(min, max, amount)
        steps_array = np.array(integer_list)
        df["Daily Steps"] = steps_array


# def remove_unwanted_data(df, name):
#     df.drop(columns='name', axis=1)


def remove_empty_columns(df):
    df.dropna(axis='columns', inplace=True)


if __name__ == "__main__":
    data = pd.read_csv("/home/maddykapfhammer/Documents/Allegheny/MozillaFellows/predictiveWellness/vigor/dataFiles/selectedData.csv")
    amount = 10
    age = 20
    activity_level = 2
    data.to_csv("/home/maddykapfhammer/Documents/Allegheny/MozillaFellows/predictiveWellness/vigor/dataFiles/selectedData.csv")
    # print(data)
