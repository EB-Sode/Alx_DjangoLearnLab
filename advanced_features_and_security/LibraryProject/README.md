This is a new alx project on django and introduction to django
Upgrading my app with 

USING CUSTOM USER
Utilised the CustomUser model to create a custom user, 
- Import BaseUserManager and AbstractUser 
- Create a custom user Manager(CLASS) with BaseUserManager, defining user func and also defining super_user func
- Create a custom User class with AbstractUser, extending the custom user with roles 
Import Permission_required in views.py
- attached permission_required as per roles for different views
-Check urls.py to ensure all views are well directed
In settings.py
-Change AUTH_USER_MODEL to bookshelf.CustomUser
-set LOGIN_URL to bookshelf:login, LOGIN_REDIRECT_URL and LOGOUT_REDIRECT_URL

GROUP PERMISSIONS
- Opened signal.py to create group permissions to avoid direct query in apps.py
- Used Post_migrate decorator to migrate permission to apps.py
- Set permissions and created group to align with same
- In apps.py create func(ready) to import bookshelf.signal

SECURITY CONSIDERATIONS
- Switched DEBUG to true, added allowed host
- Enable XSS filtering in browser
- Prevent clickjacking by blocking iframes
- Prevent NIME-type sniffing
- Set CSRF cookie only over https
- Session cookie set only over https

- added csp to "installed_apps" and added csp middleware


