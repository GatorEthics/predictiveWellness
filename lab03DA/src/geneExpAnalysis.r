# Date: 10 Feb 2020
# Lab03: Gene Expression Analysis
# Name: YourName 

# Select file NCI60.rda from your repository directory data/ when prompted. You will see this file as a variable the Global Environment panel of rStudio.
load(file.choose())

# Select file NCI60cells.rda from your repository directory data/ when prompted. You will see this file as a variable the Global Environment panel of rStudio.
load(file.choose())




# libraries
library(tidyverse)
library(dplyr)






##############################################
# Question 0: What does gsub() do in this code block?

Narrow <- NCI60 %>% tidyr::gather(cellLine, expression, -Probe)
CellTypes <- NCI60cells %>% select(cellLine, tissue) %>% mutate(cellLine=gsub("\\:",".", as.character(cellLine)))
##############################################



# create a subset of the data
Narrow <- Narrow %>% inner_join(CellTypes)

# isolate the TOP3A types of probe samples
Probe_TOP3A <- Narrow %>% filter(Probe == "TOP3A")

# find the mean of each type of each type of cancer tissue
SummaryStats <- Probe_TOP3A %>% group_by(tissue) %>% summarise(mn_exp = exp(mean(expression, na.rm=TRUE)))







##############################################
# Question 1: What does the plot on the next line show?

plot(SummaryStats, main ="Plot 1 ") 
###############################################







##############################################
# Question 2: Plot 2 is a scaled view of the same information from Plot 1. Why is scaling helpful when viewing these results of "Plot 2 ?

#A scaled plot
SummaryStats %>% ggplot(aes(x = tissue, y = mn_exp)) + geom_bar(stat = "identity") + theme(axis.text.x = element_text(angle =30, hjust=1)) + ggtitle("Plot 2")
#############################################







##############################################
# Question 3: What is the function "mutate()" doing in this code block?
# Question 4: What is the function "summarise()" doing in this code block?

SummaryStats <- SummaryStats %>% mutate(tissue = reorder(tissue, mn_exp))
SummaryStats <- Probe_TOP3A %>% group_by(tissue) %>% summarise(mn=mean(expression, na.rm=TRUE), se = (sd(expression, na.rm=TRUE) / sqrt(n())))
#############################################







##############################################
# Question 5: Interpret the results of Plot 3.

SummaryStats %>% ggplot(aes(x = tissue, y = exp(mn))) +  geom_point(data = Probe_TOP3A, aes(x = tissue, y = exp(expression))) + theme(axis.text.x = element_text(angle = 30, hjust = 1)) + ggtitle("Plot 3")
#############################################







##############################################
# Question 6: Interpret the results of Plot 4.


# plot only histogram
SummaryStats %>% ggplot(aes(x = tissue, y = exp(mn))) + geom_bar(stat = "identity", fill = "grey", color = NA) + theme(axis.text.x = element_text(angle = 30, hjust = 1)) + ggtitle("Plot 4")
##############################################







##############################################
# Question 7: In Plot 5, both of the previous plots have been combined together on the same canvas. How does this, either help or confuse the output of these lines of code?

# plotboth plots together on same canvas
SummaryStats %>% ggplot(aes(x = tissue, y = exp(mn))) + geom_bar(stat = "identity", fill = "grey", color = NA) + geom_point(data = Probe_TOP3A, aes(x = tissue, y = exp(expression))) + theme(axis.text.x = element_text(angle = 30, hjust = 1)) + ggtitle("Plot 5")
##############################################


# add some error bars
SummaryStats <- SummaryStats %>% mutate(top = mn * 2 * se , bottom = mn - 2 * se)







##############################################
# Question 8: What do the whiskers (i.e., the big "I" shaped structures above each histogram bar) convey in this plot? Why might we need to know this information?

SummaryStats %>% ggplot(aes(x = tissue, y = exp(mn),color= tissue)) + geom_bar(stat = "identity", alpha = 0.2) + geom_errorbar(aes(x = tissue, ymin = exp(bottom), ymax = exp(top)), width = .5) + theme(axis.text.x = element_text(angle = 30, hjust = 1)) + ggtitle("Plot 7")
##############################################



#install.packages("mosaic")
library(mosaic)
# define an r2 function






##############################################
# Question 9: The word, "function" is below in the code block. What does this part of the code do?
r2 <- function(data){
  # note, if "mosaic" library not installed, then use "install.packages("mosaic")
  mosaic::rsquared(lm(data$expression ~ data$tissue))
}
##############################################







##############################################
# Question 10: Some time is necessary to generate the variable, "ProbeR2". What is taking this code block so long to complete? What is the "lm()" function in R?

# Note: the do() function is analogous to summarise() and the unlist() function is for a simple translation to put the results of do() into a vector form to facilitate plotting.

# Note: The next line may take some minutes to complete.
#This code creates actual cases to describe relationships between anti-cancer drugs and probes  
ProbeR2 <- Narrow %>% group_by(Probe) %>% do(r2 = r2(.)) %>% mutate(r2 = unlist(r2))
##############################################




##############################################
# Next, we would like to pull out the 30 probes with the largest R-squared values to be plotted. In terms of the test, these values indicate that the indepentant variables were able to successfully predict the dependent variables. In this test, these probes responded well (statistically) to tests.

#  Plot 8 is showing R-squared values which have been extracted from a linear model of each Probe. Although we have not yet discussed this form of analysis (regression analysis) in class, it is sufficient to say that R-squared values provide a statistic to determine a fitness of a model. For instance, the R-squared statistic provides a measurement of how much of the variation in a variable, known as a response variable, is accounted for in other explanatory variables. R-squared values extend from 0 to 1 where a zero-value represents a poor prediction by the explanatory variables, where-as a score of 1 indicates a perfect prediction by the explanatory variables. 






##############################################
# Question 11: With the above ideas about R-squared values in mind, which Probe in Plot 8 appears to be able to best explain the model?

Actual <- ProbeR2 %>% arrange(desc(r2)) %>% head(30) %>% mutate(Probe = reorder(Probe, desc(r2)))
Actual %>% ggplot(aes(x = Probe, y = r2))  + geom_point()  + theme(axis.text.x = element_text(angle = 45, hjust = 1)) + ggtitle("Plot 8")
##############################################


# Next, we would like to determine whether the top 30 Probes that we plotted in Plot 8 were actually not relevant dur to being false positives. Now, we will build a Null Hypothesis model out of a set of R-squared values to be used for a comparison. In Plot 8, we argued that those points described relationships between anti-cancer drugs and Probes from tissues. Now, we are going to try to build a model from our data in which there are NO relationships described by the anti-cancer drugs and the Probes in tissues. Then we will test that all the relationships that we plotted in Plot 8, are not included in a plot showing that NO relationships exist.



# Note: this might take some time to complete.
# This code creates null hypotheses cases  
NullR2 <- Narrow %>% group_by(Probe) %>% mutate(expression = mosaic::shuffle(expression)) %>% group_by(Probe) %>% do(r2 = r2(.)) %>% mutate(r2 = unlist(r2))
##############################################






##############################################
# Question 12: In Plot 9 we see two curves. What can you infer about the relationships between the Actual cases of relationships and those cases for which no relationship exists? Remember, the blue curve corresponds to the variable "r2" and the red curve corresponds to the Null values.

ProbeR2 %>% ggplot(aes(x = r2)) + geom_density(fill = "blue", color = "blue4", alpha = .50) + geom_density(data = NullR2, aes(x = r2), fill = "pink", alpha = 0.45, color = "red") + ggtitle("Plot 9")
#Note: Actual cases are blue, Null cases are red.

##############################################



Null <- NullR2 %>% arrange(desc(r2)) %>% head(30) 
Actual$null <- Null$r2


##############################################
# Question 13: Plot 10, is very important to determine a result concerning the Actual data sets and the Null data sets. How do we use this plot to conclude that the 30 probes in Plot 8 are relevant results (i.e., these cases demonstrate relationships)? 

Actual %>% ggplot(aes(x = Probe, y = r2)) + geom_point(color = "blue") + geom_point(aes(y = null), color = "red") + theme(axis.text.x = element_text(angle = 45, hjust=1)) + ggtitle("Plot 10")

#Note: Actual cases are blue, Null cases are red.

##############################################

