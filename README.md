<h1 align="center">Grid Battlefield (a battleships game)</h1>

The pencil and paper game implementation in a terminal application.

Battleships is a turn based, two player game, set in a indexed finite grid space. This app allow you to play against the computer.

As a child I played this game with my father with somewhat different setup, called Battleplanes. My ultimate goal is to have the well known Battleships game and the derived Battleplanes game mode implemented in the application.

[View the live project here.](https://grid-battle.herokuapp.com/)

![Responsive Design from http://ami.responsivedesign.is/]()

# Table of content

+ [Gameplay instructions](#gameplay)
+ [Features](#features)
+ [Design Process](#design-process)
+ [Technologies used](#technologies-used)
+ [Testing](#testing)
+ [Deployment](#deployment)
+ [Credits](#credits)

***

<h2 id="gameplay">How to play</h2>
<a href="#table-of-content">Go back <span style="font-size: 1.3em">🔝</span></a>

## Features
<a href="#table-of-content">Go back <span style="font-size: 1.3em">🔝</span></a>

- Main menu

- Battleships game

- High Scores

- Game Rules

- Battleplanes game mode

## Design Process

### Base Plan

-   #### User Stories
    1.  As a new user I want to get a general unambiguous read of the game rules.
    1.  As a user I want to be able to play a game, with clear responses of the game state.
    1.  As a user I want to review other players achieved top scores.

-   #### Application Aim
    -   To communicate the game course clearly.
    -   To give the option for the player to save an achieved high score.
    -   To allow the user to have an unambiguous, error free, gameplay experience.
-   #### Roadmap
    1.  *Menu* - main menu with multiple options
    1.  *Battleships game* - the main game implementation
    1.  *High scores* - stored in a local json
    1.  *Game rules* - description of
    1.  *Battleplanes game mode* - the special game
    1.  Testing

### Flowchart

To have an understanding of the required step for the application, I have created the following flowchart using draw.io.

![Flowchart](readme/diagrams/flowchart.drawio.svg)

### Data Model

![Data Model](readme/diagrams/data-model.drawio.svg)

## Technologies Used
<a href="#table-of-content">Go back <span style="font-size: 1.3em">🔝</span></a>

### Languages Used

-   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Frameworks, Libraries & Programs Used

1. [Git](https://git-scm.com/)
1. [GitHub](https://github.com/)
1. [draw.io](https://www.diagrams.net/)

## Testing
<a href="#table-of-content">Go back <span style="font-size: 1.3em">🔝</span></a>

### Validators Testing
-   [W3C Markup Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)
-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)
-   [Python](http://pep8online.com/)

### Testing User Stories

### Further Testing

-   ~~Friends and family members were asked to review the app~~

### Known Bugs

-   ?

## Deployment
<a href="#table-of-content">Go back <span style="font-size: 1.3em">🔝</span></a>

The project was deployed using Code Institute's mock terminal for Heroku.

-   Steps for deployment:
    -   Fork or clone this repository
    -   Create a new Heroku app
    -   In the app settings:
        -   Add a config var of `PORT`:`8000`
        -   Set the buildpacks to `Python` and `NodeJS` in that order
    -   Link the Heroku app to the forked repository
    -   Manually **Deploy**

### Making a Local Clone

> *Review* to make the whole project locally deployable
Requires Python 3 installed in local environment, to run the game in a terminal

-   Fork or clone this repository
-   Navigate to folder in a terminal
-   Run the following command `python3 run.py`

## Credits
<a href="#table-of-content">Go back <span style="font-size: 1.3em">🔝</span></a>

### Code

-   [Python Docs](https://docs.python.org/3.8/)
-   [Markdown Guide](https://www.markdownguide.org/cheat-sheet/)

-   [How to clear screen with Python](https://stackoverflow.com/questions/2084508/clear-terminal-in-python#answer-36941376)

### Acknowledgements

-   Code Institute for the deployment terminal
-   [Pen and paper](http://www.papg.com/show?1TMC) website for the game rules reference
-   README.md structure inspired by several Code Institute's samples