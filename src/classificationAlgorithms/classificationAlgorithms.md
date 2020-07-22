# Classification in Vigor

Vigor is a tool which focuses on using artificial intelligence and classification algorithms to accurately predict health risks of an individual based on certain metrics.

There are many classification algorithms that exist, and even more are currently being developed. Vigor uses the three major classification algorithms which provide the basics of artifical intelligence classification, including:

- Niave Bayes

- Decision Tree

- Support Vector Machine

Each of these algorithms can be accessed with multiple different Python libraries, for the purposes of this tool, the primary library used is [scikit-learn](https://scikit-learn.org/stable/) a library for machine learning in Python.

## General Classification

Classification is an aspect of artificial intelligence and machine learnining which predicts a class label for a given input. A predictive classification algorithm, also known as a model requires a training dataset with inputs and outputs, from which an algorithm can learn which labels are associated with which data. After training, labels can be predicted for a certain set of data. There are multiple different types of classification, including:

- Classification Predictive Modeling

- Binary Classification

- Multi-Class Classification

- Multi-Label Classification

- Imbalanced Classification

Each of these algorithms require slightly different training data, and also give a different output, based on the data given. Vigor primarily works with Classification Predictive Modeling, and Multi-Label Classification.

## More About Algorithms

### Niave Bayes

The Naive Bayes classification algorithm is based on Bayes' Theorem which is often used to classify objects. This theorem focuses on the probability of an event, as new data is introduced. This classifier assumes that all data provided is independent of each other, allowing accurate labeling of data. This type of classification is not made up of only one algorithm, but rather a family of multiple algorithms which work with statistics and statistical independence. Naive Bayes classification is most often used with text, but can also be modified to work with numerical values as well.

### Decision Tree

Decision tree classification is a type of regression model which is in the form of a tree structure. It takes an input of data, which is then broken down into smaller subsets while a decision tree is also developed. This results in a binary tree with decision nodes and leaf nodes. A decision node represent a question asked about the data, and a leaf node corresponds to the answer/decision/conclusion if reached. The root of the decision tree correponds to the entry point of the data, and also the best predictor of the dataset. The algorithm associated with decision tree classification employs the use of a top-down search through the possible branches, and does not allow backtracking; finally resulting in the most accurate label possible.

### Support Vector Machine

Support Vector Machine classification, often abbreviated to SVM, contains and algorithm which focuses on problems specifically with two groups or data with two separate features. Labeled training data is plotted on a plane. With plotted training data, the support vector machine algorithm outputs the hyperplane (or line) which most accurately separates the data. With SVM, the hyperplane is defined by which line maximizes the margins from both labels. This line is considered the decision boundry, and then helps to classify and label testing data. With non-linear data, a third dimension is added to the SVM plane, for more accurate hyperplane definition. SVM is also often paired with language and text classification, but can work with numerical variables as well.
