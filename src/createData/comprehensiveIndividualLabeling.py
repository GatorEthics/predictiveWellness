"""A program to determine health risks with fitness data."""

import pandas as pd
import numpy as np
from pymed import PubMed


def label_cardiovascular_disease(df):
    """Label cardiovascular disease risk based on physical activity and hours sitting."""
    df.CD = df.CD.astype(str)
    for i, j in df.iterrows():
        hours_sitting = j["Minutes_sitting"] / 60
        if j["Minutes_physical_activity"] < 30 and hours_sitting > 8:
            df.at[i, "CD"] = "Cardiovascular disease"

            # and j["BP"] >= 130 and j["HR"] >= 80


def add_columns(df):
    df["CD"] = ""
    df["MS"] = ""
    df["Diabetes"] = ""
    df["Health"] = ""


def label_metabolic_syndrome(df):
    """Label metabolic syndrome risk based on hours sitting and daily steps."""
    df.MS = df.MS.astype(str)
    for i, j in df.iterrows():
        hours_sitting = j["Minutes_sitting"] / 60
        if j["Steps"] < 7500 and hours_sitting > 8:
            df.at[i, "MS"] = "Metabolic syndrome"
            # and j["BP"] >= 130


def label_diabetes(df):
    """Label type II diabetes risk based on physical activity and daily steps."""
    df.Diabetes = df.Diabetes.astype(str)
    for i, j in df.iterrows():
        if j["Minutes_physical_activity"] < 30 and j["Steps"] < 7500:
            df.at[i, "Diabetes"] = "Type II Diabetes"
            # and j["BP"] >= 120


def label_health_risks(df):
    """Determine health risks based on labels, or lack of labels."""
    # df.Health = df.Health.astype(str)
    health = 0
    for i, j in df.iterrows():
        if j["CD"] != "":
            health = health + 2
        if j["MS"] != "":
            health = health + 3
        if j["Diabetes"] != "":
            health = health + 4
        if j["CD"] == "" and j["MS"] == "" and j["Diabetes"] == "":
            health = 0
        df.at[i, "Health"] = health
        health = 0


def remove_columns(df):
    df.drop(["CD", "MS", "Diabetes"], axis=1)


def main(individual_data):
    add_columns(individual_data)
    label_cardiovascular_disease(individual_data)
    label_metabolic_syndrome(individual_data)
    label_diabetes(individual_data)
    label_health_risks(individual_data)
    remove_columns(individual_data)
    individual_data.to_csv("/home/maddykapfhammer/Documents/Allegheny/MozillaFellows/predictiveWellness/src/createData/customIndividual.csv")


if __name__ == "__main__":
    data = individual_data = pd.read_csv("/home/maddykapfhammer/Documents/Allegheny/MozillaFellows/predictiveWellness/src/createData/customIndividual.csv", index_col=[0])
    main(data)
