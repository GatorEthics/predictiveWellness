"""A program to determine health risks with fitness data."""

import pandas as pd
from pymed import PubMed


def label_cardiovascular_disease(df):
    df.CD = df.CD.astype(str)
    for i, j in df.iterrows():
        physical_activity = (
            j["Minutes_moderate_activity"] + j["Minutes_intense_activity"]
        )
        hours_sitting = j["Minutes_sitting"] / 60
        if physical_activity < 30 and hours_sitting > 8:
            df.at[i, "CD"] = "Cardiovascular disease"


def label_metabolic_syndrome(df):
    df.MS = df.MS.astype(str)
    for i, j in df.iterrows():
        hours_sitting = j["Minutes_sitting"] / 60
        if j["Steps"] < 7500 and hours_sitting > 8:
            df.at[i, "MS"] = "Metabolic syndrome"


def label_diabetes(df):
    df.Diabetes = df.Diabetes.astype(str)
    for i, j in df.iterrows():
        physical_activity = (
            j["Minutes_moderate_activity"] + j["Minutes_intense_activity"]
        )
        if physical_activity < 30 and j["Steps"] < 7500:
            df.at[i, "Diabetes"] = "Type II Diabetes"


def label_health_risks(df):
    df.Health = df.Health.astype(str)
    health = " "
    for i, j in df.iterrows():
        if j["CD"] != "nan":
            health = health + "Cardiovascular Disease, "
        if j["MS"] != "nan":
            health = health + "Metabolic Syndrome, "
        if j["Diabetes"] != "nan":
            health = health + "Type II Diabetes "
        if j["CD"] == "nan" and j["MS"] == "nan" and j["Diabetes"] == "nan":
            health = "Good health"
        df.at[i, "Health"] = health
        health = ""
        # print(health)


if __name__ == "__main__":
    fitbit_data = pd.read_csv("datasetAccess/FitBitData.csv")
    label_cardiovascular_disease(fitbit_data)
    label_metabolic_syndrome(fitbit_data)
    label_diabetes(fitbit_data)
    # label_good_health(fitbit_data)
    # label_moderate_health(fitbit_data)
    label_health_risks(fitbit_data)
    fitbit_data.to_csv("updated_data.csv")
