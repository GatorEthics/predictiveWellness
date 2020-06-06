# The text2vec package solves the memory allocation issues normally confronted by processing many 
# documents as a single vector by providing a better way of constructing a document-term matrix.
# The following code was taken from https://cran.r-project.org/web/packages/text2vec/vignettes/text-vectorization.html
# and focuses on sentiment analysis.
# This library seems a bit complex and uses more machine learning methods, many of which went over my
# my head while typing out this demo code on my own, I will ask questions as I present.
install.packages(text2vec)
install.packages(data.table)
install.packages(magrittr)

# We will split our dataset into two parts, train and test, showing how to perform data manipulations 
# on the training set and then apply  the same manipulations on the test set
library(text2vec)
library(data.table)
library(magrittr)
data("movie_review") # this dataset consists of 5000 movie reviews, each makred positive or negative
setDT(movie_review)
setkey(movie_review, id)
set.seed(2017L)
all_ids = movie_review$id
train_ids = sample(all_ids, 4000)
test_ids = setdiff(all_ids, train_ids)
train = movie_review[J(train_ids)]
test = movie_review[J(test_ids)]

# Creating a vocbaulary based DTM# define preprocessing function and tokenization function
prep_fun = tolower
tok_fun = word_tokenizer

it_train = itoken(train$review, # Created an iterator using the itoken() function
                  preprocessor = prep_fun, #unctions prefixed with create_ work with these iterators
                  tokenizer = tok_fun, # process data in memory friendly chunks
                  ids = train$id, 
                  progressbar = FALSE)
vocab = create_vocabulary(it_train)

# We could also create a list of tokens and reuse it in further steps
# Each element of the list should represent a document, and each element should be a character vector
# of tokens:
# train_tokens = tok_fun(prep_fun(train$review))

# it_train = itoken(train_tokens, 
                  # ids = train$id,
                  # # turn off progressbar because it won't look nice in rmd
                  # progressbar = FALSE)

# vocab = create_vocabulary(it_train)

# We can now construct a document-term matrix with out vocabulary
vectorizer = vocab_vectorizer(vocab)
t1 = Sys.time()
dtm_train = create_dtm(it_train, vectorizer) # the dtm function
print(difftime(Sys.time(), t1, units = 'sec')) # check how long it took

# We can check the dimensions of the dtm
dim(dtm_train)

# Now we can fit our first model using the glmnet package to fit a logistic regression model with an
# L1 penalty and 4 fold cross-validation
install.packages("glmnet")
library(glmnet)
NFOLDS = 4
t1 = Sys.time()
glmnet_classifier = cv.glmnet(x = dtm_train, y = train[['sentiment']], 
                              family = 'binomial', 
                              # L1 penalty
                              alpha = 1,
                              # interested in the area under ROC curve
                              type.measure = "auc",
                              # 5-fold cross-validation
                              nfolds = NFOLDS,
                              # high value is less accurate, but has faster training
                              thresh = 1e-3,
                              # again lower number of iterations for faster training
                              maxit = 1e3)
print(difftime(Sys.time(), t1, units = 'sec'))

# Then we can plot the logisitical regression model
plot(glmnet_classifier)

# Now we can check the model’s performance on test data. We use exactly the same functions from
# prepossessing and tokenization
# Most text2vec functions are pipe friendly
it_test = tok_fun(prep_fun(test$review))
# turn off progressbar because it won't look nice in rmd
it_test = itoken(it_test, ids = test$id, progressbar = FALSE)


dtm_test = create_dtm(it_test, vectorizer)

preds = predict(glmnet_classifier, dtm_test, type = 'response')[,1]
glmnet:::auc(test$sentiment, preds)
# performance on the test data is roughly the same

# We can reduce the time on our training model pruning the vocabulary, paritcularly removing the stop
# words. The corpus also contains very uncommon terms and since there isn't much data or statistics on
# them, they are also useless.
stop_words = c("i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours")
t1 = Sys.time()
vocab = create_vocabulary(it_train, stopwords = stop_words)
print(difftime(Sys.time(), t1, units = 'sec'))

# create dtm_train with new pruned vocabulary vectorizer
pruned_vocab = prune_vocabulary(vocab, 
                                term_count_min = 10, 
                                doc_proportion_max = 0.5,
                                doc_proportion_min = 0.001)
vectorizer = vocab_vectorizer(pruned_vocab)

# We can check the dimensions of the new dtm
dim(dtm_train)

# create DTM for test data with the same vectorizer
dtm_test = create_dtm(it_test, vectorizer)
dim(dtm_test)

