"""A program to query PubMed with keywords from classification."""
import decision_tree as dt
import naive_bayes as nb
import support_vector_machine as svm
import pandas as pd
import numpy as np
from pymed import PubMed


def drop_data(dataframe):
    dataframe = dataframe.iloc[0:0]
    return dataframe


def define_query(classification, data_type):
    query = 0
    if classification == 1:
        query = nb.perform_methods(data_type)
    if classification == 2:
        gini_health, entropy_health = dt.perform_methods(data_type)
        query = gini_health
    if classification == 3:
        gini_health, entropy_health = dt.perform_methods(data_type)
        query = entropy_health
    if classification == 4:
        query = svm.perform_methods(data_type)
    return query


def perform_query(keywords, amount):
    database = PubMed(tool="Vigor", email="kapfhammerm@allegheny.edu")
    query = keywords
    database_results = database.query(query, max_results=amount)
    return database_results


def gather_results(database_results):
    title = ""
    date = ""
    author = ""
    abstract = ""
    titles = []
    identification = []
    date_published = []
    authors = []
    abstracts = []
    for article in database_results:
        article_id = article.pubmed_id
        title = article.title
        date = article.publication_date
        author = article.authors
        abstract = article.abstract
        titles.append(title)
        identification.append(article_id)
        date_published.append(date)
        authors.append(author)
        abstracts.append(abstract)

    return titles, identification, date_published, authors, abstract


def determine_keywords(database_results):
    keywords_list = []
    for article in database_results:
        if article.keywords:
            if article.keywords:
                if None in article.keywords:
                    article.keywords.remove(None)
                keywords = '", "'.join(article.keywords)
                keywords_list.append(keywords)
    return keywords_list


def convert_to_file(title, id, date, authors, abstract):
    pubmed_file = pd.read_csv(
        "/home/maddykapfhammer/Documents/Allegheny/MozillaFellows/predictiveWellness/vigor/dataFiles/PubMedArticles.csv"
    )
    title_array = np.array(title)
    id_array = np.array(id)
    date_array = np.array(date)
    # author_array = np.array(authors)
    abstract_array = np.array(abstract)
    # keywords_array = np.array(keywords)
    pubmed_file["Titles"] = title_array
    pubmed_file["ID Number"] = id_array
    pubmed_file["Date Published"] = date_array
    # file["Authors"] = author_array
    pubmed_file["Abstract"] = abstract_array
    # file["Keywords"] = keywords_array

    pubmed_file.to_csv(
        "/home/maddykapfhammer/Documents/Allegheny/MozillaFellows/predictiveWellness/vigor/dataFiles/PubMedArticles.csv"
    )

    return pubmed_file
    #     steps_array = np.array(integer_list)
    # df["Steps_taken"] = steps_array
    # file[title]


def perform_methods(classification, data_type, amount):
    # dataframe = drop_data()
    keywords = define_query(classification, data_type)
    results = perform_query(classification, amount)
    title, id, date, authors, abstract = gather_results(results)
    # keywords = determine_keywords(results)
    data_file = convert_to_file(title, id, date, authors, abstract)
    return data_file


if __name__ == "__main__":
    perform_methods("Naive Bayes Classification", "Customized")
