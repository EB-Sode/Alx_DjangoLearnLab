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
Tested Ok

created and input html templates and the static directory for css and javascript



