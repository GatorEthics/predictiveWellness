"""A program to query PubMed with keywords from classification."""
import decision_tree as dt
import naive_bayes as nb
import support_vector_machine as svm
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
    database = PubMed(tool="PredictiveWellness", email="kapfhammerm@allegheny.edu")
    query = keywords
    database_results = database.query(query, max_results=2)

    for article in database_results:
        article_id = article.pubmed_id
        title = article.title
        date = article.publication_date
        abstract = article.abstract
        # if article.keywords:
        #     if None in article.keywords:
        #         article.keywords.remove(None)
        #     keywords = '", "'.join(article.keywords)
        print(f"{article_id} - {date} - {title}\n{abstract}\n")
