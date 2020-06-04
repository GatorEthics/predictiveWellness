# install.packages("tidytext")
library(tidytext)
library(tidyverse)
library(dplyr)

text <- c("Because I could not stop for Death -",
          "He kindly stopped for me -",
          "The Carriage held but just Ourselves -",
          "and Immortality")

# Create a dataframe from input data
text_df <- tibble(line = 1:4, text = text)

# Tokenize the text
text_df %>%
  unnest_tokens(word, text)
