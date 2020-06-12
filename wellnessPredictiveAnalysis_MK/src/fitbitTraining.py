"""A program to create training data based on medical literature."""

import pandas as pd
from pymed import PubMed


def label_steps(dataframe):
    """Label the data according to daily steps."""
    dataframe.Step_labels = dataframe.Step_labels.astype(str)
    for i, j in dataframe.iterrows():
        if j["Steps"] <= 7500:
            dataframe.at[i, "Step_labels"] = "Low physical activity"
        if 7500 < j["Steps"] < 1000:
            dataframe.at[i, "Step_labels"] = "Moderate physical activity"
        if j["Steps"] > 1000:
            dataframe.at[i, "Step_labels"] = "High physical activity"


def label_minutes_sitting(dataframe):
    """Label the data according to total minutes sitting daily."""
    dataframe.Sitting_labels = dataframe.Sitting_labels.astype(str)
    for i, j in dataframe.iterrows():
        hours_sitting = j["Minutes_sitting"] / 60
        if hours_sitting <= 4:
            dataframe.at[i, "Sitting_labels"] = "Low risk metabolic syndrome"
        if 4 < hours_sitting < 8:
            dataframe.at[i, "Sitting_labels"] = "Moderate risk metabolic syndrome"
        if 8 < hours_sitting < 11:
            dataframe.at[i, "Sitting_labels"] = "High risk metablolic syndrome"
        if hours_sitting >= 11:
            dataframe.at[i, "Sitting_labels"] = "Very high risk metabolic syndrome"

        # if dataframe.at[i, "Sitting_labels"] == "nan":
        #     print("Sitting label incorrect: ")
        #     print(dataframe.at[i, "Minutes_sitting"])
        # print(j["Sitting_labels"])


def label_physical_activity(dataframe):
    """Label data according to daily physical activity."""
    dataframe.Activity_labels = dataframe.Activity_labels.astype(str)
    for i, j in dataframe.iterrows():
        physical_activity = (
            j["Minutes_moderate_activity"] + j["Minutes_intense_activity"]
        )
        if physical_activity <= 15:
            dataframe.at[i, "Activity_labels"] = "High risk of cardiovascular disease"
        if 15 < physical_activity < 30:
            dataframe.at[i, "Activity_labels"] = "Moderate risk of cardiovascular disease"
        if physical_activity >= 30:
            dataframe.at[i, "Activity_labels"] = "Low risk of cardiovascular disease"


def combine_labels(dataframe):
    dataframe.Labels = dataframe.Labels.astype(str)
    for i, j in dataframe.iterrows():
        # print(j["Step_labels"])
        dataframe.at[i, "Labels"] = j["Step_labels"] + ", " + j["Sitting_labels"] + ", " + j["Activity_labels"]


def create_query(fitbit_df, article_df):
    article_df.Query = article_df.Query.astype(str)
    for i, j in fitbit_df.iterrows():
        article_df.at[i, "Query"] = j["Step_labels"] + " AND " + j["Sitting_labels"] + " AND " + j["Activity_labels"]
    
    # print(dataframe["Query"])


def access_database(fitbit_df, article_df):
    database = PubMed(tool="PredictiveWellness", email="kapfhammerm@allegheny.edu")

    for i, j in article_df.iterrows():
        print(j["Query"])
        query = j + 1["Query"]
        print(query)
        # database_results = database.query(query, max_results=2)
        # article_df.at[i, "Results"] = database_results
    #     print(database_results)
        # for article in database_results:
        #     article_id = article.pubmed_id
        #     title = article.title
        #     date = article.publication_date
        # article_df.at[i, "ArticleID"] = article_id
            # print(title, date)
        #     # abstract = article.abstract
        #     for i, j in article_df:
        #         # article_df.at[i, "ArticleID"] = article_id
        #         article_df.at[i, "Date_published"] = date
        #         article_df.at[i, "Article_title"] = title


#             # if article.keywords:
#             #     if None in article.keywords:
#             #         article.keywords.remove(None)
#             #     keywords = '", "'.join(article.keywords)
#             # print(f"{article_id} - {date} - {title}\n{abstract}\n")


if __name__ == "__main__":
    fitbit_data = pd.read_csv("datasetAccess/FitBitData.csv")
    articles = pd.read_csv("datasetAccess/pubMedArticles.csv")
    label_steps(fitbit_data)
    label_minutes_sitting(fitbit_data)
    label_physical_activity(fitbit_data)
    combine_labels(fitbit_data)
    create_query(fitbit_data, articles)
    articles.to_csv("updated_data.csv")
    # print(fitbit_data["Query"])
    access_database(fitbit_data, articles)

