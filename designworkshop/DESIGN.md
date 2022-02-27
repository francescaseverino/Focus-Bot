# Problem Statement

Time management continues to be one of the best ways to gain control over one's life. For the typical college student, managing Things such as homework, sports, social time and other components of our lives can become quite a complicatedprocess.fo much so that refraining kom practicing Ame management leads to disorganized schedules, late submissions and all around chaos. The constantly changing environment of a college student makes the process of completing tasks in an efficient, timely manner all the more harder to achieve. As the responsibility of each student piles up, it becomes more difficult to choose what to do and when to do it with the number of over. all tasks to complete in mind.


# Bot Description
Our bot makes completing tasks easy and inevitable. Our bot takes the uncertainty and stress out of organizing one's Schedule. The bot also holds users accountable by prompting users to complete certain tasks at various times. With the help of this bot, users can be reminded of upcoming tasks and assignments, as well as be able to submit assignments through third party access. This bot is great for and curated with group projects in mind. Each individual of a group will be aided in completing a task to contribute to the whole of the project. Deciding when and what to do for a particular project is made easy and instantly through the use of this bot.

This bot will be made available through discord, a platform that many are aware of and use on a daily basis. Discord promotes multiparty discussions, to which the bot will be implemented to help organize tasks and projects. This bot should automatically be made aware of a user's current tasks and assignments through third party apis, however any other information such as group members can be introduced to the bot through a chat interface. The bot can pick up on user behavior to delegate tasks in group behaviors and can be modified to suit most user needs through the chat interface.

# Use Cases
## Use Case 1: Getting a HW alert
- 1 Preconditions
  Must have discord bot in server
	Inputting an assignment and its due date
- 2 Main Flow
	User is prompted X amount of time ahead of the due date of the assignment. The user is also prompted x amount of times prior to the submission deadline.
- 3 Subflow
	[S1] User opens discord chat (server) 
  [S2] Bot will prompt user regarding assignment status
  [S3] Users can choose to interact with bot by updating status of assignment or submitting assignment.
  [S4]Bot responds with further action that must be taken or with submission complete status
- 4 Alternative Flows
 [E1] User has no current assignments 


## Use Case 2: Starting a group assignment
- 1 Preconditions
	Must have a server with all group members in it
	Must have the discord bot in the same server
- 2 Main Flow
	Group Members input assignment and responsibilities to which the bot organizes and assigns each member their tasks. The bot periodically sends group reminders as well as tagged reminders for each user to encourage progress.
- 3 Subflow
	[S1] Group member accessed discord chat
  [S2] Bot will prompt user regarding assignment progress and any personal tasks that need to be done 
  [S3] Users can choose to interact with bot by updating status of assignment or submitting assignment.
  [S4]Bot responds with further action that must be taken or with submission complete status
- 4 Alternative Flows
	[E1] Group has no current project 
  [E2] Group members manually choose tasks
  [E3] Group member has completed no work and the submission deadline for the assignment is particularly close


# Design Sketches
## Sequence flow chart
<img width="646" alt="Screen Shot 2022-02-26 at 5 23 29 PM" src="https://user-images.githubusercontent.com/81393135/155861999-17ecb1a0-cd12-4f80-b1dd-3780875f72c7.png">



## StoryBoard drawing
![IMG_8963](https://user-images.githubusercontent.com/81393135/155862035-a64b2c22-30a1-497b-a666-07c6ed58e893.jpg)


## Wireframe
<img width="494" alt="Screen Shot 2022-02-26 at 6 12 58 PM" src="https://user-images.githubusercontent.com/81393135/155862001-4585c900-47fc-46ae-9f6e-fa2372e9c39c.png">

# Architecture Design
<img width="757" alt="Screen Shot 2022-02-27 at 1 40 43 PM" src="https://user-images.githubusercontent.com/81393135/155895320-e6c8cac6-5f63-46a9-a210-64af8033b160.png">

