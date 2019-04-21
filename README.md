# Recipe Website

The brief of the project was to create a recipe book website with a simple frontend design. User needed to be able to view, add, delete and edit recipes easily as well as search by categories such as cuisine, allergies and main ingredients. 

## UX
As part of the UX a number of personas were created outlined below.

Persona –website guest
Be able to enter the website as a guest without having to sign up. The guest would only want to view the recipes on multiple platforms such as laptops, tablets and phones.

Persona – website registered user
Be able to sign up to the site with a unique username. Have the ability to view recipes as well as edit delete or add their own recipes. The user would also want their own recipes protected from being updated by other users.

Wire frames were also created in order to design the layout of the site and these can be found [here][1]

[1]: https://github.com/cjmorgan1185/cookbook/tree/master/UX
## Features

### Existing Features
•	Users can create a unique username
•	Users can only edit their own recipes
•	USers can search by Main ingredient, cuisine, Avoid Allergy and a secondary ingredient
### Features Left to Implement
•	Guest access
•	ability to add images
•	Passwords


### Technologies Used
*	JQuery
    * The project uses JQuery to simplify javascript functions and the game play. 
    * https://jquery.com/
* Materialize
    * Grid layout
    * Form and button creation
    * https://materializecss.com/
* MLAB
    * mongodb to store database
    * https://mlab.com/

# Testing
1.	New User
    1. Click “New User”
    2. Loads page to enter a new user name

2.	Check unique username
    1. added unique user
    2. opens correct page with “hello user” as expected

3.	Check unique username
    1. added a username already in use
    2. Got error message advising username in use

4.	User login
    1. added a username already in use
    2. opens correct page with “hello user” as expected

5.	Search button
    1. Click “Search”
    2. opens search page

6.	Add button
    1. Click “Add”
    2. opens search page

7.	Edit / Delete button
    1. Click “Edit / Delete”
    2. opens search page

8.	Logout button
    1. Click “Logout”
    2. opens search page
9.	Search function
    1. Searched 1 condition only
    2. Returns expected result

10.	Search function
    1. Searched 2 conditions only
    2. Returns expected result

11.	Search function
    1. Searched 3 conditions only
    2. Returns expected result

12.	Search function
    1. Searched 4 conditions
    2. Returns expected result

13.	Add function
    1. Added test recipe
    2. Returns expected result and recipe added to collection in mongodb

13.	Edit function
    1. Edited test recipe
    2. Returns expected result and recipe was updated in collection in mongodb

14.	Delete function
    1. Deleted test recipe
    2. Returns expected result and recipe was deleted from collection in mongodb


7. link to browser test can be found [here][4]

[4]: https://github.com/cjmorgan1185/cookbook/tree/master/testing

# Deployment
The website has been deployed to heroku and can be found [here][3]

[3]:

# Credits
## Acknowledgements
•	Initial recipes used on the webiste were taken from BBC good food website [here][2]

[2]: https://www.bbcgoodfood.com/
