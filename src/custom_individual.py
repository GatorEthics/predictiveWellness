"""A program to create training and testing data for health, based on age and activity level."""

from faker import Faker
from faker.providers import python
import pandas as pd
import numpy as np

fake = Faker()
fake.add_provider(python)


def reset_dataframe(df):
    df.drop(df.index, inplace=True)


def get_individual_information():
    age = int(input("Please enter your age: "))
    if age < 1 or age > 110:
        print("You entered an invalid age.")
        age = input("Please enter your age: ")
    activity_level = int(input("Please enter your physical activity level on a scale from 1 to 5: "))
    if activity_level > 5 or activity_level < 1:
        print("You entered an invalid activity level.")
        activity_level = input("Please enter your physical activity level on a scale from 1 to 5: ")
    return age, activity_level


def randomize_int(min, max, increments, amount):
    """Create a list of random numbers, based on specific parameters."""
    integer_list = []
    Faker.seed(0)
    for x in range(amount):
        integer = fake.pyint(min_value=min, max_value=max, step=increments)
        integer_list.append(integer)
    return integer_list


def create_steps(df, activity_level):
    # age, activity_level = get_individual_information()
    # Steps for sedentary lifestyle
    if activity_level == 1:
        min = 0
        max = 5000
        increments = 1
        amount = 1000
        integer_list = randomize_int(min, max, increments, amount)
        steps_array = np.array(integer_list)
        df["Steps"] = steps_array
    # Steps for low activity lifestyle
    if activity_level == 2:
        min = 5000
        max = 7499
        increments = 1
        amount = 1000
        integer_list = randomize_int(min, max, increments, amount)
        steps_array = np.array(integer_list)
        df["Steps"] = steps_array
    # Steps for somewhat active lifestyle
    if activity_level == 3:
        min = 7500
        max = 9999
        increments = 1
        amount = 1000
        integer_list = randomize_int(min, max, increments, amount)
        steps_array = np.array(integer_list)
        df["Steps"] = steps_array
    # Steps for active lifestyle
    if activity_level == 4:
        min = 10000
        max = 12500
        increments = 1
        amount = 1000
        integer_list = randomize_int(min, max, increments, amount)
        steps_array = np.array(integer_list)
        df["Steps"] = steps_array
    # Steps for highly active lifestyle
    if activity_level == 5:
        min = 12500
        max = 35000
        increments = 1
        amount = 1000
        integer_list = randomize_int(min, max, increments, amount)
        steps_array = np.array(integer_list)
        df["Steps"] = steps_array


def create_minutes_sitting(df, activity_level):
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
            max = 45
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


# def create_heart_rate(df):


# def create_blood_pressure(df):

def main(age, activity_level):
    custom_individual = pd.read_csv("/home/maddykapfhammer/Documents/Allegheny/MozillaFellows/predictiveWellness/src/createData/customIndividual.csv", index_col=[0])
    reset_dataframe(custom_individual)
    create_steps(custom_individual, activity_level)
    create_minutes_sitting(custom_individual, activity_level)
    create_activity_minutes(custom_individual, age, activity_level)
    custom_individual.to_csv("/home/maddykapfhammer/Documents/Allegheny/MozillaFellows/predictiveWellness/src/createData/customIndividual.csv")
    return custom_individual

if __name__ == "__main__":
    main(20, 2)
