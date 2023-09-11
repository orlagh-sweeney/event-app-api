# The Big Review
This project is a REST API for an event app.<br>
The API has been built using Django REST Framework and forms the back-end of XX, an event planning application.<br>
This project has been developed as my 5th Portfolio Project for my Diploma in Full Stack Software Development with Code Institute where I have undertaken a specialization in Advanced Frontend. 

## Table of Contents
1. [Project Goal](#project-goals)
2. [Planning](#planning)
    - [Methodology](#methodology)
    - [Models](#models)
3. [Features](#features)

4. [Technololgies Used](#technologies-used)
    - [Languages](#languages)
    - [Frameworks, Libraries and Programmes](#frameworks-libraries-and-programmes)
5. [Testing](#testing)
    - [Testing User Stories](#testing-user-stories)
    - [Code Validation](#code-validation)
    - [Automated Tests](#automated-tests)
    - [Feature Testing](#manual-feature-testing)
    - [Bugs](#bugs)
6. [Deployment](#deployment)
7. [Credit](#credit)
    - [Content](#content)
    - [Media](#media)
    - [Code](#code)
8. [Acknowledgements](#acknowledgements)

## Project Goals


## Planning
### Methodology
### Models
This project uses 7 models:
1. Profile model:
    - This has a one-to-one relationship with the Django User Model.
    - When a User is created a Profile is automatically created for the new User. 
2. Event model:
    - Stores data about an event. 
    - owner is a foreign key connecting to the User model.
    - type categories are retrieved from the Cateogry model
3. Attendee model:
    - Stores data about an Event that a User is attending.
    - owner is a foreign key connecting to the User model.
    - event is a foreign key connecting to the Event model.
4. Categories model:
    - Stores a list of categories to be used in the Event model type field and the Interest model type field. 
5. Comment model:
    - Stores data about a Comment a User left on an event.
    - owner is a foreign key connecting to the User model.
    - event is a foreign key connecting to the Event model.
6. Like model:
    - Stores data about likes on a comment.
    - owner is a foreign key connecting to the User model.
    - comment is a foreign key connecting to the Comment model.
7. Interest model:
    - Records profiles linked to a specific category aka interest.
    - owner is a foreign key connecting to the User model.
    - type categories are retrieved from the Cateogry model.

The below entity relationship diagram was created using [dbdigram](https://dbdiagram.io/home) and demonstrates the relationship between the models.

## Features


## Technologies Used
### Languages
- Python

### Frameworks, Libraries and Programmes- [Balsamiq](https://balsamiq.com/): this was used to create wireframes in the planning stage of the project. 
- [Django](https://www.djangoproject.com/): this was the MVC web framework used.
- [Django REST Framework](https://www.django-rest-framework.org/): this was used as the framework to build the REST API.
- [Cloudinary](https://cloudinary.com/): this was used to store static and media files.
- [Gitpod](https://www.gitpod.io/): this was used to write, commit and to push the code to Github. 
- [Github](https://github.com/): this was used for version control. 
- [Heroku](https://dashboard.heroku.com/login): this was used to host and deploy the finished project.
- [ElephantSQL](https://www.elephantsql.com/): this is the SQL database used in production.
- [SQLite](https://www.sqlite.org/index.html): this is the databased used in development. 
- [CI Python Linter](https://pep8ci.herokuapp.com/): this was used to validate python code.
- [pycodestlye](https://pypi.org/project/pycodestyle/): this was used to validate python code.

A complete list of packages and dependencies can be viewed in the requirements.txt file. 

## Testing
### Testing User Stories
### Code Validation
### Automated Tests
### Manual Feature Testing
### Bugs

## Deployment

## Credit
### Content
### Media
### Code

## Acknowledgements

