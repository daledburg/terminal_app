# Terminal Application Assignment - Your Budget Buddy!

[App repository found here!](https://github.com/daledburg/terminal_application)

---
## Code styling guide/styling conventions
The styling guide that was followed when creating this application was PEP 8. This code relates directly to Python and provides coding conventions for the standard Python libraries.
[PEP 8 Stlye Guide](https://peps.python.org/pep-0008/)

---
## list of each feature and description
- use of variables and concept of variable scope
- loops and conditional control structures
- error handling
---
## Implementation plan
### Purpose of design

This application is being designed as a bash-terminal based application using python. The goal in creating this application is to provide a useful tool for users to be able to understand their financial situation and provide facts and figures to help them make smarter financial decisions. It has multiple features to provide an array of different kinds of information that the user may want, while also providing the ability for the user to create their own profile to store this information.

Develop an implementation plan which:
- outlines how each feature will be implemented and a checklist of tasks for each feature
- prioritise the implementation of different features, or checklist items within a feature
- provide a deadline, duration or other time indicator for each feature or checklist/checklist-item

Utilise a suitable project management platform to track this implementation plan.

Provide screenshots/images and/or a reference to an accessible project management platform used to track this implementation plan.
Your checklists for each feature should have at least 5 items.
## Features

### Login and store data relating to login
This application provides two different login methods when starting. First of all is 'Register' for new users to create their own unique Username and Password. The script accomplishes this through the use of dictionaries and the python package Pickle. To do this a file where the login information is opened, the new User is then prompted to create a Username and a Password. From there the script takes these values and assigns the username input as the key, and the password input as the value in a dictionary that is saved into the open file. This file can then be accessed in further uses of the application and these inputs can be accessed to check if the password entered corresponds to the valid value for password.

The username that is created is also used to save the budget data for later recall. for each of the descriptions and amounts of expenses as well as the income information a new file is created where a predetermined string is concatenated with the username information to create the new file. When a user logs in at a later date this information can be retrieved by re-opening the file name 

### Budget inputs budget and expenses


### graphical table to show information

### 

---

Help documentation
You must include:
- steps to install the application
- any dependencies required by the application to operate
- any system/hardware requirements
- how to use any command line arguments made for the application