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




