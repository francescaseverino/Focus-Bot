# FocusBot
***Ali El Sayed, Nylayah Jones, Hyeonu Ju, Francesca Severino***
***“I pledge my honor that I have abided by the Steven’s Honor System”***
## Problem

FocusBot makes completing tasks easy and inevitable. Our bot takes the uncertainty and stress out of organizing one's Schedule. This bot also holds users accountable by prompting users to complete certain tasks at various times. With the help of this bot, users can be reminded of upcoming tasks and assignments, as well as be able to submit assignments through third party access. Deciding when and what to do for a particular project is made easy and instantly through the use of this bot.
This bot will be made available through discord, a platform that many are aware of and use on a daily basis. Discord promotes multiparty discussions, to which the bot will be implemented to help organize tasks and projects. This bot should automatically be made aware of a user's current tasks and assignments through third party apis, however any other information such as verbally assigned assignments can be introduced to the bot through a chat interface.
Using this bot solves the problem of not knowing what to do and when to do it, from a student’s perspective.

## Primary Features

- **clear** - this command prompts the bot to clear all assignments stored in the firestore console, including manually input assignments. This would be useful during course changes or a new semester, for example. In the image below, it shows how all the data was cleared in the firebase and using the other commands to display this.

  <img width="711" alt="Screen Shot 2022-05-09 at 15 29 44" src="https://user-images.githubusercontent.com/71108842/167483506-57951e1e-30ac-4cbe-8930-3fdc928bf11e.png">



- **delete_reminders** - this command prompts the bot to delete all reminders stored in the firebase console, both reminders from the manual input and canvas. This would be useful if the user was to reset the reminders and a fresh start.

  <img width="645" alt="Screen Shot 2022-05-09 at 15 19 11" src="https://user-images.githubusercontent.com/71108842/167481960-efcfc956-1e9e-45b8-9343-786fb3e60b34.png">



- **get_assignment** - this command prompts the bot to show all assignments due in the set time range (the default is set to seven days). The assignments listed are limited to a single course, chosen by the user. If the ‘other’ labeled course is chosen, assignments manually input and not related to canvas assignments will be listed.

  <img width="503" alt="Screen Shot 2022-05-09 at 15 14 55" src="https://user-images.githubusercontent.com/71108842/167481300-04832738-3263-4773-805c-c704906d8c19.png">



- **get_course_assignment** - this command prompts the bot to show assignments due in set range (default 7days) from a course chosen by user. This helps keep the user from getting overwhelmed with all their assignments throughout the semester.

  <img width="569" alt="Screen Shot 2022-05-09 at 15 16 04" src="https://user-images.githubusercontent.com/71108842/167481489-40b1f207-bd21-401f-a7e0-1901e0c2d59d.png">



- **help** - this command prompts the bot to show a list of all the commands available on the bot.

  <img width="893" alt="Screen Shot 2022-05-09 at 15 11 59" src="https://user-images.githubusercontent.com/71108842/167480764-04e3bcac-4721-45d4-8234-06936867ab14.png">



- **remind** - this command prompts the bot to show the automate reminders for assignments on canvas. This allows there to be a separate list of reminders specifically for assignments on canvas.

  <img width="676" alt="Screen Shot 2022-05-09 at 15 17 31" src="https://user-images.githubusercontent.com/71108842/167481719-68e510be-f79b-4f52-875c-5c6b563bc2ce.png">



- **set_assignment** - this command lets users inform the bot of assignments not listed in the users’ canvas courses. The bot will store the assignment in the firestore console alongside the stored canvas assignments and will report on user requests. Users also have the option to add assignments to existing canvas courses.

  <img width="645" alt="Screen Shot 2022-05-09 at 15 24 33" src="https://user-images.githubusercontent.com/71108842/167482725-23bc4f68-2458-4b5a-a9da-0f28506ccb18.png">



- **set_getAssignmentRange** - this command sets a range for the bot to report assignments. The range is from one day to 365 days, and once set, the bot will only provide assignments within that range.

  <img width="677" alt="Screen Shot 2022-05-09 at 15 13 53" src="https://user-images.githubusercontent.com/71108842/167481116-5b230264-94f2-4cfe-bf2c-7cb72d318f81.png">



- **set_reminder** - this command sets a reminder to a current assignment. While the canvas assignments have a pre-set reminder already, the user can still set a reminder for an assignment, even on canvas, for an earlier day or earlier then the time set beforehand.

  <img width="685" alt="Screen Shot 2022-05-09 at 15 16 43" src="https://user-images.githubusercontent.com/71108842/167481604-f930a92f-b700-466e-aca5-b64e47c42284.png">



- **update** - this command prompts the bot to update the database (sourced by google’s firestore console) with canvas assignments and courses. This update also includes manually input assignments not related to canvas assignments.

  <img width="893" alt="Screen Shot 2022-05-09 at 15 12 46" src="https://user-images.githubusercontent.com/71108842/167480905-7c808b11-e6e5-456a-870b-75e9da98f7cc.png">



- **view_reminders** - this command prompts the bot to display the list of all the current reminders, both manual and automate. This helps organizing the user to have the abiltiy to view all the reminders, grasping an overview of all assignments coming up for time mangement.

  <img width="676" alt="Screen Shot 2022-05-09 at 15 18 23" src="https://user-images.githubusercontent.com/71108842/167481846-bdcec344-0a6f-4e4e-b5ad-796ad102a72f.png">




## Reflections

***Development Process***

Once the purpose of the bot and its functionality were decided, through discussion, the group was able to divide up the functionalities with the goal of working on the project using agile methodology. Even though the functions and tasks were separated by how much the user would interact with the bot, all tasks required each developer to interact with the bot as well as the firestore database. Progress on the bot was made while learning more about python functions, the discord api, and google’s firebase services. This situation allowed for all developers to increase their specific knowledge on the bot as well as overall knowledge of the resources used. Furthermore, the developers of this project were exposed to organizational practices such as scrum meetings and kanban boards to which were used to help the smooth progression of the project and collaboration efforts within the team. The use of these tools also promoted the organization of the project so much so that at any moment any team member could view the progress of the entire project as well as each individual member. This made finding issues with the project occur much earlier than usual.

***Project Overall***

The project overall was a great learning experiance for each team member. From the discord API to project mangement, the team was able to develop skills that would help with future sucess. We are able to establish communication among each team member, creating great team working enviroment. For instance, the scrum meetings and kanban boards really helped with origanzation of the development process, elements of project development that the team members were not exposed to prior. 


## Limitations

The greatest limit to note would be the lack of technical knowledege. Much time was spent, for each team member, learning how to use and apply the tools used to make the FocusBot. Time was also a limiting factor as the more time we spent learning how to use the materials, the less time we had to implement them into the bot. We also had less time to customize the bot, as functionality was prioritized over aesthetic.



## Future Work

If the team were to continue pursuing this project there are a number of features we would update and implement. A key concept that would be explored is the user interface. The point of this bot is to decrease the effort on the user’s end, thus, we would aim to minimize the interactions between the bot and the user while maintaining or even increasing the impact of the bot. 
With the time constraint and lack of technical knowledge during this project, our team’s goal had to be amended. Originally we intended this bot to work for multiple individuals at once, however, it only works for one individual at a time. We would hope to make it so this bot would be functional for groups and would help to organize and manage teamwork and group based assignments.
