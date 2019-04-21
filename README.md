# Recipe Website

The brief of the project was to create a recipe book website with a simple frontend design. User needed to be able to view, add, delete and edit recipes easily as well as search by categories such as cuisine, allergies and main ingredients. 

## UX
As part of the UX a number of personas were created outlined below.

Persona –website guest
Be able to enter the website as a guest without having to sign up. The guest would only want to view the recipes on multiple platforms such as laptops, tablets and phones.

Persona – website registered user
Be able to sign up to the site with a unique username. Have the ability to view recipes as well as edit delete or add their own recipes. The user would also want their own recipes protected from being updated by other users.

Wire frames were also created in order to design the layout of the site and these can be found [here][1]

[1]: 
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
1.	Start Button:
    1. Click “Start Button”
    2. Game loads
2.	Check boxes highlight when clicked
    1.	Click all boxes
    2.	All boxes light up as expected
3.	Submit answer
    1.	Select correct answer and verify “answer correct” message appears
    2.	Select incorrect answer and verify “incorrect answer” message appear
4.	Next button
    1.	Get answer correct
    2.	Click next button
    3.	Verify sequence begins the same as before with one extra box highlighted.
5.	Restart 
    1.	Get answer incorrect
    2.	Click start button
    3.	Verify new sequence starts and only one box lights up
6.	Test different answer types
    1.	Too many boxes selected verify gives incorrect answer
    2.	Too few boxes selected verify gives incorrect answer
    3.	No boxes selected verify gives incorrect answer
    4.	Incorrect sequence selected verify gives incorrect answer
    5.	Correct sequence gives correct answer

7. link to browser test can be found [here][4]

[4]:https://github.com/cjmorgan1185/memoryGame/blob/master/design/testing.xlsx?raw=true

In relation to test 6, the first test showed that if you selected the correct sequence but added more boxes to you sequence it would still show answer correct. (i.e. sequence was red, red, blue, if user selected red, red, blue, blue, it would return correct answer message.) To fix this an extra condition was added to the answer if statement that took into account the size of the arrays
```JavaScript
    $("#answer-button").click(function() {
        for (y = 0; y < sequence.length; y++) {
            if (sequence[y] == answers[y] && sequence.length == answers.length {
                $("#next-button").show();
                $("#correct-message").show();
                $("#answer-button").hide();
                $(".box").hide();
            }
```

# Deployment
The website has been deployed to github pages and can be found [here][3]

[3]: https://cjmorgan1185.github.io/memoryGame/
# Credits
## Acknowledgements
•	Details of the original game called SIMON can be found [here][2]

[2]: https://en.wikipedia.org/wiki/Simon_(game)
