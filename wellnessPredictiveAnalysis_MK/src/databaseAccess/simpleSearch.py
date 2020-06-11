"""A simple program to query from PubMed Database."""
# PubMed query builder: https://github.com/gijswobben/pymed/tree/master/examples/advanced_search

from pymed import PubMed

database = PubMed(tool="PredictiveWellness", email="kapfhammerm@allegheny.edu")
query = "diabetes"
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
