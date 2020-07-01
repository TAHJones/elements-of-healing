<img src="https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png" style="margin: 0;">

Welcome Thomas,

This is the Code Institute student template for Gitpod. We have preinstalled all of the tools you need to get started. You can safely delete this README.md file, or change it for your own project.

## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: *Make Public*,

Another blue button should appear to click: *Open Browser*.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: *Make Public*,

Another blue button should appear to click: *Open Browser*.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the backend lessons.

## Updates Since The Instructional Video

We continually tweak and adjust this template to help give you the best experience. Here are the updates since the original video was made:

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

--------

Happy coding!



## Deployment

## How to Deploy Project Using Gitpod

1. Navigate to the github repository located at https://github.com/TAHJones/homeopathy.

2. Create a Gitpod workspace using one of the following methods:

- Prefix the github repository URL in the address bar of your browser with https://gitpod.io/# e.g. https://gitpod.io/#https://github.com/TAHJones/homeopathy.

- If you have installed the Gitpod [extension](https://www.gitpod.io/docs/browser-extension/) for Chrome or Firefox click on the green 'Gitpod' button located on the top right of the github repository homepage.

3. If using Gitpod for the first time, you will have to authorize access to your GitHub account. This is necessary so you can access your data from within Gitpod.

4. Gitpod will create a workspace container for you in the cloud, containing a full Linux system. It will also clone the GitHub repository branch based on the GitHub page you were coming from.

## How to Create a Django Project

1. Click `Select Python interpreter` in the blue bar at the bottom of the page then select `Python 3.7.4 64-bit ('3.8.2': pyenv)` from the dropdown menu.

2. Open a terminal and run the following command to install the django framework:
```
pip3 install django
```

3. In the terminal run the following command to create a new project:
```
django-admin startproject your-project-name
```

4. To confirm the project has been installed correctly, navigate to the project folder and run the following command:
```
python3 manage.py runserver
```
5. Click `Open Browser` in the pop up window. The default Django page should appear with the message `The install worked successfully! Congratulations!`.

## How to Create a Django App

1. To create a new app in your Django project run the following command:
```
python3 manage.py startapp your-app-name
```

2. In the project folder open `settings.py` and add the new app to the `INSTALLED_APPS` list:
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'your-app-name'
]
```



pip3 install django

django-admin startproject homeopathy

python3 manage.py startapp homeopathy
