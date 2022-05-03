# Focus Bot
## Bot Summary
Our bot makes completing tasks easy and inevitable. Our bot takes the uncertainty and stress out of organizing one's Schedule. The bot also holds users accountable by prompting users to complete certain tasks at various times. With the help of this bot, users can be reminded of upcoming tasks and assignments, as well as be able to submit assignments through third party access. Deciding when and what to do for a particular project is made easy and instantly through the use of this bot.

This bot will be made available through discord, a platform that many are aware of and use on a daily basis. Discord promotes multiparty discussions, to which the bot will be implemented to help organize tasks and projects. This bot should automatically be made aware of a user's current tasks and assignments through third party apis, however any other information such as verbally assigned assignments can be introduced to the bot through a chat interface.

## How to Operate:
### For Developers: 
1. firebase account 
2. seviceAccountKey
- In order to execute the bot code, the developer must have access to the accountServiceKey.json for this project. Otherwise, the code can be run using a personal accountServiceKey which holds the private key provided by Google Services for a firebase project. This information can be input in a new .json file (with ‘serviceAccountKey’ as a prefix) which should automatically integrate with the bot code and file.
3. Discord Account	
- The developer must also have access to a Discord account to which they can provide a service key for a discord account for the bot to run in.
4. canvas api key
- The developer must also have canvas api key for the bot to connect to and run.
5. pip install
- must run: 
  - pip install firebase-admin 
  - pip install canvasapi 
  - pip install discord 
  -running these commands ensures that all the dependencies needed will be downloaded on the local environment.
6. Running in local environment  
- developers should be able to click 'run' to run the code locally so that the bot can function in a discord chat online.
### For Users:
- bot command = “f-”
#### Bot Commands

- **_clear_**   : Clears out all assignments + reupdates in database
- **_get_assignment_**   : List of all assignments due in set range (default 7 days)
- **_get_course_assignment_**   : Get assignment for a specific course
- **_help_**   : Shows list of commands
- **_remind_**   : Reminders for assignments in canvas
- **_set_assignment_**   : Add an assignment not on canvas
- **_set_assignmentRange_**   : Sets time range for retreiving assignments (default 7 days)
- **_set_reminder_**   : Adding reminder to a current assignment
- **_update_**   : Updates the list of assignments to databases (both canvas and manual assignemnts)
- **_view_reminders_**   : View list of current reminders
