# Install all packages, one at a time, line by line
install.packages("quanteda")
install.packages("readtext")
install.packages("devtools")
devtools::install_github("quanteda/quanteda.corpora")
install.packages("quanteda.textmodels")
install.packages("spacyr")
install.packages("newsmap")

# Use these requirements for projects
# require(quanteda)
# require(readtext)
# require(quanteda.textmodels)
# require(quanteda.corpora)
# require(newsmap)

library(quanteda)
summary(data_corpus_inaugural)