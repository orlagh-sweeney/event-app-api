# Event App API 
This project is a REST API for an event app.<br>
The API has been built using Django REST Framework and forms the back-end of [Connect Event App](https://github.com/orlagh-sweeney/connect-event-app), an event planning application.<br>
This project has been developed as my 5th Portfolio Project for my Diploma in Full Stack Software Development with Code Institute where I have undertaken a specialization in Advanced Frontend. <br>
The deployed API can be viewed here [drf-event-api](https://drf-event-api-8dabfe6ebdec.herokuapp.com/).

## Table of Contents
1. [Project Goals](#project-goals)
2. [Planning](#planning)
    - [User Stories](#user-stories)
    - [Methodology](#methodology)
3. [Models](#models)
4. [Technololgies Used](#technologies-used)
    - [Languages](#languages)
    - [Frameworks, Libraries and Programmes](#frameworks-libraries-and-programmes)
5. [Testing](#testing)
    - [Testing User Stories](#testing-user-stories)
    - [Code Validation](#code-validation)
    - [Manual Testing](#manual-testing)
    - [Bugs](#bugs)
6. [Deployment](#deployment)
7. [Credit](#credit)
    - [Code](#code)
    - [Media](#media)
8. [Acknowledgements](#acknowledgements)

## Project Goals
- Build a REST API using Django Rest Framework to be consumed by Connect Event App.
- Implement full CRUD functionality so users can modify data in the API.
- Implement authentification layers so data can only be modified by intended users/owners. 

## Planning
### User Stories
1. As a developer I want the functionality to to create, retrieve and update profile resources so that users can view and edit their own profiles.
2. As a developer I want the functionality to get, create, update, edit and delete event resources so that users interact with event data.
3. As a developer I want the functionality to get, create, and delete attending resources so that users can modify if they are attending an event or not.
4. As a developer I want the functionality to get, create, update, edit and delete comments so that users can modify comment data.
5. As a developer I want the functionality to get, create, and delete like resources so that users can like comments and interact with the like data
6. As a developer I want the functionality to store categories so that I can use categories in the Event and User Interest apps.
7. As a developer I want the functionality to store user interests so that I can customize their experience. 
8. As a developer I want the functionality to filter data so that I can customize the users experience. 

### Methodology
The project was planned and implemented following agile methodology principles. GitHub Projects was used to manage and document this process.

The GitHub project can be viewed here: [Event App API User Stories](https://github.com/users/orlagh-sweeney/projects/5)

User Stories contained a list of Acceptance Criteria and Tasks to support the development of the project.
Following MoSCoW Priortisation principles, each User Story was assigned a tag from one of the following:
- Must Have
- Should Have
- Could Have
- Won't Have

## Models
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

The below entity relationship diagram was created using [dbdigram](https://dbdiagram.io/home) and demonstrates the relationship between the models. <br> 
<image src="assets/readme/dbdiagram.png" width="600px"></image>

## Technologies Used
### Languages
- Python

### Frameworks, Libraries and Programmes
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
1. As a developer I want the functionality to create, retrieve and update profile resources so that users can view and edit their own profiles.
    - The API has a profiles app.
    - Profile owners can edit their profiles.
    - Authenticated users can view profiles. 
2. As a developer I want the functionality to to get, create, update, edit and delete event resources so that users interact with event data.
    - The API has an events app. 
    - This app provides functionality for users to create, edit, update and delete their own events. 
    - Any user can view events. 
3. As a developer I want the functionality to get, create, and delete attending resources so that users can modify if they are attending an event or not.
    - The API has an attendes app. 
    - This app provides functionality for authenticated users to create and delete attending resources.  
4. As a developer I want the functionality to get, create, update, edit and delete comments so that users can modify comment data.
    - The API has an comments app. 
    - This app provides functionality for users to create, edit, update and delete their own comments on an event. 
    - Any user can view comments.
5. As a developer I want the functionality to get, create, and delete like resources so that users can like comments and interact with the like data.
    - The API has a likes app. 
    - This app provides functionality for authenticated users to create and delete like resources for a comment.  
6. As a developer I want the functionality to store categories so that I can use categories in the Event and User Interest apps.
    - The API has an categories App.
    - The categories can be retrieved in the Event and User Interests apps. 
7. As a developer I want the functionality to store user interests so that I can customize their experience. 
    - The API has ann interest App.
    - The app stores interests for a particular user. 
    - Interests can be created and delete by authenticated users. 
8. As a developer I want the functionality to filter data so that I can customize the users experience. 
    - The API has a search function where users can search events by keyword.
    - Events can be filtered based on event type.
    - Events can also be filtered by events a user is attending or that a user has created. 

### Code Validation
The following validators were used to test the code:
- [pycodestlye](https://pypi.org/project/pycodestyle/): No errors were reported when passing the final python code through the validator.  <br>

### Manual Testing
The following manual tests were carried out:
#### Profiles App
TEST       | ENDPOINT | DESIRED RESULT          | PASS/FAIL |
---------- | -------- | ----------------------- | --------- |
List profiles | profiles/ GET  | Returns a list of profiles | PASS
Retrieve Profile | profiles/int:pk/ GET | Returns a single profile based on the id provided. Only authenticated users can view a profile by id | PASS
Update Profile | profiles/int:pk/ PUT | Only the profile owner can edit their profile. | PASS 
Cascasde | n/a | If a profile is deleted any associated events, attendees, comments, like and interests are also deleted | PASS

#### Event App
TEST       | ENDPOINT | DESIRED RESULT          | PASS/FAIL |
---------- | -------- | ----------------------- | --------- |
List Events | /events/ GET  | Returns a list of events | PASS
Create Event | /events/ POST | Authenticated users can create event objects. Unauthenticated users cannot. | PASS
Retrieve Event | /events/int:pk/ GET | Returns a single event object based on the id provided. | PASS
Update Event | /events/int:pk/ PUT | Only the event owner can edit an event object. | PASS
Delete Event | /events/int:pk/ DELETE | Only the event owner can edit delete an event object. | PASS
Invalid PK | /events/int:pk/ GET | If the event id is invalid a 404 error is returned | PASS
Cascasde | n/a | If an event is deleted any associated attendees and comments are also deleted | PASS

#### Attendee App
TEST       | ENDPOINT | DESIRED RESULT          | PASS/FAIL |
---------- | -------- | ----------------------- | --------- |
List Attendees | /attendees/ GET  | Returns a list of attendeess | PASS
Create Attendee | /attendees/ POST | Authenticated users can create an attendee object. Unauthenticated users cannot. | PASS
Retrieve Attendee | /attendees/int:pk/ GET | Returns a single attendee object based on the id provided. | PASS
Delete Attendee | /attendees/int:pk/ DELETE | Only the attendee object owner can delete an attendee object. | PASS

#### Categories App
TEST       | ENDPOINT | DESIRED RESULT          | PASS/FAIL |
---------- | -------- | ----------------------- | --------- |
Store categories | n/a  | Categories are stored in list. | PASS
Access categories | n/a  | Categories can be accessed by other apps. | PASS

#### Comment App
TEST       | ENDPOINT | DESIRED RESULT          | PASS/FAIL |
---------- | -------- | ----------------------- | --------- |
List Comments | /comments/ GET  | Returns a list of comments | PASS
Create Comment | /comments/ POST | Authenticated users can add comment objects. Unauthenticated users cannot. | PASS
Retrieve Comment | /comments/int:pk/ GET | Returns a single comment object based on the id provided. | PASS
Edit Comment | /comments/int:pk/ PUT | Only the comment owner can edit a comment object. | PASS
Delete Commnet | /comments/int:pk/ DELETE | Only the comment owner can edit a comment object. | PASS
Cascade | n/a | If a comment is deleted any associated likes are also deleted | PASS

#### Like App
TEST       | ENDPOINT | DESIRED RESULT          | PASS/FAIL |
---------- | -------- | ----------------------- | --------- |
List Likes | /likes/ GET  | Returns a list of likes | PASS
Create Like | /likes/ POST | Authenticated users can add like objects. Unauthenticated users cannot. | PASS
Retrieve Like | /likes/int:pk/ GET | Returns a single like object based on the id provided. | PASS
Delete Like | /likes/int:pk/ DELETE | Only the like owner can delete a like object. | PASS

#### Interest App
TEST       | ENDPOINT | DESIRED RESULT          | PASS/FAIL |
---------- | -------- | ----------------------- | --------- |
List Interests | /interests/ GET  | Returns a list of interests | PASS
Create Interest | /interests/ POST | Authenticated users can create interest objects. Unauthenticated users cannot. | PASS
Retrieve Interest | /interests/int:pk/ GET | Returns a single interest object based on the id provided. | PASS
Delete Interest | /interests/int:pk/ DELETE | Only the interest owner can delete an interest object. | PASS

### Bugs
1. Event Field Type:
In the Event model, the 'type' field was set as a Foreign Key relating to the Category model which did not allow the relevant choices to be added to the database. I changed the type field to a CharField and imported the Category model into the Event Model to resolve this issue.

2. Attending and Attended Count:
When calculating attending count and attended count I was using greater than and less than signs ('<' or '>') to check if date has passed or not. This is throwing an error in the code and not returning the desired output. Django documentation revealed the need to use 'lt' or 'gt' to fix this issue. 

3. Profiles:
If a user had not yet registered their interests the profiles page would not display. To fix this, in the profiles serialzier I updated get_user_interests to return None if there were no interests. 

## Deployment
The program was developed in Gitpod. It was then commited and pushed to GitHub.
The finished project was deployed in Heroku. 
Deployment to Heroku was completed using the following steps: 
1. Open and login to [Heroku](https://id.heroku.com/login).
2. From the dashboard, click 'New', then click 'Create new app' from the dropdown menu. 
3. Enter the App name, choose a region, then click 'Create app'.
4. Navigate to the 'Settings' tab.
5. Within 'Settings', navigate to 'Convig Vars'. Click 'Reveal Config Vars'.
6. Add config vars using the following 'KEY' and 'VALUE' pairs from env.py:
    - SECRET_KEY
    - DATABASE_URL
    - CLOUDINARY_URL
7. Add the following additional Config Vars:
    - ALLOWED_HOST: *set to deployed api URL
    - CLIENT_ORIGIN: *set to deployed front end URL
    - CLIENT_ORIGIN_DEV: *set to gitpod workspace url
    - DISABLE_COLLECT STATIC: 1
8. Navigate to the 'Deploy' tab. 
9. Within 'Deploy', navigate to 'Deployment method'. 
10. Click on 'GitHub'. Navigate to 'Connect to GitHub' and click 'Connect to GitHub' 
11. Within 'Connect to GitHub', use the search function to find the repository to be deployed. Click 'Connect'.
12. Navigate to either 'Automatic Deploys' or 'Manual Deploys' to choose which method to deploy the application.
13. Click on 'Enable Automatic Deploys' or 'Deploy Branch' respectively, depending on chosen method. 
14. Once the app is finished building, a message saying 'Your app was successfully deployed' will appear.
15. Click 'View' to see the deployed app. 

## Credit
### Code
- [Code Institute](https://codeinstitute.net/de/):
    - The Code Insitute Django REST Framework walkthrough project was referred to when setting up the project. Elements of the Code Institute project were used and adapted to suit this project.
- [Django REST Framework](https://www.django-rest-framework.org/): 
    - DRF documentation was referred to throughout development to educate myself and solve issues. 
- [Stackoverflow](https://stackoverflow.com/):
    - To access categories from the Category model in the type field in Event and Interest models I adapted a solution by [Linovia](https://stackoverflow.com/a/48090126).

### Media
Images were sourced from the following resources:
- [Pixabay](https://pixabay.com/):
    - Default user image is [blank-profile-picture-mystery-man-973460/](https://pixabay.com/vectors/blank-profile-picture-mystery-man-973460/) by [Stephaine Edwards](https://pixabay.com/users/wanderercreative-855399/)
- [Pexals](https://www.pexels.com/):
    - The default event image is [white-ball-838869/](https://www.pexels.com/photo/white-ball-838869/) by [Michael L.](https://www.pexels.com/@hiraeth/)

## Acknowledgements
- Thank you to my mentor Marcel for his feedback and suggestions at each stage of the project.
- Thank you to Code Institute for providing me with the tools and skills to complete this project
