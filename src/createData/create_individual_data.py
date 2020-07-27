"""A program to create fake data for an individual using Faker Python Package."""

from faker import Faker
from faker.providers import python
import pandas as pd
import numpy as np

fake = Faker()
fake.add_provider(python)


    # df.drop(df.index, inplace=True)


def randomize_int(min, max, increments, amount):
    """Create a list of random numbers, based on specific parameters."""
    integer_list = []
    Faker.seed(0)
    for x in range(amount):
        integer = fake.pyint(min_value=min, max_value=max, step=increments)
        integer_list.append(integer)
    return integer_list


def create_steps(df):
    # df.Steps = df.Steps.astype(str)
    min = 0
    max = 26500
    increments = 1
    amount = 1000
    integer_list = randomize_int(min, max, increments, amount)
    steps_array = np.array(integer_list)
    df["Steps_taken"] = steps_array


def create_minutes_sitting(df):
    min = 400
    max = 1450
    increments = 1
    amount = 1000
    integer_list = randomize_int(min, max, increments, amount)
    sitting_array = np.array(integer_list)
    df["Minutes_sitting"] = sitting_array


def create_moderate_activity():
    min = 0
    max = 100
    increments = 1
    amount = 1000
    moderate_list = randomize_int(min, max, increments, amount)
    return moderate_list


def create_intense_activity():
    min = 0
    max = 150
    increments = 1
    amount = 1000
    intense_list = randomize_int(min, max, increments, amount)
    return intense_list


def create_activity_minutes(df):
    activity_list = []
    moderate_activity_list = create_moderate_activity()
    intense_activity_list = create_intense_activity()
    for i in range(0, len(moderate_activity_list)):
        activity_list.append(moderate_activity_list[i] + intense_activity_list[i])
    activity_array = np.array(activity_list)
    df["Minutes_physical_activity"] = activity_array


def create_heart_rate(df):
    min = 50
    max = 110
    increments = 1
    amount = 1000
    integer_list = randomize_int(min, max, increments, amount)
    heart_rate_array = np.array(integer_list)
    df["HR"] = heart_rate_array


def create_blood_pressure(df):
    min = 110
    max = 145
    increments = 1
    amount = 1000
    integer_list = randomize_int(min, max, increments, amount)
    blood_pressure_array = np.array(integer_list)
    df["BP"] = blood_pressure_array


def main():
    individual_data = pd.read_csv("/home/maddykapfhammer/Documents/Allegheny/MozillaFellows/predictiveWellness/src/dataFiles/individual_data.csv")
    # , index_col=[0]
    # clear_existing_data(individual_data)
    create_steps(individual_data)
    create_minutes_sitting(individual_data)
    create_activity_minutes(individual_data)
    create_heart_rate(individual_data)
    create_blood_pressure(individual_data)
    individual_data.to_csv("/home/maddykapfhammer/Documents/Allegheny/MozillaFellows/predictiveWellness/src/dataFiles/individual_data.csv")


if __name__ == "__main__":
    main()
