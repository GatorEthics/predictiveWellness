# Install all packages, one at a time, line by line
install.packages("quanteda")
install.packages("readtext")
install.packages("quanteda.textmodels")
install.packages("spacyr")

library(quanteda)
summary(data_corpus_inaugural)

# all information used id from the cran, https://cran.r-project.org/web/packages/quanteda/vignettes/quickstart.html

# We use readtext() to takea a file or fileset from disk or a URL, and returns a type of data.frame that can be used directly with the corpus() constructor function, to create a quanteda corpus object
# readtext() works on text (.txt) files, comma-separated-value (.csv) files, XML formatted data, data from the Facebook API, in JSON format, data from the Twitter API, in JSON format, and generic JSON data.

# build a new corpus from the texts
corp_uk <- corpus(data_char_ukimmig2010)  

# To summarize the texts from a corpus, we can call a summary() method defined for a corpus
summary(corp_uk)

# we could add some document-level variables, we can do this using the R’s names() function to get the names of the character vector data_char_ukimmig2010, and assign this to a document variable (docvar)
docvars(corp_uk, "Party") <- names(data_char_ukimmig2010)
docvars(corp_uk, "Year") <- 2010
summary(corp_uk)

# texts in corpus are not designed to be changed internally through cleanin or processing 
# texts can be extracted from the corpus and assigned to new objects, but the idea is that the corpus will remain as an original reference copy

# To extract texts from a corpus, we use an extractor, called texts().
texts(data_corpus_inaugural)[2]

# we can add corpuses together so that no important information is lost
corp1 <- corpus(data_corpus_inaugural[1:5])
corp2 <- corpus(data_corpus_inaugural[53:58])
corp3 <- corp1 + corp2
summary(corp3)

# the corpus_subset() function extracts  a new corpus based on logical conditions applied to docvars
summary(corpus_subset(data_corpus_inaugural, Year > 1990))
summary(corpus_subset(data_corpus_inaugural, President == "Adams"))

# The keywords-in-context function performs a search for a word and allows us to view the contexts in which it occurs
kwic(data_corpus_inaugural, pattern = "terror")

# Using phrase() we can also look up multi-word expressions.
kwic(data_corpus_inaugural, pattern = phrase("United States")) %>%
  head()

# inspect the document-level variables
head(docvars(data_corpus_inaugural))

