"""A program to depict using Faker for data generation."""

# import necessary packages 
import pandas as pd 
import numpy as np

# import Faker and providers
from faker import Faker
from faker.providers import python
from faker.providers import date_time

# initalize faker
fake = Faker()
fake.add_provider(python)
fake.add_provider(date_time)
Faker.seed(0)

# Declare csv file and convert to pandas dataframe
data = pd.read_csv("/home/maddykapfhammer/Documents/Allegheny/MozillaFellows/predictiveWellness/vigor/dataGeneration/faker.csv")

# create integer list and put in dataframe
integer_list = []
for x in range(10):
    integer = fake.pyint(min_value=1, max_value=100)
    integer_list.append(integer)
integer_array = np.array(integer_list)
data["Integers"] = integer_array

# create date list and put in dataframe
date_list = []
for x in range(10):
    date = fake.date_between()
    date_list.append(date)
date_array = np.array(date_list)
data["Dates"] = date_array

# Convert pandas dataframe back to .csv file
data.to_csv("/home/maddykapfhammer/Documents/Allegheny/MozillaFellows/predictiveWellness/vigor/dataGeneration/faker.csv")

