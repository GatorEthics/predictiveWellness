Dr. Bonham-Carter
1 June 2020

#### Declan Casey's theme


Misinformation from incorrect analysis and the spread of bias.


#### Idea paper
_The Making of a President Using Data Analytics and Social Media_ by Ed Lindoo

###### Abstract
Today, political campaigns rely heavily on analytics to target potential voters. The algorithms used, as well as bias that may be introduced in the process, may skew the results and cost an election, as seen in the Clinton campaign. Additionally, Social Media plays a huge role in political races, as does fake news. More alarming is the new trend for Social Media sites to censor anyone or anything which can also make or  break  a  campaign.  In this paper we research events that affected the 2016 Presidential election and present issues that may have an effect on future elections.

###### Keywords
big data, bias, analytics, fake news, social media

###### Reference:
 Lindoo, Ed. "The Making of a President Using Data Analytics and Social Media." Journal of Marketing Development and Competitiveness 14.1 (2020).


###### Notes:
Words and their context lose meaning when they are repeated with out integrity-checking, or checking that their original message and facts is being conserved. Original information may become vulgar, mutated and  meaningless after they are repeated by sources without fact-checking (hear-say.)

Information that may be used to influence an election.

###### Quote:
 _Analysts must be aware of bias and cautious to prevent it in all phases of their analysis. Analytics and ethics are not necessarily enemies but can be if not properly treated. For example, releasing data gained through analytics, whether it is technically correct or not, could result in a company’s loss of their reputation, create competitive weakness, or possibly result in legal sanctions (Noyes, 2015)._


---

#### Coding Goal


###### Purpose:
To demonstrate how information can become misinformed with slight changes in language.

###### TODO: For THIS week

* Literature: Find and read two or three current PEER-REVIEWED articles which discuss the theme of mutated and /or biased information due to social media. Please keep a record of these references in the project repository along with a short summary (no more than five sentences) to give a basic overview of each. Please come to next week's meeting prepared to discuss the articles. Google Scholar might be a good place to begin a search for the keywords,  "Misinformation", "bias", "social media" and similar words.

* Software libraries: Find and follow  coding tutorials of the following suggested text analysis and text manipulation libraries in R (`Spacyr`, `Quanteda`, `text2vec`, `Tidytext` and `Stringr`). The links are listed below.

* Please keep the working code from the tutorial to demonstrate some interesting functionality of text mining using the library.

Please note, you will have to choose one or more of these libraries for next week's programming deliverable and so you are invited to spend some time to decide which you think will be most suitable for the text mining task.

---
###### TODO: For NEXT week


Write a program in R to allow students to study how a message may become mutated by using some social media service. For instance, an original message is stated by a person and then becomes increasingly altered and confused with each additional person who tries mentioned it. The message becomes distorted when it is stated without checking the original facts. If each person invents some new part of the original message, how long will it take for the message to become completely meaningless?

 **Input**: Read-in a textfile of original information to be mutated by an iterative process. Use a text mining library to manipulate the text.

 **Algorithm**: Randomly mutate the text containing over a series of intervals in which only one change may be completed at a time. For instance, only one word or punctuation character may be altered during each iteration. Allow the user to determine how many iterations are allowed.

 **Output**: The new and misinformed text to allow for the study of the distortion of information.

 **Questions**: Please think of some leading questions to help the user to understand what is happening in this demonstration? What is the "take-away" message from this demonstration?

---

#### Ideas for Implementation

###### Potential libraries for project
 * Spacyr:
 	* https://cran.r-project.org/web/packages/spacyr/vignettes/using_spacyr.html
 * Quanteda:
 	* https://quanteda.io/
 * text2vec:
  	* http://text2vec.org/
 * Tidytext:
  	* https://www.tidytextmining.com/
 * Stringr:
  	* https://stringr.tidyverse.org/

 * These above liraries are summarized in https://towardsdatascience.com/r-packages-for-text-analysis-ad8d86684adb


###### Tutorial for basic background

 * TM and Natural language processing:
 	* https://www.youtube.com/watch?v=m8r7WtZ0voQ
 	* The above tutorial uses TM: https://cran.r-project.org/web/packages/tm/vignettes/tm.pdf



###### Deliverables
* Please submit all work in the Mozilla Fellows repository.
	* Articles
	* Code samples from each of the five libraries above
	* Your program to model how information becomes mutated.


Please let me know if you have any questions or concerns.
