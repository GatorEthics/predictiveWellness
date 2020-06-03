# make sure you have some version of conda installed before running these commands, https://docs.conda.io/en/latest/miniconda.html

install.packages("spacyr")
library("spacyr")
spacy_install()
spacy_initialize(model = "en_core_web_sm")

# Basic sentences to be processed and lemmatized
txt <- c(d1 = "spaCy is great at fast natural language processing.",
         d2 = "Mr. Smith spent two years in North Carolina.")

# Process documents and obtain a data.table
parsedtxt <- spacy_parse(txt)
parsedtxt

# Remove unnecessary information from the data.table
spacy_parse(txt, tag = TRUE, entity = FALSE, lemma = FALSE)

# Directly parse a text as a named list
spacy_tokenize(txt)

# Directly parse a text as a data.frame
spacy_tokenize(txt, remove_punct = TRUE, output = "data.frame") %>%
  tail()

# Update the parsed text file and extract named entities
parsedtxt <- spacy_parse(txt, lemma = FALSE, entity = TRUE, nounphrase = TRUE)
entity_extract(parsedtxt)

# Extract or concatenate noun phrases
nounphrase_extract(parsedtxt)

# Consolidate noun phrases into single tokens
nounphrase_consolidate(parsedtxt)

# Extract either only entities or noun phrases without parsing the entire text
spacy_extract_entity(txt)
spacy_extract_nounphrases(txt)

# Detailed parsing of syntactic dependencies is possible with the 'dependency = TRUE' option:
spacy_parse(txt, dependency = TRUE, lemma = FALSE, pos = FALSE)

# Extract additional attributes such as numbers or email with 'addition_attributes'
spacy_parse("I have six email addresses, including me@mymail.com.", 
            additional_attributes = c("like_num", "like_email"),
            lemma = FALSE, pos = FALSE, entity = FALSE)