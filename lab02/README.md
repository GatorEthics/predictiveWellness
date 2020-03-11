# CMPSC 311- Lab 2: Robotic Agents
**Instructor:** Janyl Jumadinova, Fall 2019

**Assigned:** 11 September 2019

**Due:** Wednesday, 25 September, by 2:30pm (2 weeks)

## Table of Contents

* [Agreement](#Agreement)
* [Lab Team Work Guidelines](#lab-team-work-guidelines)
* [Objectives](#objectives)
* [Reading Assignment](#reading-assignment)
* [Part 1: Task Completion using Perception](#part-1)
* [Part 2: Calibration](#part-2)
* [Configuring Git and GitHub](#Configuring-Git-and-GitHub)
* [Required Deliverables](#required-deliverables)

## Agreement

This laboratory assignment will be completed in groups of two (preferably) or three (if needed). Since you got a first-hand experience working in a robotics team during your first laboratory assignment, before you begin the work on this lab you (as a class) will develop robotics team member guidelines, included in the next section. Instructor will reduce the grade of the team member who fails to follow the team guidelines generated in our robotics group.
By working on and completing this laboratory assignment you agree to use the hardware given to you in a responsible manner. Each group is responsible for the safety and security of the robot while it is in your possession. You are not allowed to take the robots outside of Doane without instructor’s permission. If you need to complete the assignment outside of the laboratory session time, please ask the instructor for access.

## Lab Team Work Guidelines

1. **Play to your strengths:** each team member is assigned specific task(s) that tailor to their strength.
2. **Try every task:**  despite possibly concentrating on a particular task more heavily, each team member will also participate in some degree in every aspect of the lab completion tasks, including robot design, robotic software development, testing, and demonstrations.
3. **Communicate any concerns:** each team member will continuously communicate with other team members, especially when any concerning issues arise.
4. **Don't abandon your team members:** under no circumstances a team member is to stop completing their assigned tasks and attending team work meetings.
5. **Prioritize time and set boundaries:** team members are to discuss the feasibility of the project at the beginning and fill out the “Timeline” section of the report document before beginning the lab work.
6. **Plan the robotic design and team work:** : team members should discuss and agree on the robotic design and its task and also how the work for the lab is to be completed/distributed in the team.
7. **Teams on GitHub:** teams are to use GitHub to  commit their work regularly and to submit their completed code and the report. All team members can contribute to their lab team repository as necessary.

## Objectives
To continue to experiment with Lego EV3 sensors and motors. To create Lego structures with ethical design in mind and to develop programs to complete certain tasks using available sensors. To experiment with the implementation of the perception techniques for the robot. To develop exciting demonstrations for elementary school students and to develop technical presentation skills.

## Reading Assignment
To learn about engineering ethics into artificially intelligent beings please read an article titled
[“Engineering Ethics into a Robot”](https://www.eetimes.com/author.asp?section_id=36&doc_id=1323081).
To learn about robotics ethics please read an article titled
[Robotics ethics: a technology-based ethical framework for today and tomorrow](http://www.unesco.org/new/en/social-and-human-sciences/themes/bioethics/sv0/news/robotics_ethics_a_technology_based_ethical_framework_for_to/) that overviews a report of the Commission on the Ethics of Scientific Knowledge and Technology. Click on the “Read the report and recommendations of COMEST” link and browse through the recommendations at the end relating to the design of the robots.

## Part 1
### Task Completion using Perception
In the first (and main) part of this assignment, you will choose a task that your robot will complete.
The completion of the task you select should utilize at least one sensor, that is the robot must use
its perception to make decisions/take actions. You should change the design of the structure of
your robot to accommodate the selected task completion. You may consult the following Websites
for inspiration:

* https://education.lego.com/en-us/support/mindstorms-ev3/building-instructions#building-core
* https://www.intorobotics.com/best-lego-mindstorms-ev3-robotics-projects/
* http://robotsquare.com/2013/10/01/education-ev3-45544-instruction/

Since this lab is very open ended, to ensure fairness in the amount of work you dedicate to this lab, your selected task (what your robot will do) has to be approved by the instructor. You will be asked to discuss your idea during the class or the lab session. In general, you either need to propose a unique robot design (e.g., the need to rebuild the robot) and a solution for a simple task (e.g., using only one sensor) or a simple design (e.g., minimal need for robot body’s restructuring) with a solution for a more complex task (e.g., involving multiple sensors).

Additionally, you need to develop concrete motivation for the educational purposes of your robotic design. Articles “Robotics for Education” by David Miller, Illah Nourbakhsh, Roland Siegwart and “Teaching a Core CS Concept through Robotics” by S Magnenat, J Shin, F Riedo, R Siegwart will give you some background into robotics used for education. You should answer the following questions before settling on an idea:
* What are the learning objectives of my proposed demonstration?
* What is the hands-on component of my design?

## Part 2
### Calibration
In the second part of the lab assignment, you will add calibration to ensure the sensor readings are as accurate as possible. For this part of the lab, you should conduct experiments and record your results (with at least 10 sensor readings) before calibration, and then do the same after calibration. You should produce a graph with your calibration results and include it in your report.

## Configuring Git and GitHub

To access the template directory for the laboratory assignment, you should go into the #labs channel in our Slack team and find the announcement that provides a link for it which will be posted  on Thursday, September 12. The team leader should accept the laboratory assignment first, create a team and set up the GitHub repository for the team to access the assignment’s starting materials and to store the completed version of your assignment. Once the team has been created, the other members of the team can click on the given GitHub Classroom link and join the team. Every team member can clone the team’s lab02 repository, and use regular Git commands, such
as `git commit`, `git push` and `git pull`. Please ensure your team practices standard GitHub practices to avoid merge conflicts.

## Required Deliverables
This assignment invites you to submit electronic versions of the following deliverables through your GitHub repository.
1. A properly completed and commented source programs. Additionally, your programs must conform to Google style standards. Please submit your complete project directory from Eclipse.
2. The report, stored in `/writing/report.md` and written in Markdown, that contains three paragraphs, with each paragraph containing at least 250 words. In the _first paragraph_ you should describe the specific details of your chosen robotic design and its implementation. The _second paragraph_ should describe the calibration experiments you have performed and include a graph with the calibration results. Finally, in the _third paragraph_, discuss how or whether you have built ethics into your robot through engineering. You should also highlight whether your robot satisfies the recommendations of COMEST.
3. A demonstration of your completed lab to be given during the second portion of the lab session on Wednesday, September 25.
