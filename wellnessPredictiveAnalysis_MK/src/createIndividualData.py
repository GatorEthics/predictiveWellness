"""A program to create fake data for an individual using Faker Python Plugin."""

from faker import Faker
from faker.providers import python
import pandas as pd
import numpy as np

fake = Faker()
fake.add_provider(python)


def randomize_int(min, max, increments):
    """Create a list of random numbers, based on specific parameters."""
    integer_list = []
    Faker.seed(0)
    for x in range(366):
        integer = fake.pyint(min_value=min, max_value=max, step=increments)
        integer_list.append(integer)
    return integer_list


def create_heart_rate(df):
    min = 50
    max = 110
    increments = 1
    integer_list = randomize_int(min, max, increments)
    heart_rate_array = np.array(integer_list)
    df["HR"] = heart_rate_array


def create_blood_pressure(df):
    min = 110
    max = 145
    increments = 1
    integer_list = randomize_int(min, max, increments)
    blood_pressure_array = np.array(integer_list)
    df["BP"] = blood_pressure_array


if __name__ == "__main__":
    fitbit_data = pd.read_csv("datasetAccess/FitBitData.csv")
    randomize_int(10, 100, 1)
    create_heart_rate(fitbit_data)
    create_blood_pressure(fitbit_data)
    fitbit_data.to_csv("FitBitData.csv")
