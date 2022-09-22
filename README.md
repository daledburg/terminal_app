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


## Features

### Login and store data relating to login
This application provides two different login methods when starting. First of all is 'Register' for new users to create their own unique Username and Password. The script accomplishes this through the use of dictionaries and the python package Pickle. To do this a file where the login information is opened, the new User is then prompted to create a Username and a Password. From there the script takes these values and assigns the username input as the key, and the password input as the value in a dictionary that is saved into the open file. This file can then be accessed in further uses of the application and these inputs can be accessed to check if the password entered corresponds to the valid value for password.

The username that is created is then used to save the budget data for later recall. For the user data that is entered for descriptions and amounts of expenses as well as the income a new file is created. This new fileis named using a predetermined string that is concatenated with the username information to create the new file name. When a user logs in at a later date this information can be retrieved by re-opening the file name that has the corresponding username information in the file name and loading the information using pickle load.

### Budget inputs budget and expenses
The budget feature itself is the heart of the project. Once the user has created a profile, it begins asking questions, starting with the income of the user and then following on to the regular expenses that the user may have. Both the income and expenses also asks how often they are either paying it or are being paid so that the script can convert the values into comparable values. This aspect of the feature allows the application itself to do most of the heavy lifting for the data analysis. This feature showcases 

### graphical table to show information

### 

---

Help documentation
You must include:
- steps to install the application
- any dependencies required by the application to operate
- any system/hardware requirements
- how to use any command line arguments made for the application