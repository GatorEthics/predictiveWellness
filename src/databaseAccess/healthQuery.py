"""A program to query PubMed with keywords from classification."""

# import classificationAlgorithms.SupportVectorMachine as svm
import classificationAlgorithms.DecisionTree as decision_tree
import classificationAlgorithms.SupportVectorMachine as svm
import classificationAlgorithms.NaiveBayes as bayes
from pymed import PubMed

matrix, report, health_results = svm.perform_methods()


database = PubMed(tool="PredictiveWellness", email="kapfhammerm@allegheny.edu")
query = health_results
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