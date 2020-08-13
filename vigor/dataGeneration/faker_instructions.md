# Using Faker

Faker is a Python package developed to generate fake data of many different types. It is useful in scenarios and projects that require a lot of data for training, or analysis. In the case of this tool, it is used to create accurate health data to be used for artificial intelligence training and classification.

For a full description of this package please visit Faker's [documentation](https://faker.readthedocs.io/en/master/) and Faker's [GitHub page](https://github.com/joke2k/faker)

## Understanding Faker's Providers

Faker has multiple different properties for data generation, such as names, addresses and numerical values. These range from fairly simple to fairly complex. There are [Standard Providers](https://faker.readthedocs.io/en/master/providers.html), [Community Providers](https://faker.readthedocs.io/en/master/communityproviders.html), and [Localized Providers](https://faker.readthedocs.io/en/master/locales.html) all which have documented functions on Faker's documentation. If Faker does not have a provider which would generate the data you need, a programmer can start with a basic provider, and create guidelines for a new and customized provider.

## Steps for Use

- In order to install Faker use the command `pip install Faker` in your terminal window

- Faker should also be added to your dependencies in your `Pipfile`

```
[Packages]
faker = "*"
```

This package dependency can be installed using the command `pipenv install --dev`

- At the beginning of your program, Faker must be included with your import statements
`from faker import Faker`

- Additionally, the provider which you are interested in using for data generation also must be imported at the beginning of your program
`from faker.providers import name_of_provider`

![Using Faker](faker1smaller.mp4)

- Depending on the provider, there are different functions, which allow random generation of data. Some functions require numberical boundaries, and all functions require the amount of random data which should be generated.

## Writing to CSV Files

It is easiest to store the generated fake information in a list. This list should then be converted to an array and assigned to the specific column in your data file.

![Writing to .cvs files](faker2.mp4)

## Helpful Tutorials

- For an overview of simple Faker usage and multiple providers including names, jobs, local data, currencies, words, profiles, numbers and more visit [zetcode.com/python/faker/](zetcode.come/python/faker/)

- For an overview of incoorporating Faker into testing visit [https://semaphoreci.com/community/tutorials/generating-fake-data-for-python-unit-tests-with-faker](https://semaphoreci.com/community/tutorials/generating-fake-data-for-python-unit-tests-with-faker) and [https://kishstats.com/python/2018/04/04/faker-demo-python.html](https://kishstats.com/python/2018/04/04/faker-demo-python.html)

- For an overview of anonymizing CSV data, generating fake data, and **creating a provider** visit [https://medium.com/district-data-labs/a-practical-guide-to-anonymizing-datasets-with-python-faker-ecf15114c9be](https://medium.com/district-data-labs/a-practical-guide-to-anonymizing-datasets-with-python-faker-ecf15114c9be)
