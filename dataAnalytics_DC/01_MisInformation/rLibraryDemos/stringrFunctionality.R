# Main uses for stringr
# 1) Character manipulation: these functions allow you to manipulate individual characters within the strings in character vectors.
# 2) Whitespace tools to add, remove, and manipulate whitespace.
# 3) Locale sensitive operations whose operations will vary from locale to locale.
# 4) Pattern matching functions. These recognise four engines of pattern description. The most common is regular expressions, but there are three other tools.

install.packages("stringr")
install.packages("devtools")
devtools::install_github("tidyverse/stringr")

# 
# All functions in stringr start with str_ and take a vector of strings as the first argument
x <- c("why", "video", "cross", "extra", "deal", "authority")
str_length(x)
str_c(x, collapse = ", ")

# WHITESPACE
# str_pad adds whitespace to either the right, left, or both sides of a string, default pads to the left
x <- c("abc", "defghi")
str_pad(y, 5)

# str_trim does the opposite, removing either leading or trailing whitespaces
x <- c("  a   ", "b   ",  "   c")
str_trim(x)

# combine str_pad() and str_trunc() to ensure all string are the same length
x <- c("Short", "This is a long string")
x %>% 
  str_trunc(10) %>% 
  str_pad(10, "right")

# str_wrap() wraps an existing paragraph with whitespace, in a sense justifying the paragraph
jabberwocky <- str_c(
  "`Twas brillig, and the slithy toves ",
  "did gyre and gimble in the wabe: ",
  "All mimsy were the borogoves, ",
  "and the mome raths outgrabe. "
)
cat(str_wrap(jabberwocky, width = 40))

# LOCALE SENSITIVE
# Certain functions perform differently in different parts of the world
# In turkish there are two types of i's so it may not put all i's into lowercase
x <- "I like horses."
str_to_upper(x)
str_to_title(x)
str_to_lower(x)
# tr, denotes turkish
str_to_lower(x, "tr")

# PATTERN MATCHING
# Each pattern matching function has the same first two arguments, a character vector of strings and a single pattern to match agaisnt that
# You can use either a regular expression as the pattern, bytewise matching, locale sensitive matching, or boundary matching
# The ones most pertinent for us are pattern and boundary matching
# Character vector of strings
strings <- c(
  "apple", 
  "219 733 8965", 
  "329-293-8753", 
  "Work: 579-499-7527; Home: 543.355.3679"
)
# Regular expression to match US phone numbers
phone <- "([2-9][0-9]{2})[- .]([0-9]{3})[- .]([0-9]{4})"

# which strings contain phone numbers?
str_detect(strings, phone)

# what are the elements of the string that contain phone numbers?
str_subset(strings, phone)

# how many phone numbers in each string?
str_count(strings, phone)

# where in the string is the phone number located?
(loc <- str_locate(strings, phone))
str_locate_all(strings, phone)

# What are the phone numbers?
str_extract(strings, phone) # only lists the first
str_extract_all(strings, phone) # lists all

# Pull out the three components of the match
str_match(strings, phone) # character matrix of the first match
str_match_all(strings, phone) # character matrix for all matches

# replace the matched string with something else
str_replace(strings, phone, "XXX-XXX-XXXX") # replaces only the first match
str_replace_all(strings, phone, "XXX-XXX-XXXX") # replaces all matches

# splits a string into a number of individual pieces and returns a character matrix
str_split("a-b-c", "-")

# splits a string into a fixed number of pieces based on a pattern and returns a character matrix
str_split_fixed("a-b-c", "-", n = 2)

# BOUDARY MATCHING
# boundary() matches boundaries between characters, lines, sentences or words
x <- "This is a sentence."
str_split(x, boundary("word"))
str_extract_all(x, boundary("word"))

# "" is treated as boundary("character")
str_split(x, "")
str_count(x, "")





















