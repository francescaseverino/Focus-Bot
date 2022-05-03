# FocusBot
***Ali El Sayed, Nylayah Jones, Hyeonu Ju, Francesca Severino***
***“I pledge my honor that I have abided by the Steven’s Honor System”***
## Problem

FocusBot makes completing tasks easy and inevitable. Our bot takes the uncertainty and stress out of organizing one's Schedule. This bot also holds users accountable by prompting users to complete certain tasks at various times. With the help of this bot, users can be reminded of upcoming tasks and assignments, as well as be able to submit assignments through third party access. Deciding when and what to do for a particular project is made easy and instantly through the use of this bot.
This bot will be made available through discord, a platform that many are aware of and use on a daily basis. Discord promotes multiparty discussions, to which the bot will be implemented to help organize tasks and projects. This bot should automatically be made aware of a user's current tasks and assignments through third party apis, however any other information such as verbally assigned assignments can be introduced to the bot through a chat interface.
Using this bot solves the problem of not knowing what to do and when to do it, from a student’s perspective.

## Primary Features
- **update** - this command prompts the bot to update the database (sourced by google’s firestore console) with canvas assignments and courses. This update also includes manually input assignments not related to canvas assignments.

![update](https://user-images.githubusercontent.com/46319759/166458477-6222eaeb-4e3c-4756-9dca-dd41d56b9250.png)

- **get_assignment**- this command prompts the bot to show all assignments due in the set time range (the default is set to seven days). The assignments listed are limited to a single course, chosen by the user. If the ‘other’ labeled course is chosen, assignments manually input and not related to canvas assignments will be listed.

![getassignment](https://user-images.githubusercontent.com/46319759/166458542-96ce1ff5-a654-4e8b-97c0-04ce791febd6.png)

- **clear** - this command prompts the bot to clear all assignments stored in the firestore console, including manually input assignments. This would be useful during course changes or a new semester, for example.

![clear](https://user-images.githubusercontent.com/46319759/166458685-7c48a82e-f0b4-4e85-b8cc-2ae83cb13036.png)

- **get_course_assignment** - show assignments due in set range(default 7days) from a course chosen by user

![getcourseassignment](https://user-images.githubusercontent.com/46319759/166458754-d25dc4b0-7b38-4fb2-bb4e-4d21e446e4dd.png)
![getcourseassignment2](https://user-images.githubusercontent.com/46319759/166458725-66e21afb-df91-4044-b22e-e3681e0d1412.png)

- **set_getAssignmentRange** - this command sets a range for the bot to report assignments. The range is from one day to 365 days, and once set, the bot will only provide assignments within that range.

![setassignmentrange](https://user-images.githubusercontent.com/46319759/166458791-78031258-0771-4111-b1d9-56c178a59b91.png)

- **set_Assignment** - this command lets users inform the bot of assignments not listed in the users’ canvas courses. The bot will store the assignment in the firestore console alongside the stored canvas assignments and will report on user requests. Users also have the option to add assignments to existing canvas courses.

![setassigncourse](https://user-images.githubusercontent.com/46319759/166459583-f527eaca-a178-418c-9d8c-b58efb80eeff.png)
![setassigncourse2](https://user-images.githubusercontent.com/46319759/166459606-8b90bb57-b6ef-4e60-b21c-05730dcde363.png)
![firebbasecourse](https://user-images.githubusercontent.com/46319759/166459619-ba846e9c-c35c-4aa8-9478-f45bee83ded4.png)
![setassignnocourse](https://user-images.githubusercontent.com/46319759/166459630-b087951e-6935-4cf7-b60e-4d7ab45d0a1f.png)
![firebasenocourse](https://user-images.githubusercontent.com/46319759/166459638-25e98a0d-e25e-446c-9f4f-6b4ec6303499.png)


- **set timer**-

***Insert pic of timer function***


## Reflections
***Development Process***
Once the purpose of the bot and its functionality were decided, through discussion, the group was able to divide up the functionalities with the goal of working on the project using agile methodology. Even though the functions and tasks were separated by how much the user would interact with the bot, all tasks required each developer to interact with the bot as well as the firestore database. Progress on the bot was made while learning more about python functions, the discord api, and google’s firebase services. This situation allowed for all developers to increase their specific knowledge on the bot as well as overall knowledge of the resources used. Furthermore, the developers of this project were exposed to organizational practices such as scrum meetings and kanban boards to which were used to help the smooth progression of the project and collaboration efforts within the team. The use of these tools also promoted the organization of the project so much so that at any moment any team member could view the progress of the entire project as well as each individual member. This made finding issues with the project occur much earlier than usual.

***Project Overall***



## Limitations
The greatest limit to note would be the lack of technical knowledege. Much time was spent, for each team member, learning how to use and apply the tools used to make the FocusBot. Time was also a limiting factor as the more time we spent learning how to use the materials, the less time we had to implement them into the bot. We also had less time to customize the bot, as functionality was prioritized over aesthetic.



## Future Work
If the team were to continue pursuing this project there are a number of features we would update and implement. A key concept that would be explored is the user interface. The point of this bot is to decrease the effort on the user’s end, thus, we would aim to minimize the interactions between the bot and the user while maintaining or even increasing the impact of the bot. 
With the time constraint and lack of technical knowledge during this project, our team’s goal had to be amended. Originally we intended this bot to work for multiple individuals at once, however, it only works for one individual at a time. We would hope to make it so this bot would be functional for groups and would help to organize and manage teamwork and group based assignments.
