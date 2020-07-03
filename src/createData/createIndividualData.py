"""A program to create fake data for an individual using Faker Python Plugin."""

from faker import Faker
from faker.providers import python
import pandas as pd
import numpy as np

fake = Faker()
fake.add_provider(python)


def randomize_int(min, max, increments, amount):
    """Create a list of random numbers, based on specific parameters."""
    integer_list = []
    Faker.seed(0)
    for x in range(amount):
        integer = fake.pyint(min_value=min, max_value=max, step=increments)
        integer_list.append(integer)
    return integer_list


def create_heart_rate(df2):
    min = 50
    max = 110
    increments = 1
    amount = 1000
    integer_list = randomize_int(min, max, increments, amount)
    heart_rate_array = np.array(integer_list)
    df2["HR"] = heart_rate_array


def create_blood_pressure(df2):
    min = 110
    max = 145
    increments = 1
    amount = 1000
    integer_list = randomize_int(min, max, increments, amount)
    blood_pressure_array = np.array(integer_list)
    df2["BP"] = blood_pressure_array


def create_more_steps(df2):
    min = 0
    max = 26500
    increments = 1
    amount = 636
    integer_list = randomize_int(min, max, increments, amount)
    steps_array = np.array(integer_list)
    df2["Steps"] = steps_array


def create_minutes_sitting(df2):
    min = 400
    max = 1450
    increments = 1
    amount = 636
    integer_list = randomize_int(min, max, increments, amount)
    sitting_array = np.array(integer_list)
    df2["Minutes_sitting"] = sitting_array


def create_moderate_activity(df2):
    min = 0
    max = 100
    increments = 1
    amount = 636
    integer_list = randomize_int(min, max, increments, amount)
    moderate_array = np.array(integer_list)
    df2["Minutes_moderate_activity"] = moderate_array


def create_intense_activity(df2):
    min = 0
    max = 150
    increments = 1
    amount = 636
    integer_list = randomize_int(min, max, increments, amount)
    intense_array = np.array(integer_list)
    df2["Minutes_intense_activity"] = intense_array


def combine_data(df1, df2):
    frames = [df1, df2]
    result = pd.concat(frames)
    return result


if __name__ == "__main__":
    fitbit_data = pd.read_csv("datasetAccess/FitBitData.csv")
    fitbit_data2 = pd.read_csv("datasetAccess/FitBitData2.csv")
    create_more_steps(fitbit_data2)
    create_minutes_sitting(fitbit_data2)
    create_moderate_activity(fitbit_data2)
    create_intense_activity(fitbit_data2)
    create_heart_rate(fitbit_data2)
    create_blood_pressure(fitbit_data2)
    individual_data = combine_data(fitbit_data, fitbit_data2)
    individual_data.to_csv("individual_data.csv")
