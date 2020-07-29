"""A program to query PubMed with keywords from classification."""
import decision_tree as dt
import naive_bayes as nb
import support_vector_machine as svm
import pandas as pd
import numpy as np
from pymed import PubMed


def define_query(classification):
    if classification == "Naive Bayes Classification":
        query = nb.perform_methods()
    if classification == "Gini Decision Tree Classification":
        gini_health, entropy_health = dt.perform_methods()
        query = gini_health
    if classification == "Entropy Decision Tree Classification":
        gini_health, entropy_health = dt.perform_methods()
        query = entropy_health
    if classification == "Support Vector Machine Classification":
        query = svm.perform_methods()
    return query


def perform_query(keywords, amount):
    database = PubMed(tool="Vigor", email="kapfhammerm@allegheny.edu")
    query = keywords
    database_results = database.query(query, max_results=amount)
    return database_results


def gather_results(database_results):
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
    file = pd.read_csv(
        "/home/maddykapfhammer/Documents/Allegheny/MozillaFellows/predictiveWellness/src/dataFiles/PubMedArticles.csv"
    )
    title_array = np.array(title)
    id_array = np.array(id)
    date_array = np.array(date)
    # author_array = np.array(authors)
    abstract_array = np.array(abstract)
    # keywords_array = np.array(keywords)
    file["Titles"] = title_array
    file["ID Number"] = id_array
    file["Date Published"] = date_array
    # file["Authors"] = author_array
    file["Abstract"] = abstract_array
    # file["Keywords"] = keywords_array

    file.to_csv(
        "/home/maddykapfhammer/Documents/Allegheny/MozillaFellows/predictiveWellness/src/dataFiles/PubMedArticles.csv"
    )
    #     steps_array = np.array(integer_list)
    # df["Steps_taken"] = steps_array
    # file[title]


if __name__ == "__main__":
    keywords = define_query("Gini Decision Tree Classification")
    results = perform_query(keywords, 3)
    title, id, date, authors, abstract = gather_results(results)
    # keywords = determine_keywords(results)
    convert_to_file(title, id, date, authors, abstract)
