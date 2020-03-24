# CMPSC 310- Artificial Intelligence: Lab 3
**Instructor:** Janyl Jumadinova, Spring 2020

**Assigned:** 3 March, 2020 at 2:30 pm

**Due:** 3 April, 2020 at 2:30 pm

## Table of Contents

* [Agreement](#Agreement)
* [Lab Team Work Guidelines](#lab-team-work-guidelines)
* [Objectives](#objectives)
* [Reading Assignment](#reading-assignment)
* [Accessing the Laboratory Assignment on GitHub](#Accessing-the-laboratory-assignment-on-GitHub)
* [Automated Text Generation and Analysis](#Automated-text-generation-and-analysis)
* [Testing Your Program](#Testing-Your-Program)
* [Project Presentation](#project-presentation)
* [Required Deliverables](#required-deliverables)
* [Evaluation of Your Laboratory Assignment](#Evaluation-of-your-laboratory-assignment)

## Agreement
This laboratory assignment will be completed in groups of three or four(max). You are free to select your own teams with one caveat, at least one member of your team must be someone you have not been in a team with in this class’s lab. You must receive instructor’s permission if you would like an exception to this rule or if you would like to have a smaller team size. **Each team member must follow the team member guidelines** developed by the students in this class, included in the next section. Instructor will reduce the grade of the team member who fails to
follow the team guidelines generated in our AI group.

## Lab Team Work Guidelines
#### 1. **Organization and function:**
  * Team will delegate one member to be a team manager. In teams of two, the role of the team manager will be restricted to initiating the project on GitHub and resolving merge issues.
  * The project work will be distributed evenly among the team members. The work of being a team manager should count toward work distribution.
  * The team will work collaboratively to create a detailed project work plan with clear deadlines.
  * Teams must ensure that the project’s scope is feasible and that every member of the team is comfortable with the projected scope.

#### 2. **Communication:**
  * All team members must promptly respond to the other team members’ communication.
  * All team members must regularly check and respond to Slack messages and GitHub
issues.
  * Each team member should keep their communication clear and concise.

#### 3. **Interaction:**
  * Conflicts within the team should be first brought to the team leader first. If unresolved, they should be elevated to the instructor.
  * All team members must recognize and avoid biases.
  * Each team member must act in a professional and in a respectful manner.
  * All team members must attend the scheduled team meetings and be punctual.

#### 4. **Project Problem Solving and Decision Making:**
  * During problem solving teams should utilize collaborative brainstorming and researching tactics.
  * During brainstorming each team must ensure that every member is able to express their ideas, solutions, concerns, etc.
  * The decisions about the project are to be made collaboratively. If a decision can not be reached, a majority vote should be the deciding factor, or, in case of a draw, the instructor’s input should be the deciding vote.

## Objectives
To learn how to use a `tensorflow` software library and a neural network algorithm for the natural language processing tasks. To gain understanding of natural language processing techniques that can be used for text generation and text analysis. To evaluate the performance of the machine learning algorithm used for the natural language processing tasks. To reflect on the design and development of the algorithm and to highlight ethical issues raised in the generated text. To produce a supplemental component to motivate the potential issues raised in the developed text synopsis.

## Reading Assignment

To learn more about neural network learning algorithms, you should read Chapter 7.5 in “Artificial Intelligence: Foundations of Computational Agents” book. To learn about `tensorflow` and its use you may follow these [tutorials](https://www.tensorflow.org/tutorials). To see how to use Google’s `colab` environment to run Tensorflow applications, please refer to [this Colab notebook](https://colab.research.google.com/notebooks/intro.ipynb). If you are not familiar with a Python programming language, you may refer to [Python library documentation](https://docs.python.org/3/).

If you have not done so already, please read all of the relevant [“GitHub Guides”](https://guides.github.com/), that explain how to use many of the features that GitHub provides. In particular, please make sure that you have read guides such as “Mastering Markdown” and “Documenting Your Projects on GitHub”; each of them will help you to understand how to use both GitHub and GitHub Classroom.

## Accessing the Laboratory Assignment on GitHub
Since this is a team-based assignment we will be using a group assignment functionality of GitHub Classroom. For team assignments only one person will be creating the team while the other team members will join that team. Please form a team consisting of three or four members, assign one person to be the designated team manager.

The selected team manager should go into the `#labs` channel in our Slack team and find the announcement that provides a link for it. Copy this link and paste it into your web browser. Now, you should accept the laboratory assignment and create a new team with a unique and descriptive team name (under “Or Create a new team”).

Now the other members of the team can click on the assignment link in the `#labs` channel and select their team from the list under “Join an Existing Team”. When other team members join their group in GitHub Classroom, a team is created in our GitHub organization. Teams have pretty cool functionality, including threaded comments and emoji support. Every team member will be able to push and pull to their team’s repository. Your team’s project manager should be the one to resolve any conflicts or merge pull requests.

Unless you provide the instructor with documentation of the extenuating circumstances that you are facing, not working in a team and not accepting the assignment means that you automatically receive a failing grade for it.

## Automated Text Generation and Analysis
One of the grand challenges in AI is developing a system that can comprehend and manipulate language as well as humans do. Automated text generation uses computational linguistics and artificial intelligence to automatically generate natural language texts that satisfy certain communicative requirements. Deep learning algorithms have recently achieved a great success on natural language processing tasks such as machine translation, dialogue response generation, summarization, and other text generation tasks.

In this lab project, each team will use neural network based algorithm with `tensorflow` to create an agent that is able to generate text. The specific text to be generated is a synopsis for a science fiction show as today’s technology tends to be yesterday’s science fiction. During this lab, you are invited to create an agent that is able to generate a synopsis for a science fiction show or
movie that may help us think through different possibilities of (future) technology use. Then, you will analyze your generated text both autonomously and manually and assess its ability to spark discussions on ethical issues surrounding technology.

### 1. Data Gathering
To generate relevant science fiction text you first need relevant data. There are many TV shows or movies that might provide text that would be useful for your task. “Black Mirror” show on Netflix is a good example as most episodes involve the technology that seems feasible (or at least represents a foreseeable straight line from our current capabilities) and takes it a step further. This allows the viewers to ask important questions about possibilities of such technologies. What kinds of regulations would exist in a world that had this technology? What would the terms of service for this technology look like? What social norms would form? What kinds of ethical decisions would individual actors have to make?

*Your first task is to gather useful textual data.* For example, you can get the subtitle (.str) filesfrom https://www.tv-subs.net/, where each file contains the transcript of an episode. You may need to do some pre-processing to get a dialog of each episode without extraneous text. An example of getting a single string which contains the whole dialog of the Black Mirror episode as a paragraph
can be found at https://github.com/pcalderon0711/black-mirror-sentiment-analysis/blob/master/blackmirrorsentiment.ipynb. While the goal of this example tool is to conduct sentiment analysis of Black Mirror episodes, the `return_dialog` method provides Python code for extracting dialog from subtitle files.

### 2. Text Generation using Tensorflow
*Once you have the relevant data, you are to use `tensorflow` and a machine learning algorithm of your choice that is based on the idea of neural networks to automatically generate synopsis for a science fiction show* (see lab slides for reference on the course schedule web page). While your generated text does not need to be structurally or grammatically correct, it should produce some phrases that can be used to extract meaning of what the episode of a show might be about.

There are many examples and tutorials for generating text using Tensorflow. There are also some existing projects that provide tools to automatically generate text. For example, https://github.com/minimaxir/textgenrnn uses recurrent neural network and allow you to train the model on new text relatively easily (see basic example code in the repository). A more recent approach is to use unsupervised learning, TensorFlow and neural networks to create an AI-based text-generation model, called GPT-2, which is trained on huge amounts of text all around the
internet. `gpt-2 simple`(https://github.com/minimaxir/gpt-2-simple) is a Python package which provides many functionalities for model management and generation control, allowing you to easily fine tune GPT-2 on your text (https://minimaxir.com/2019/09/howto-gpt2/).

Thanks to gpt-2-simple and this Colaboratory Notebook, you can easily finetune GPT-2 on your own dataset with a simple function, and generate text to your own specifications! Please select an existing project for text generation and using your own data generate a script for a show (must be a few sentences long).

You will need to either install `tensorflow` locally or via Docker, please refer to the [official website](https://www.tensorflow.org/install) for instructions for both. Alternatively, you can run `tensorflow` applications directly in a browser using Google’s `Colaboratory` platform. Since training and testing natural language models is computationally expensive, with big models running
for hours or days on a regular CPU machine, use of GPU is encouraged. Google’s `Colaboratory` platform allows you to execute programs using `tensorflow` on GPU for free. Go to https://colab.research.google.com/, click on “File”, “New notebook”. Now you can write the code and run it in the web browser. You can also download the program either as a notebook (.ipynb file) or as a Python program (.py file) by going to “File”, “Download”.

### 3. Text Analysis

*After you have an automatically generated text, you will automatically analyze it.*  Here, you are free to select any natural processing task, as long as it extracts some information about your generated text. For example, you can get information about POS or NER or perform a sentiment analysis on your generated text. Fell free to explore and use one of the natural language processing libraries, such as `nltk` (https://www.nltk.org/) or `nlp` (https://nlp.stanford.edu/) to easily accomplish these tasks.

### 4. Supplemental Production
*Finally, to “sell” your script’s synopsis, you are to produce a supplemental production, which could be a tangible product or a visual software artifact.* Please feel free to utilize the resources of the ALIC’s fab lab for this task. For example, perhaps you find a 3D printer model on https://www.thingiverse.com/ that speaks about your synopsis. You can 3D print it and demonstrate it during your presentation. Or, maybe you want to etch the words of your synopsis on wood or
another material. You can use a laser cutter to easily accomplish this task. Or, you may use text to speech library to develop an agent that can speak the text of the synopsis. Or perhaps, you decide to create a digital art (https://adamj.eu/tech/2019/01/24/making-my-own-black-mirrorbandersnatch-easter-egg/). Possibilities are limitless but keep it to something that is feasible to do in a short amount of time.

### Timeline
For this lab you are encouraged to follow a timeline specified below. In your report, you will include the details of the timeline you actually followed. Please remember to record your completed tasks in a timeline as you accomplish them.

**Phase 1 (March 6–13):** Complete task 1 and start task 2. Submit Progress Update. Write a portion of the report.
**Phase 2 (March 25 – April 3):**  Finalize task 2, complete tasks 3 and 4. Complete the report.

## Testing Your Program
Since this is an open-ended assignment involving data and method of your choice you must
execute your program(s) and see if they are producing the expected output. When you believe you have completed all of the requirements of the writing for this lab, you can use the [GatorGrader tool](https://github.com/GatorEducator/gatorgrader) to automatically check if your submission meets the minimum submission requirements (by running the “`gradle grade`” command). If you are using Docker Desktop, you can use the following “`docker run`” command to start “`gradle grade`” as a containerized application, using the “DockaGator” Docker image available on DockerHub. You can run the following command to run the “`gradle grade`” on your project:

```
docker run --rm --name dockagator \
-v "$(pwd)":/project \
-v "$HOME/.dockagator":/root/.local/share \
gatoreducator/dockagator
```

This command will use "``$(pwd)``" (i.e., the current directory) as the project directory and "`$HOME/.dockagator`" as the cached GatorGrader directory. Please note that both of these directories must exist, although only the project directory must contain some content. To ensure that the previous command will work correctly, you should create the cache directory by running the command “`mkdir $HOME/.dockagator`”; you will only need to do this once. If the above “`docker run`” command does not work correctly on the Windows operating system, then you may need to instead run the following command to work around limitations in the terminal window:

```
docker run --rm --name dockagator \
-v "$(pwd):/project" \
-v "$HOME/.dockagator:/root/.local/share" \
gatoreducator/dockagator
```
To enter into an “interactive terminal” in the Docker container, you can instead use the following command:

```
docker run -it --rm --name dockagator \
-v "$(pwd)":/project \
-v "$HOME/.dockagator":/root/.local/share \
gatoreducator/dockagator /bin/bash
```

Now, you can type “`gradle grade`” to run through the checks that the instructor specified for your assignment. Throughout the process of working on this assignment you should remember to transfer your files to GitHub using the “`git commit`” and “`git push`” commands. Remember, to correctly complete this assignment you need to commit all modified files to GitHub. Also, please utilize appropriate GitHub practices while working with your team members to avoid common merge conflicts.

When you use the “`git push`” command to transfer your source code to your GitHub repository, Travis CI will initialize a “build” of your assignment, checking to see if it meets all of the minimum requirements. If your commit meets all of the minimum submission established requirements, then you will see a green ✓ in the listing of commits in GitHub after awhile. If your submission does not meet the requirements, a red ✗ will appear instead. Please note GatorGrader and Travis are used to just ensure that all materials have been submitted. A Travis pass does not indicate a correct completion of the technical details of the lab due to the open ended nature of the lab.

## Project Presentation

During the lab session on *Friday, April 3rd*, each team will be given an opportunity to present their project. During this **five minute** presentation, each team should address the following (you do not need to prepare slides):
* Introduction of the team.
* The overview of the project completed.
* The demonstration.
* Showcase of the developed supplemental production.
* Summary of the results.

## Required Deliverables

This assignment invites you to submit the following deliverables through your team repository.

1. Commit on March 13 by 4:30pm with the “progress update” in the `writing/report.md` file
and the current version of part 1 source code in the `src/generator.py` file (part 2 should be started but does not need to be completed).
2. A properly completed and commented working source programs for the lab. The main source
for parts 1 and 2 should be stored in the `src/generator.py` files and the main source code
for part 3 should be stored in the `src/analyzer.py` file.
3. The report, stored in` writing/report.md` and written in Markdown, that contains answers
to all sections in the report including ethics reflection (follow the prompts inside the report document).
4. Class sessions on March 11 and 13 and the lab session on March 13 is to be used for lab work.
5. The lab session on April 3 will be used for demonstrations.

## Evaluation of Your Laboratory Assignment
The grade that a student receives through Sakai on this assignment will have the following
components:
* **Percentage of Correct GatorGrader Checks and Travis CI Build Status [up to
10%]:** Students are encouraged to repeatedly revise their submission to ensure that it passes all of GatorGrader’s checks about, for instance, the length of the report, its appropriate use of Markdown, and inclusion of minimal programming constraints. The instructor will provide GatorGrader and Travis configuration files during the second week of the lab to each team individually that will be customized to their work.

* **Mastery of Verbal Explanation during Presentation [up to 20%]:** Since the continuous and timely project development and the ability to communicate technical details of
a project is crucial to building successful software and hardware applications, a portion of students’ lab grade will be determined based on the quality of the project walkthrough and the project demonstration.

* **Mastery of Supplemental Production [up to 10%]:** Since the engagement and creativity
is important for new technology’s success and progression, a portion of students’ lab grade
will be determined based on the quality of the supplemental production and its relevance to
the generated synopsis.

* **Mastery of Technical Writing [up to 10%]:** Students will also receive a portion of the
lab grade when the responses to the technical writing questions presented in the `writing/report.md` reveal a mastery of both writing skills and conceptual and technical knowledge. To receive this portion of the grade, the submitted writing should have correct spelling, grammar, and punctuation in addition to following the rules of Markdown and providing conceptually and technically accurate answers.

* **Mastery of Technical Knowledge and Skills [up to 50%]:** Students will receive a
portion of their assignment grade when their project implementation reveals that they have
mastered all of the technical knowledge and skills developed during the completion of this
project. As a part of this grade, the instructor will assess aspects of the project including, but not limited to, the correctness of the program, the completeness of the programming requirements, the use of effective source code comments and Git commit messages.
