CREATING THE NEW BLOG APP

I started with creating the project directory: djangoadmin startproject "project"
Inside the project I created the blog app: python manage.py startapp "app"
Opened the settings and added the app in installed apps
In settings.py I configured the database to be PostgreSQL
Created the a model for Post in the models.py and ran migrations
MIGRATION CHALLENGE
    -I ran into an error trying to migrate as I did not install any postgreSql driver. So I installed psycopg
    -Ran into another error because my database settings was incorrect. So i had to correct it
    -I had some challenges with using postgres and migrating it, 
    -I manually input the postgres user and then create a data base in the psql shell. 
finally ran migrations and migrated. no errors 
    - I also used pgAdmin to see and conrol my postgres
Tested Ok

created and input html templates and the static directory for css and javascript

Next is coding the Authentication, registeration and login/logout using django authentication views and forms in views.py
forms.py:
    In my forms.py I used UserCreationForm(the Inbuilt djg form)
    I added profile edit class to enable user profile edit
    I utilised a custom creation form to add an email field to the form
views.py: 
    imported the forms
    created views for both new form and edit profile. 
Urls.py: 
    set url for in-built Login/logout
    set url for custom profile registeration and profile edit
Settings.py:
    I ensured the login/logout redirect_url was set accordingly

ADDED VIEWs to the views.py

API CRUD(Not applicable in this app) views and HTML CRUD views
Also added templates for the crud display, still taking from the base.html

Tested all pages. Ok

ADDED MODELS FOR POST COMMENTS
-   created a form in forms.py to accept comments 
-   added CRUD abilities for the comments in views.py
-   link urls to the views
-   created updated the post_details template to add comments and added other templates for the comments. 
-   Had to watch out for the form creation and update the post view to accomodate comments form. 


ADDED TAG AND SEARCH FEATURES TO THE POST AND COMMENTS.
-   Creaeted a tag model with taggit (first install djangotaggit)
-   added tag features to Post form in forms.py 
-   Updated the detailsPostview detailscommentsview in views.py to accomodate tagging features
-   Also added FBV for tag and search(importing Q) and ofcourse, set up the url to direct. 
-   Created html templates for the tag list and search page.