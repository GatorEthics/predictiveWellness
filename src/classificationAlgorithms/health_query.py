"""A program to query PubMed with keywords from classification."""
import decision_tree as dt
import naive_bayes as nb
import support_vector_machine as svm
from pymed import PubMed

svm_health = svm.perform_methods()
gini_health, entropy_health = dt.perform_methods()
naive_health = nb.perform_methods()


database = PubMed(tool="PredictiveWellness", email="kapfhammerm@allegheny.edu")
query = gini_health
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
