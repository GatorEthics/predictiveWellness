"""A program to create training and testing data for health, based on age and activity level."""
import numpy as np
import pandas as pd
from faker import Faker
from faker.providers import python

fake = Faker()
fake.add_provider(python)


def clear_existing_data(df):
    """Create a clear dataframe for data generation."""
    df.drop(df.index, inplace=True)


def randomize_int(min, max, increments, amount):
    """Create a list of random numbers, based on specific parameters."""
    integer_list = []
    Faker.seed(0)
    for x in range(amount):
        integer = fake.pyint(min_value=min, max_value=max, step=increments)
        integer_list.append(integer)
    return integer_list


def create_steps(df, activity_level):
    """Create steps based on activity level."""
    # age, activity_level = get_individual_information()
    # Steps for sedentary lifestyle
    if activity_level == 1:
        min = 0
        max = 5000
        increments = 1
        amount = 1000
        integer_list = randomize_int(min, max, increments, amount)
        steps_array = np.array(integer_list)
        df["Steps_taken"] = steps_array
    # Steps for low activity lifestyle
    if activity_level == 2:
        min = 5000
        max = 7499
        increments = 1
        amount = 1000
        integer_list = randomize_int(min, max, increments, amount)
        steps_array = np.array(integer_list)
        df["Steps_taken"] = steps_array
    # Steps for somewhat active lifestyle
    if activity_level == 3:
        min = 7500
        max = 9999
        increments = 1
        amount = 1000
        integer_list = randomize_int(min, max, increments, amount)
        steps_array = np.array(integer_list)
        df["Steps_taken"] = steps_array
    # Steps for active lifestyle
    if activity_level == 4:
        min = 10000
        max = 12500
        increments = 1
        amount = 1000
        integer_list = randomize_int(min, max, increments, amount)
        steps_array = np.array(integer_list)
        df["Steps_taken"] = steps_array
    # Steps for highly active lifestyle
    if activity_level == 5:
        min = 12500
        max = 35000
        increments = 1
        amount = 1000
        integer_list = randomize_int(min, max, increments, amount)
        steps_array = np.array(integer_list)
        df["Steps_taken"] = steps_array


def create_minutes_sitting(df, activity_level):
    """Create minutes sitting based on activity level."""
    # age, activity_level = get_individual_information()
    # Minutes sitting for sedentary lifestyle
    if activity_level == 1:
        min = 660
        max = 1000
        increments = 1
        amount = 1000
        integer_list = randomize_int(min, max, increments, amount)
        sitting_array = np.array(integer_list)
        df["Minutes_sitting"] = sitting_array
    # Steps for low activity lifestyle
    if activity_level == 2:
        min = 480
        max = 660
        increments = 1
        amount = 1000
        integer_list = randomize_int(min, max, increments, amount)
        sitting_array = np.array(integer_list)
        df["Minutes_sitting"] = sitting_array
    # Steps for somewhat active lifestyle
    if activity_level == 3:
        min = 240
        max = 480
        increments = 1
        amount = 1000
        integer_list = randomize_int(min, max, increments, amount)
        sitting_array = np.array(integer_list)
        df["Minutes_sitting"] = sitting_array
    # Steps for active lifestyle
    if activity_level == 4:
        min = 100
        max = 240
        increments = 1
        amount = 1000
        integer_list = randomize_int(min, max, increments, amount)
        sitting_array = np.array(integer_list)
        df["Minutes_sitting"] = sitting_array
    # Steps for highly active lifestyle
    if activity_level == 5:
        min = 0
        max = 240
        increments = 1
        amount = 1000
        integer_list = randomize_int(min, max, increments, amount)
        sitting_array = np.array(integer_list)
        df["Minutes_sitting"] = sitting_array


def create_activity_minutes(df, age, activity_level):
    """Create physical activity based on age and activity."""
    # age, activity_level = get_individual_information()
    # physical activity for school-aged children and adolescents (6-17)
    if 6 < age < 17:
        if 3 < activity_level < 5:
            min = 50
            max = 100
        if 1 < activity_level < 3:
            min = 30
            max = 60
        increments = 1
        amount = 1000
        integer_list = randomize_int(min, max, increments, amount)
        activity_array = np.array(integer_list)
        df["Minutes_physical_activity"] = activity_array
    # physical activity for adults (18-64)
    if 18 < age < 64:
        if 3 < activity_level < 5:
            min = 30
            max = 100
        if 1 < activity_level < 3:
            min = 15
            max = 454
        increments = 1
        amount = 1000
        integer_list = randomize_int(min, max, increments, amount)
        activity_array = np.array(integer_list)
        df["Minutes_physical_activity"] = activity_array
    # physical activity for older adults (65 and older)
    if age < 65:
        if 3 < activity_level < 5:
            min = 30
            max = 70
        if 1 < activity_level < 3:
            min = 10
            max = 30
        increments = 1
        amount = 1000
        integer_list = randomize_int(min, max, increments, amount)
        activity_array = np.array(integer_list)
        df["Minutes_physical_activity"] = activity_array


def create_heart_rate(df, age, activity_level):
    """Create heart rate based on age and activity level."""
    if age <= 20:
        if 3 < activity_level < 5:
            min = 100
            max = 170
        if 1 < activity_level < 3:
            min = 130
            max = 200
        increments = 1
        amount = 1000
        integer_list = randomize_int(min, max, increments, amount)
        heart_array = np.array(integer_list)
        df["HR"] = heart_array
    if 20 < age < 30:
        if 3 < activity_level < 5:
            min = 100
            max = 162
        if 1 < activity_level < 3:
            min = 130
            max = 205
        increments = 1
        amount = 1000
        integer_list = randomize_int(min, max, increments, amount)
        heart_array = np.array(integer_list)
        df["HR"] = heart_array
    if 30 < age < 40:
        if 3 < activity_level < 5:
            min = 95
            max = 153
        if 1 < activity_level < 3:
            min = 125
            max = 190
        increments = 1
        amount = 1000
        integer_list = randomize_int(min, max, increments, amount)
        heart_array = np.array(integer_list)
        df["HR"] = heart_array
    if 40 < age < 50:
        if 3 < activity_level < 5:
            min = 90
            max = 145
        if 1 < activity_level < 3:
            min = 120
            max = 185
        increments = 1
        amount = 1000
        integer_list = randomize_int(min, max, increments, amount)
        heart_array = np.array(integer_list)
        df["HR"] = heart_array
    if 50 < age < 60:
        if 3 < activity_level < 5:
            min = 85
            max = 136
        if 1 < activity_level < 3:
            min = 115
            max = 175
        increments = 1
        amount = 1000
        integer_list = randomize_int(min, max, increments, amount)
        heart_array = np.array(integer_list)
        df["HR"] = heart_array
    if 60 < age < 70:
        if 3 < activity_level < 5:
            min = 80
            max = 128
        if 1 < activity_level < 3:
            min = 110
            max = 165
        increments = 1
        amount = 1000
        integer_list = randomize_int(min, max, increments, amount)
        heart_array = np.array(integer_list)
        df["HR"] = heart_array
    if age >= 70:
        if 3 < activity_level < 5:
            min = 75
            max = 128
        if 1 < activity_level < 3:
            min = 105
            max = 160
        increments = 1
        amount = 1000
        integer_list = randomize_int(min, max, increments, amount)
        heart_array = np.array(integer_list)
        df["HR"] = heart_array


def create_blood_pressure(df, age, activity_level):
    """Create blood pressure based on age and activity level."""
    # Systolic Blood Pressure
    if 6 < age < 13:
        if 3 < activity_level < 5:
            min = 60
            max = 115
        if 1 < activity_level < 3:
            min = 90
            max = 135
        increments = 1
        amount = 1000
        integer_list = randomize_int(min, max, increments, amount)
        blood_pressure_array = np.array(integer_list)
        df["BP"] = blood_pressure_array
    if 14 < age < 18:
        if 3 < activity_level < 5:
            min = 70
            max = 120
        if 1 < activity_level < 3:
            min = 100
            max = 140
        increments = 1
        amount = 1000
        integer_list = randomize_int(min, max, increments, amount)
        blood_pressure_array = np.array(integer_list)
        df["BP"] = blood_pressure_array
    if 19 < age < 40:
        if 3 < activity_level < 5:
            min = 75
            max = 135
        if 1 < activity_level < 3:
            min = 95
            max = 155
        increments = 1
        amount = 1000
        integer_list = randomize_int(min, max, increments, amount)
        blood_pressure_array = np.array(integer_list)
        df["BP"] = blood_pressure_array
    if 41 < age < 60:
        if 3 < activity_level < 5:
            min = 90
            max = 145
        if 1 < activity_level < 3:
            min = 110
            max = 165
        increments = 1
        amount = 1000
        integer_list = randomize_int(min, max, increments, amount)
        blood_pressure_array = np.array(integer_list)
        df["BP"] = blood_pressure_array
    if age >= 61:
        if 3 < activity_level < 5:
            min = 75
            max = 145
        if 1 < activity_level < 3:
            min = 95
            max = 165
        increments = 1
        amount = 1000
        integer_list = randomize_int(min, max, increments, amount)
        blood_pressure_array = np.array(integer_list)
        df["BP"] = blood_pressure_array


def main(age, activity_level):
    """Perform all functions."""
    custom_individual = pd.read_csv(
        "/home/maddykapfhammer/Documents/Allegheny/MozillaFellows/predictiveWellness/src/dataFiles/customIndividual.csv",
        index_col=[0],
    )
    # clear_existing_data(custom_individual)
    create_steps(custom_individual, activity_level)
    create_minutes_sitting(custom_individual, activity_level)
    create_activity_minutes(custom_individual, age, activity_level)
    create_heart_rate(custom_individual, age, activity_level)
    create_blood_pressure(custom_individual, age, activity_level)
    custom_individual.to_csv(
        "/home/maddykapfhammer/Documents/Allegheny/MozillaFellows/predictiveWellness/src/dataFiles/customIndividual.csv"
    )
    return custom_individual


if __name__ == "__main__":
    main(20, 2)
