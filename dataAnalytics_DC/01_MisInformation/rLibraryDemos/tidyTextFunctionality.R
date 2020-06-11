# We look at the tidy text format, sentiment analysis, and word and document frequency

# install.packages("tidytext")
library(tidytext)
library(tidyverse)
library(dplyr)

text <- c("Because I could not stop for Death -",
          "He kindly stopped for me -",
          "The Carriage held but just Ourselves -",
          "and Immortality")

# Create a dataframe from input data, tidy text uses tibbles
text_df <- tibble(line = 1:4, text = text)

# Tokenize the text, makes it easier to manipulate
text_df %>%
  unnest_tokens(word, text) # arguments are column names

# putting some of Jane Austen's work into the tidy format
library(janeaustenr)
library(dplyr)
library(stringr)
# use mutate() to annotate a line number to keep track of lines in the original format and a chapter()
# to find where the chapters ar
original_books <- austen_books() %>%
  group_by(book) %>%
  mutate(linenumber = row_number(),
         chapter = cumsum(str_detect(text, regex("^chapter [\\divxlc]",
                                                 ignore_case = TRUE)))) %>%
  ungroup()

# to make it tidy, we need to restructure it to one token per row, which is done by the unnest_tokens()
tidy_books <- original_books %>%
  unnest_tokens(word, text) # can do word, character, n-grams, sentences

# We can remove stop words with an anti_join()
data(stop_words)
tidy_books <- tidy_books %>%
  anti_join(stop_words)

# We can also use dplyr’s count() to find the most common words in all the books as a whole
tidy_books %>%
  count(word, sort = TRUE) 

# keeping it tidy allows us to pipe this directly to ggplot2
library(ggplot2)
tidy_books %>%
  count(word, sort = TRUE) %>%
  filter(n > 600) %>%
  mutate(word = reorder(word, n)) %>%
  ggplot(aes(word, n)) +
  geom_col() +
  xlab(NULL) +
  coord_flip()

# We'll use the gutenbergr package to examine some non-Austen texts and their word frequencies
library(gutenbergr)
hgwells <- gutenberg_download(c(35, 36, 5230, 159)) # ID numbers for each novel we're looking at
bronte <- gutenberg_download(c(1260, 768, 969, 9182, 767))

# tidying the novels
tidy_hgwells <- hgwells %>%
  unnest_tokens(word, text) %>%
  anti_join(stop_words)

# the most common words in these specific novels of H.G. Wells
tidy_hgwells %>%
  count(word, sort = TRUE)

tidy_bronte <- bronte %>%
  unnest_tokens(word, text) %>%
  anti_join(stop_words)

library(tidyr)

# calculate the frequency for each word for the works of Jane Austen, the Brontë sisters, and H.G.
# Wells by binding the data together by using the spread and gather functions from tidyr so that we can
# plot and compare them
frequency <- bind_rows(mutate(tidy_bronte, author = "Brontë Sisters"),
                       mutate(tidy_hgwells, author = "H.G. Wells"), 
                       mutate(tidy_books, author = "Jane Austen")) %>% 
  mutate(word = str_extract(word, "[a-z']+")) %>%
  count(author, word) %>%
  group_by(author) %>%
  mutate(proportion = n / sum(n)) %>% 
  select(-n) %>% 
  spread(author, proportion) %>% 
  gather(author, proportion, `Brontë Sisters`:`H.G. Wells`)

# a plot showing the most common words in each text 
library(scales)
ggplot(frequency, aes(x = proportion, y = `Jane Austen`, color = abs(`Jane Austen` - proportion))) +
  geom_abline(color = "gray40", lty = 2) +
  geom_jitter(alpha = 0.1, size = 2.5, width = 0.3, height = 0.3) +
  geom_text(aes(label = word), check_overlap = TRUE, vjust = 1.5) +
  scale_x_log10(labels = percent_format()) +
  scale_y_log10(labels = percent_format()) +
  scale_color_gradient(limits = c(0, 0.001), low = "darkslategray4", high = "gray75") +
  facet_wrap(~author, ncol = 2) +
  theme(legend.position="none") +
  labs(y = "Jane Austen", x = NULL)







