# CMPSC 311- Robotic Agents: Lab 1
**Instructor:** Janyl Jumadinova, Fall 2019

**Assigned:** 4 September 2019

**Due:** Wednesday, 11 September, by 4:20pm

## Table of Contents

* [Agreement](#Agreement)
* [Objectives](#objectives)
* [Reading Assignment](#reading-assignment)
* [Configuring Git and GitHub](#Configuring-Git-and-GitHub)
* [Robotic Field Day](#robotic-field-day)
* [Set Up leJOS and Start the Project](#set-up-leJOS)
* [Lego EV3 Robot](#lego-ev3-robot)
* [Robotic Field Day Activities](#robotic-field-day-activities)
* [SSH Legacy Option Configuration](#ssh-Legacy-option-configuration)
* [Uploading Programs Using `ssh`](#Uploading-programs)
* [Required Deliverables](#required-deliverables)

## Agreement

This laboratory assignment will be completed in groups of two (preferably) or three (if needed). You may select your group members and your own robot, which you will be responsible for. By working on and completing this laboratory assignment you agree to use the hardware given to you in a responsible manner. Each group is responsible for the safety and security of the robot while it is in your possession. You are not allowed to take the robots outside of Doane without instructor’s permission. If you need to complete the assignment outside of the laboratory session time, please ask the instructor for access.

## Objectives
* To establish and configure GitHub to access the files for a laboratory assignment.
* To learn how to use and experiment with Lego EV3 sensors and motors.
* To gain experience in building robotic programs to complete certain tasks using available sensors.
* To design and develop robust robotic applications for competitive movement scenarios using the development of ethical and aggressive robots.
* To reflect on the design and algorithmic choices of your robot and ethical implications of the robot’s behavior.

## Reading Assignment

To learn about ethical and aggressive robots please read an article titled [“Why Ethical Robots Might Not Be Such a Good Idea After All”](https://spectrum.ieee.org/automaton/robotics/artificial-intelligence/why-ethical-robots-might-not-be-such-a-good-idea-after-all) by Alan Winfield, which was inspired by an article titled [“The Dark Side of Ethical Robots”](https://www.aies-conference.com/2018/contents/papers/main/AIES_2018_paper_98.pdf) by Dieter Vanderelst and Alan Winfield.

To complete the necessary installations on your machine to work with leJOS, please follow the [tutorials](https://sourceforge.net/p/lejos/wiki/Home/). To learn how to program an EV3 robot using leJOS, please consult [leJOS API](http://www.lejos.org/ev3/docs/).

If you have not done so already, please read all of the relevant [“GitHub Guides”](https://guides.github.com/), that explain how to use many of the features that GitHub provides. In particular, please make sure that you have read guides such as **“Mastering Markdown”** and **“Documenting Your Projects on GitHub”**; each of them will help you to understand how to use both GitHub and GitHub Classroom.

## Configuring Git and GitHub
During this and the subsequent laboratory assignments, we will securely communicate with the GitHub servers that will host all of the project templates and your submitted deliverables. In this assignment, you will perform all of the steps to configure your account on GitHub, so that you can complete lab assignments using GitHub Classroom.

1. If you do not already have a GitHub account, then please go to the [GitHub website](https://github.com/) and create one, making sure that you use your “allegheny.edu” email address so that you can join GitHub as a student at an accredited educational institution. You are also encouraged to sign up for [GitHub’s “Student Developer Pack”]( https://education.github.com/pack), qualifying you to receive free software development tools. Additionally, please add a description of yourself and an appropriate professional photograph to your GitHub profile. Unless your username is taken, you should also pick your GitHub
username to be the same as Allegheny’s Google-based email account.

2. If you have never done so before, you must use the “ssh−keygen” program to create secureshell keys that you can use to support your communication with GitHub. Open the terminal and type the “ssh−keygen” command in it. Follow the prompts to create your keys and save them in the default directory. That is, you should press "Enter" after you are prompted to “Enter file in which to save the key ... :” and then type your selected passphrase whenever you are prompted to do so or press “Enter” for no passphrase to be used. Please note that a “passphrase” is like a password that you will type when you need to prove your identify
to GitHub.

3. Now, in the GitHub’s website and look in the right corner for an account avatar with a down arrow. Click on this link and then select the “Settings” option. Now, scroll down until you find the “SSH and GPG keys” label on the left, click to create a “New SSH key”, and then upload your ssh key to GitHub. You can copy your SSH key to the clipboard by going to the terminal and typing `cat ~/.ssh/id rsa.pub` command and then highlighting this output. When you are completing this step in your terminal window, please make sure that you only highlight the letters and numbers in your key—if you highlight any extra symbols or spaces then this step may not work correctly. Then, paste this into the GitHub text field in your
web browser.

To access the laboratory assignment, you should go into the #labs channel in our Slack team and find the announcement that provides a link for it. Copy this link and paste it into your web browser. Now, you should accept the laboratory assignment and see that GitHub Classroom created a new GitHub repository for you to access the assignment’s starting materials and to store the completed version of your assignment.

**It is recommended that you create a directory called “labs”, which will act as your lab workspace for Eclipse.** Now click the “Clone or download” button and, after ensuring that you have selected “Clone with SSH”, please copy this command to your clipboard. By typing `git clone` in your terminal and then pasting in the string that you copied from the GitHub site you will download all of the code for this assignment.

## Robotic Field Day

In this lab, you will learn how to use and program Lego EV3 robots and their sensors. As a part of this learning experience you will extend and modify Java programs run on EV3 robots that allow the robots to compete in various robotic field day activities. We will have a robotic field day challenge during the beginning of the lab on _Wednesday, September 11_. The activities chosen for this event give a general overview of the EV3 sensors and an introduction to topics such as navigation and obstacle avoidance.

### Set Up leJOS and Start the Project
leJOS is a small Java Virtual Machine, which allows us to write Java programs for [Lego robots](http://www.lejos.org). You will be using leJOS to write Java programs for a Lego EV3 robot using a plugin (add-on software) in a development environment called “Eclipse”. You should first ensure that Eclipse and leJOS are correctly installed on your computer. Then, you need to complete the following instructions to configure Eclipse to work on leJOS and to recognize the Lego Robots.

1. Start “Eclipse” and when the “Workspace Launcher” comes up, navigate your workspace to the “labs” directory you created earlier. You can also create a new leJOS project in Eclipse and copy the given program into the new project.

2. Turn on your robot by pushing the middle square button on the robot.

3. Using the top menu in Eclipse, click on "Window", select "Preferences", you will see a small window pop up as in the snapshot shown below. Click on "leJOS EV3" on the left-side of the menu, check boxes for "Run Tools in separate JVM", "Connect to named brick", and "Run program after upload". Verify that "EV3 HOME" has ""/opt/lejos-ev3" field populated next to it. Then, next to the "Connect to named brick" you have to specify the IP address of your robot. Without the WIFI dongle connected to your robot, the IP should be 10.0.1.1, but you may want to verify this by cross-checking it with the second line displayed on your robot’s
LCD screen. Click "OK".

4. leJOS compilation level must be set to 1.7. You set the compilation level of leJOS applications to 1.7 by going to “Window”, “Preferences”, “Java”, “Compiler”.

![Preferences Screen](link)
**Currently refer to the [original lab pdf](https://www.cs.allegheny.edu/sites/jjumadinova/teaching/311/labs/cs311f2019_lab1.pdf) for image**

5. Now you are ready to start developing Java programs for a Lego robot!

## Lego EV3 Robot
Lego EV3 robot contains a programmable EV3 controller, called a “brick”, user interface with an LCD screen, Lego building blocks, motors and various sensors such as light, ultrasonic, color, touch, gyro. The brick contains four outputs (motors), four inputs (sensors), USB, Bluetooth, or Wi-Fi connection, LCD screen, 16 MB flash memory, 64 MB RAM, SD Card Port, EV3 Brick Button lights, sound. EV3 Brick buttons are explained in the figure below:

![EV3 Brick button diagram](link)
**Currently refer to the [original lab pdf](https://www.cs.allegheny.edu/sites/jjumadinova/teaching/311/labs/cs311f2019_lab1.pdf) for image**

First of all, you will import an existing project and run the sample program. A basic program to complete in the sprint race is given to you in the course repository. This program demonstrates how to set up motors and sensors. You should study the given program and use it as a building block to develop your own. Please complete the following steps to import the given project and execute the basic programs on the Lego robot.

1. The first thing you need to do is to import a leJOS EV3 project. Using the top menu in Eclipse, click on “File”, “Import”, “Existing Projects into Workspace”, “Import Projects from File System”. Now navigate to the lab01 directory that you cloned earlier from GitHub. Then click “Finish”. This will add a directory with lab01 starter contents in your “Package Explorer” view on the left-side panel in Eclipse (close the “Welcome” window if there is one).

2. Make sure your EV3 robot is turned on, is connected to the computer via a USB cable or has a WIFI dongle attached and its menu is running. Now run your sample program by rightclicking of the class name from the “Package Explorer”, and selecting “Run As”, “leJOS EV3 Program”. You should then see the message on the EV3 robot’s LCD screen. After you upload the program from Eclipse, if you would like to run the same program more than once, you do not have to upload it again - you can just use EV3 robot’s menu, go to “Programs” and click on the program you wish to run. However, if you make changes to the program, then you have to upload the new version to the robot.

3. Next, make sure all the sensors are connected to the correct ports. There are five steps in using a sensor using the method in the given program: 1) get a port, initialize the sensor, get a SampleProvider, create an array to store samples and take samples. All of the steps except the last one only need to be done once in a program. The last step needs to be repeated every time the program takes a new measurement. In LeJOS each sensor uses standard units, SI-units. So, distances are always returned in meters, acceleration is always returned in `m/s^2`, angles are always measured in degrees, etc.

4. Now, review the provided sample programs and read the description of the race activities below. Then, you should decide what design and development choices you will make. In particular, you should decide on any modifications to the structure of the robot and the placement of the sensors. Then, you should make changes to the sample programs to ensure they are more successful in the races with one caveat. **You are required to develop either an ethical or an aggressive robot behavior, while having at least one behavior in one of the three races** (that is you can not have aggressive robots participate in all three races).

5. Finally, you must ensure that your programs meet the Google style guidelines. In order to do this effectively, please download the `eclipse-java-google-style.xml` file from [Google Style Guide](http://code.google.com/p/google-styleguide/). Then, in Eclipse, under “Window/Preferences”
select “Java/Code Style/Formatter”, and import the settings file by selecting “Import”. Then, in the “Preferences” menu (same as before), go to “Java”, “Editor”, “Save Actions”, select “Perform the selected actions on save”, select “Format source code”, click the “Formatter” link and ensure the “GoogleStyle” formatter is selected as active. Click OK.

## Robotic Field Day Activities

1. **Sprint Race:** all of the robots will start together at the same line and will race along a straight path for three meters until a wall is reached. The wall can be detected by the touch sensor or an ultrasonic sensor, the given program uses the touch sensor. The robot that reaches the wall first wins.

2. **Pushing Race:** all of the robots will start at the same line with a colored box right in front of it (front center). The robot needs to push the box along a straight path for three meters until it pushes the box into a larger box. Large boxes will be positioned horizontally across the length of the wall to catch the small boxes. The robot that pushes the small box into the larger box first wins. The robot may be stopped manually (using an escape button push) for this activity if the robot succeeds or if the team desires to restart the race.

3. **Obstacle Race:** each robot will travel from their starting position straight until they reach the (long) red finish line, while avoiding (not hitting) obstacles set up in the environment. The obstacles include small rectangular boxes. If an obstacle gets knocked down after your robot bumps it, your robot will receive a penalty of -10 sec added to the total time, if the obstacle gets touched and moved by your robot, your robot will receive a penalty of -5 sec added to the total time. The robot that is able to complete the obstacle course by reaching the red finish line the fastest wins. This activity will be completed sequentially by the robots and each robot will be timed.

## SSH Legacy Option Configuration
In order to allow ssh to connect to the robots, you need to configure ssh to enable the `diffie-hellman-group1-sha1` key exchange algorithm using the `KeyxAlgorithms` option. The most convenient way to do this is by modifying the `config` file in the `.ssh` directory:

* In the terminal, type: `vim ∼/.ssh/config`
* Add the following to the `config` file:
```
Host ip_of_your_robot
HostKeyAlgorithms +ssh-dss
```

## Uploading Programs Using `ssh.`
If you would like to use `ssh` (instead of the USB cable) to upload jar files to your robot, you can follow the following steps:

1. You can copy jar files from your workspace on your computer to the robot through ssh by using the regular `scp` command. For example, if I wanted to copy Test.jar from my workspace into ‘programs’ directory on the robot, then after I changed into my workspace directory, I would type:
`scp Test.jar root@ip_address:/home/lejos/programs` or (depending on your path)
`scp Test.jar root@ip_address:/home/root/lejos/programs`

2. To access your robot through ssh in your terminal, type
`ssh root@ip_address`
Type `admin` when you are prompted to enter the ‘password’

3. Change your directory to `/lejos/programs` or create one if it does not exist

4. Choose one of the programs in the ‘programs’ directory. In your terminal, type
`jrun -jar SomeProgram.jar`
This should run the program on your robot.

5. _Please **root** responsibly_

## Required Deliverables
This assignment invites you to submit electronic versions of the following deliverables through your GitHub repository.

1. A properly completed and commented source programs. Additionally, your programs must conform to Google style standards. Please submit your complete project directory from Eclipse.

2. The report, stored in /writing/report.md and written in Markdown, that contains three paragraphs, with each paragraph containing at least 250 words. In the first paragraph you should describe the specific details of your implementation and any design decisions you made in constructing your robot and your programs. The second paragraph should describe the ethical or aggressive behavior of your robot for each race. Finally, in the third paragraph, summarize the assigned reading in a few sentences, and using the assigned article as a resource as necessary include your observations about the overall races containing both ethical and aggressive robots after the races have been completed.
