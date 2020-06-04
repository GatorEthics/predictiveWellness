# Install all packages, one at a time, line by line
install.packages("quanteda")
install.packages("readtext")
install.packages("quanteda.textmodels")
install.packages("spacyr")

library(quanteda)
summary(data_corpus_inaugural)

# all information used id from the cran, https://cran.r-project.org/web/packages/quanteda/vignettes/quickstart.html

# we use readtext() to takea a file or fileset from disk or a URL, and returns a type of data.frame that can be used directly with the corpus() constructor function, to create a quanteda corpus object
# readtext() works on text (.txt) files, comma-separated-value (.csv) files, XML formatted data, data from the Facebook API, in JSON format, data from the Twitter API, in JSON format, and generic JSON data.

# build a new corpus from the texts
corp_uk <- corpus(data_char_ukimmig2010)  

# to summarize the texts from a corpus, we can call a summary() method defined for a corpus
summary(corp_uk)

# we could add some document-level variables, we can do this using the R’s names() function to get the names of the character vector data_char_ukimmig2010, and assign this to a document variable (docvar)
docvars(corp_uk, "Party") <- names(data_char_ukimmig2010)
docvars(corp_uk, "Year") <- 2010
summary(corp_uk)

# texts in corpus are not designed to be changed internally through cleanin or processing 
# texts can be extracted from the corpus and assigned to new objects, but the idea is that the corpus will remain as an original reference copy

# to extract texts from a corpus, we use an extractor, called texts().
texts(data_corpus_inaugural)[2]

# we can add corpuses together so that no important information is lost
corp1 <- corpus(data_corpus_inaugural[1:5])
corp2 <- corpus(data_corpus_inaugural[53:58])
corp3 <- corp1 + corp2
summary(corp3)

# the corpus_subset() function extracts  a new corpus based on logical conditions applied to docvars
summary(corpus_subset(data_corpus_inaugural, Year > 1990))
summary(corpus_subset(data_corpus_inaugural, President == "Adams"))

# the keywords-in-context function performs a search for a word and allows us to view the contexts in which it occurs
kwic(data_corpus_inaugural, pattern = "terror")

# using phrase() we can also look up multi-word expressions.
kwic(data_corpus_inaugural, pattern = phrase("United States")) %>%
  head()

# inspect the document-level variables
head(docvars(data_corpus_inaugural))

# we can also extract many features from a Corpus
# to tokenize a text we use the tokens() method
txt <- c(text1 = "This is $10 in 999 different ways,\n up and down; left and right!",
         text2 = "@kenbenoit working: on #quanteda 2day\t4ever, http://textasdata.com?page=123.")
tokens(txt)

# we can also clean up our tokens with these parameters
tokens(txt, remove_numbers = FALSE, remove_punct = FALSE, remove_separators = FALSE)

# we also have the option to tokenize characters as well as sentences
tokens("Great website: http://textasdata.com?page=123.", what = "character")
tokens(c("Kurt Vongeut said; only assholes use semi-colons.",
         "Today is Thursday in Canberra:  It is yesterday in London.",
         "En el caso de que no puedas ir con ellos, ¿quieres ir con nosotros?"),
       what = "sentence")

# tokens_compound() allows us to concatenate multi-word expressions and keep them as a single feature
tokens("New York City is located in the United States.") %>%
  tokens_compound(pattern = phrase(c("New York City", "United States")))

# we use the dfm() function to produce a matrix associating values for certain features with each document
# dfm() performs tokenization and tabulates the extracted features into a matrix of documents by features
corp_inaug_post1990 <- corpus_subset(data_corpus_inaugural, Year > 1990)
dfmat_inaug_post1990 <- dfm(corp_inaug_post1990)
dfmat_inaug_post1990[, 1:5]

# make a dfm, removing stopwords and applying stemming
dfmat_inaug_post1990 <- dfm(dfmat_inaug_post1990,
                            remove = stopwords("english"),
                            stem = TRUE, remove_punct = TRUE)
# you can see the stopwords for english using head(stopwords("en"), 20)
head(stopwords("en"), 20)

# to access a list of the most frequently occurring features, we can use topfeatures()
topfeatures(dfmat_uk, 20) # 20 most frequent words
