"""A program to create fake data for an individual using Faker Python Plugin."""

from faker import Faker
from faker.providers import python

fake = Faker()
fake.add_provider(python)


def randomize_int(min, max, increments):
    Faker.seed(0)
    for x in range(5):
        integer = fake.pyint(min_value=min, max_value=max, step=increments)
        return integer


def create_heart_rate(min, max, increments):
    randomize_int(min, max, increments)


if __name__ == "__main__":
    randomize_int(10, 100, 1)

# fake = Faker()
# fake.add_provider(python)

# Faker.seed(0)
# for x in range(5):
#     print(fake.pyint(min_value=0, max_value=100, step=1))
