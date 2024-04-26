# OPIUM - API

#### DEPLOYED BACKEND API HEROKU [LINK](https://drfa-api-0c6557539d5a.herokuapp.com/)

#### DEPLOYED FRONTEND HEROKU [LINK - LIVE SITE](https://opium-a765be924d82.herokuapp.com/)

#### DEPLOYED FRONTEND [REPOSITORY](https://github.com/BIBI78/opium)

## Table of Contents

- [User Stories](#user-stories "User Stories")
- [Database](#database "Database")
- [Testing](#testing "Testing")
  - [Validator Testing](#validator-testing "Validator Testing")
  - [Unfixed Bugs](#unfixed-bugs "Unfixed Bugs")
- [Technologies Used](#technologies-used "Technologies Used")
  - [Main Languages Used](#main-languages-used "Main Languages Used")
  - [Frameworks, Libraries & Programs Used](#frameworks-libraries-programs-used "Frameworks, Libraries & Programs Used")
- [Deployment](#deployment "Deployment")
- [Credits](#credits "Credits")
  - [Content](#content "Content")
  - [Media](#media "Media")

## User Stories:

All user stories can be found [HERE](static/userstories.md).

Links to the [GitHub Issues](https://github.com/BIBI78/opium/issues) f
[KANBAN board]().

## Database:

![SQL Database model](/static/images/.png)

## Testing:

### Validator Testing:

All files passed through [PEP8](http://pep8online.com/) without error.( Except for 1 file mentioned in the unfoxed bugs section)

![PEP8](/static/images/pep8.png)

### Manual Testing:

1. Manually verified each url path created works & opens without error.

2. Verified that the CRUD functionality for each app : Comments, Followers, Likes, Beats, Profiles, Feedback

- Checked by visiting each link.
- Creating new item for whatver app.
- Checking URL paths.(_very important for mp3_)
- Editing the item (not available for Likes, Followers or Rating)

3. Ensured search feature for Beats

4. Repeated these steps for the deployed API, and all pages.

- Needed to reset database everytime I edit my models, first I delete the **pycache** file in the migration folder of each app. Then clear my database on Elephant SQL then I run this command in the terminal:

```
python manage.py makemigrations
python manage.py migrate

```

- after I need to recreate the admin login by running this command:

```
python3 manage.py createsuperuser
```

- After all that I was able to create a beat through the deployed admin panel.

- Its important to note that I have to clear my cache after doing all this as well.

### Unfixed Bugs

- In the Beats serializer , I have to use " mp3_url = serializers.SerializerMethodField()" instead of the normal mp3 because of a problem with the prefix in Cloudinary. This bug is discussed further in my frontend READMEdoc [HERE](https://github.com/BIBI78/opium).
- I have chosen to rearrange my serializer file for the mp3 app because getting it to work properply already was a headache and I dont have time to fix it if any breaks.

## Technologies Used:

### Main Languages Used:

- Python

### Frameworks, Libraries & Programs Used:

- Django
- Django RestFramework
- Cloudinary
- Heroku
- Pillow
- Django Rest Auth
- PostgreSQL
- Cors Headers

## Deployment:

### Project creation:

#### (I followed these exact directions from this README doc [HERE](https://github.com/CluelessBiker/project5-drf-api))

1. Create the GitHub repository.
2. Create the project app on [Heroku](heroku.com).
3. Add the Postgres package to the Heroku app via the Resources tab.
4. Once the GitHub repository was launched on GitPod, installed the following packages using the `pip install` command:

```
'django<4'
dj3-cloudinary-storage
Pillow
djangorestframework
django-filter
dj-rest-auth
'dj-rest-auth[with_social]'
djangorestframework-simplejwt
dj_database_url psycopg2
gunicorn
django-cors-headers
```

5. Create the Django project with the following command:

```
django-admin startproject project_name .
```

6. Navigate back to [Heroku](heroku.com), and under the Settings tab, add the configvars:

- Key: SECRET_KEY | Value: hidden
- Key: CLOUDINARY_URL | Value: cloudinary://hidden
- Key: DISABLE_COLLECTSTATIC | Value: 1
- Key: ALLOWED_HOST | Value: api-app-name.herokuapp.com

7. Add two additional configvars after the ReactApp has been created:

- Key: CLIENT_ORIGIN | Value: https://react-app-name.herokuapp.com
- Key: CLIENT_ORIGIN_DEV | Value: https://gitpod-browser-link.ws-eu54.gitpod.io
- Make sure that the trailing slash `\` at the end of both links has been removed.

- (_IMPORTANT_) Gitpod updates the browser preview link every now and then. If this happpens the CLIENT_ORIGIN_DEV value needs to be updated.

8. Creat the env.py file, and add the following variables. (_The value for DATABASE_URL comes from the Heroku configvars in the previous step_):

```
import os

os.environ['CLOUDINARY_URL'] = 'cloudinary://hidden'
os.environ['DEV'] = '1'
os.environ['SECRET_KEY'] = 'hidden'
os.environ['DATABASE_URL'] = 'postgres://hidden'
```

### In settings.py:

<!-- For reference, refer to: [DRF-API walkthrough settings.py](https://github.com/Code-Institute-Solutions/drf-api/blob/2c0931a2b569704f96c646555b0bee2a4d883f01/drf_api/settings.py) -->

9. Add the following to INSTALLED_APPS:

```
'cloudinary_storage',
'django.contrib.staticfiles',
'cloudinary',
'rest_framework',
'django_filters',
'rest_framework.authtoken',
'dj_rest_auth',
'django.contrib.sites',
'allauth',
'allauth.account',
'allauth.socialaccount',
'dj_rest_auth.registration',
'corsheaders',
```

10. Import the database, the regular expression module & the env.py

```
import dj_database_url
import re
import os
if os.path.exists('env.py')
    import env
```

11. Below the import statements, add the following variable for Cloudinary:

```
CLOUDINARY_STORAGE = {
    'CLOUDINARY_URL': os.environ.ger('CLOUDINARY_URL')
}

MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinartStorage'
```

- Below INSTALLED_APPS, set site ID:

```
SITE_ID = 1
```

12. Below BASE_DIR, create the REST_FRAMEWORK, and include page pagination to improve app loading times, pagination count, and date/time format:

```
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [(
        'rest_framework.authentication.SessionAuthentication'
        if 'DEV' in os.environ
        else 'dj_rest_auth.jwt_auth.JWTCookieAuthentication'
    )],
    'DEFAULT_PAGINATION_CLASS':
        'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DATETIME_FORMAT': '%d %b %Y',
}
```

13. Set the default renderer to JSON:

```
if 'DEV' not in os.environ:
    REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = [
        'rest_framework.renderers.JSONRenderer',
    ]
```

14. Beneath that, added the following:

```
REST_USE_JWT = True
JWT_AUTH_SECURE = True
JWT_AUTH_COOKIE = 'my-app-auth'
JWT_AUTH_REFRESH_COOKIE = 'my-refresh-token'
JWT_AUTH_SAMESITE = 'None'
```

15. Then add:

```
REST_AUTH_SERIALIZERS = {
    'USER_DETAILS_SERIALIZER': 'project_name.serializers.CurrentUserSerializer'
}
```

16. Updated DEBUG variable to:

```
DEBUG = 'DEV' in os.environ
```

17. Updated the DATABASES variable to:

```
DATABASES = {
    'default': ({
       'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    } if 'DEV' in os.environ else dj_database_url.parse(
        os.environ.get('DATABASE_URL')
    )
    )
}
```

18. Added the Heroku app to the ALLOWED_HOSTS variable:

```
os.environ.get('ALLOWED_HOST'),
'localhost',
```

19. Below ALLOWED_HOST, added the CORS_ALLOWED variable as shown in [DRF-API walkthrough](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+DRF+2021_T1/courseware/a6250c9e9b284dbf99e53ac8e8b68d3e/0c9a4768eea44c38b06d6474ad21cf75/?child=first):

```
if 'CLIENT_ORIGIN' in os.environ:
    CORS_ALLOWED_ORIGINS = [
        os.environ.get('CLIENT_ORIGIN')
    ]

if 'CLIENT_ORIGIN_DEV' in os.environ:
    extracted_url = re.match(r'^.+-', os.environ.get('CLIENT_ORIGIN_DEV', ''), re.IGNORECASE).group(0)
    CORS_ALLOWED_ORIGIN_REGEXES = [
        rf"{extracted_url}(eu|us)\d+\w\.gitpod\.io$",
    ]
```

20. Also added to the top of MIDDLEWARE:

```
'corsheaders.middleware.CorsMiddleware',
```

- During a deployment issue, it was suggested by a fellow student, Johan, to add the following lines of code below CORS_ALLOW_CREDENTIALS:

```
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_HEADERS = list(default_headers)
CORS_ALLOW_METHODS = list(default_methods)
CSRF_TRUSTED_ORIGINS = [os.environ.get(
    'CLIENT_ORIGIN_DEV', 'CLIENT_ORIGIN',
)]
```

- In addition, Johan also suggested to add the following import statement at the top of the settings.py file:

```
from corsheaders.defaults import default_headers, default_methods
```

### Final requirements:

21. Created a Procfile, & added the following two lines:

```
release: python manage.py makemigrations && python manage.py migrate
web: gunicorn project_name.wsgi
```

22. Migrated the database:

```
python manage.py makemigrations
python manage.py migrate
```

23. Froze requirements:

```
pip3 freeze --local > requirements.txt
```

24. Added, committed & pushed the changes to GitHub
25. Navigate back to heroku, and under the ‘Deploy’ tab, connect the GitHub repository.
26. Deployed the branch.

### Deploy to ElephantSQL:

-

## CREDITS:

### Content:

- I followed the exact steps described in the CI walkrough project.
- The ratings app outline comes from this project [HERE](https://github.com/andreas-ka/explore-sthlm-api), but I had to edit and downgrade the package to be able to deploy it in the frontend.
- All my thanks to my mentor [Lauren](https://github.com/CluelessBiker)
- I used [ChatGPT](https://chat.openai.com/) To spell check and correct grammer throughout this project and to help add notes to the code.

