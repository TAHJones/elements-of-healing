<h1 align="center">
  <a href="https://elements-of-healing.herokuapp.com/" target="_blank" style="width: 100%;">
    <img src="/media/logo.png" alt="elements of healing logo">
  </a>
</h1>

<img src="/media/homeopathy-montage--large.png" alt="elements of healing logo" style="width: 100%;">

## Introduction

[Elements of Healing](https://elements-of-healing.herokuapp.com/) is a website that is avaliable to the general public. It is designed to appeal to users with an interest in holistic medicine, specifically **homeopathy**. The site is designed to provide four core services:

1. To educate users who have an interest in holisitic medicine, but little or no knowledge of homeopathy with an understanding of it's basic principles e.g The law of similars.

2. To provide users who are interested in homeopathic treatment with an understanding of how a homeopathic consultation works, my background as a holistic healer and homeopathic qualifications. Also to provide these users with a means of contacting me should they have further questions about how a homeopathic consultation works.

3. To provide users who want a homeopathic treatment with a means to contact me should they have further questions, check my current avaliability or book a consultation.

4. To provide users (primarily existing homeopathy clients) with the ability to self-treat acute illnesses by purchasing homeopathic remedies & remedy kits from the online store.

## Table of Contents

1. [UX](#ux)
    - [User Requirements](#user-requirements)
    - [User Stories](#user-stories)
    - [Wireframes](#wireframes)
      - [Site Layout](#site-layout)
      - [How to Use the Site](#how-to-use-the-qc-metrics-analyser-website)
        - [As an Unregistered User](using-the-site-as-an-unregistered-user)
        - [As a Registered User](using-the-site-as-a-registered-user)
        - [As a Registered User with Admin Privileges](using-the-site-as-a-registered-user-with-admin-privileges)
2. [Main Features](#main-features)
     - [Main Page](#main-page)
     - [Login Page](#login-page)
     - [Signup Page](#signup-page)
     - [User Page](#user-page)
     - [Add Run Page](#add-run-page)
     - [Manage Runs Page](manage-runs-page)
     - [Admin or User Page](admin-or-user-page)
     - [Admin Page](#admin-page)
     - [Manage User Runs Page](#manage-user-runs-page)
     - [Delete Run Page](#delete-run-page)
     - [Update Run Page](#update-run-page)
     - [Manage Users Page](#manage-users-page)
     - [Delete User Page](#delete-user-page)
     - [Update User Page](#update-user-page)
     - [Logout Page](#logout-page)
     - [Permission Denied Page](#permission-denied-page)
     - [404 Error Page](#404-error-page)
     - [Features Left to Implement](#features-left-to-implement)
3. [Technologies Used](#technologies-used)
4. [Testing](#testing)
     - [Testing Stories](#testing-stories)
5. [Deployment](#deployment)
     - [How to Deploy Project Using Gitpod](#how-to-deploy-project-using-gitpod)
     - [How to Deploy Project Using Heroku](#how-to-deploy-project-using-heroku)
6. [Credits](#credits)
     - [Content](#content)
     - [Media](#media)
     - [Acknowledgements](#acknowledgements)

## Technologies Used

- HTML
- CSS
- [SCSS](https://sass-lang.com/)
- Javascript
- [jQuery](https://jquery.com/)
- [Bootstrap](https://getbootstrap.com/docs/)
- Python
- [Django](https://www.djangoproject.com/)
- [django-allauth](https://django-allauth.readthedocs.io/en/latest/)
- [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/)
- [pillow](https://pillow.readthedocs.io/en/stable/)
- [bootstrap-datepicker](https://getdatepicker.com/4/Installing/)
- [dj_database_url](https://pypi.org/project/psycopg2-binary/)
- [psycopg2-binary](https://pypi.org/project/dj-database-url/)
- [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- [django-storages](https://django-storages.readthedocs.io/en/latest/)

## Testing

### Testing Stories

- The following error message  `NameError at /checkout/ - name 'basket' is not defined` occurred during the final implementation of the checkout app. This was caused by the basket session variable being incorrectly named 'bag' in the checkout view.

- The potency value of purchased remedies failed to appear in either the shopping basket or on the checkout page. This was caused by the form value name for 'potency' being incorrectly named as 'product_potency' in the add_to_basket view.

- The error message `Field 'id' expected a number but got 'checkout'.` occurred when clicking on the 'Secure Checkout' button to purchase items in the shopping basket. This error occurred because of an error in the structuring of my url naming. The project level url was changed from '' to 'checkout/' and the checkout app level url was changed from 'checkout/wh' to 'wh/' to fix this problem.

- A problems occurred when customising the layout of my projects allauth forms. Forms with only a small amount of content would have a limited height which would break the pages layout. The footer section would be forced up the page and the page background image would be visible beneath it. To fix this problem the allauth base.html template was replaced with the form_base.html and message_base.html template. The message_base.html template would contain classnames that uses min-height with viewpoint units and the transform: translate property to center the page content. This prevented the limited content breaking the page layout.

- The following error message `NoReverseMatch at /accounts/logout/ , Reverse for 'home' not found. 'home' is not a valid view function or pattern name` occurred when the user clicks on the login button. This was fixed by changing the name for the root url from index to home.

- The following error message `AttributeError at /profile/, 'UserProfile' object has no attribute 'orders'` occurred when the current user clicks on the 'My Profile' link. This was fixed by adding the user_profile field to the Order model in the checkout app.

- The error message `NoReverseMatch at /add/, Reverse for 'add_product' with arguments '(43,)' not found. 1 pattern(s) tried: ['products/add/$']` occurred when a product was being deleted. This was caused by the incorrect view `view.update_product` being used in the app level url path. This was changed to the correct view `views.delete_product`.

- The error message `NoReverseMatch at /products/add/, Reverse for 'add_product' with arguments '(44,)' not found. 1 pattern(s) tried: ['products/add/$']` occurred because the redirect was pointing back to the add_product view when it should have been pointing to the product_detail view. 

- The error message `404 Not Found` occurred when remove link is clicked in shopping basket. This was fixed by changing the url variable from `/remove/${itemId}/` to `basket/remove/${itemId}/`.

- Conditional statement was failing to prevent the addition of more than one appointment to the basket. This was fixed by changing the if statement from `if quantity > 1` to `if item_id in list(basket.keys())`

- When navigating to the homepage a http 500 internal server error occurred with the following error message `KeyError at /, 'appointment_details'`. This error was traced back to the basket context.py file and was fixed by replacing `appointment_details = request.session['appointment_details]` with `appointment_details = request.session.get('appointment_details', {})`.

- When adding a product to the shopping basket a http 500 internal server error occurred with the following error message `KeyError at /basket/add/22/, 'appointment_details'`. This error was traced back to the add_to_basket view and was fixed by replacing `appointment_details = request.session['appointment_details]` with `appointment_details = request.session.get('appointment_details', {})`.

- Found a security problem with the shopping basket. The appointment form input field is designated as readonly to prevent more than one appointment being entered at a time. However this can be overridden by the client using the developer tools. This was fixed by resetting the appointment quantity to 1 in the checkout view.

## Deployment

In order to deploy this project you must first set up an account at [MongoDB Atlas](https://www.mongodb.com/cloud/atlas). Click [here](https://docs.atlas.mongodb.com/) for instructions on how to set up able Mongo Atlas account.

## How to Deploy Project Using Gitpod

1. Navigate to the github repository located at https://github.com/TAHJones/qc-metrics-analyser.

2. Create a Gitpod workspace using one of the following methods:

- Prefix the github repository URL in the address bar of your browser with https://gitpod.io/# e.g. https://gitpod.io/#https://github.com/TAHJones/qc-metrics-analyser

- If you have installed the Gitpod [extension](https://www.gitpod.io/docs/browser-extension/) for Chrome or Firefox click on the green 'Gitpod' button located on the top right of the github repository homepage.

3. If using Gitpod for the first time, you will have to authorize access to your GitHub account. This is necessary so you can access your data from within Gitpod.

4. Gitpod will create a workspace container for you in the cloud, containing a full Linux system. It will also clone the GitHub repository branch based on the GitHub page you were coming from.

5. Click 'Select Python interpreter' in the blue bar at the bottom of the page then select 'Python 3.7.4 64-bit ('3.7.4': pyenv) from the dropdown menu.

6. Open a terminal and run the following command to install project dependencies:
```
pip3 install -r requirements.txt
```
6. In the projects root directory create a file called `env.py`.

7. Inside the env.py file create SECRET_KEY, MONGO_DBNAME and MONGO_URI environment variables to link to your own mongodb database. Please make sure to call your database `sequencingMetricsDB`, with 2 collections called `users` and `seqMetCol`. You will find example json structures for these collections in the [schemas](https://github.com/TAHJones/qc-metrics-analyser/tree/master/schemas/) folder.

8. You can now run the application from the terminal using the following command:
```
python3 app.py
```

## How to Deploy Project Using Heroku

1. Create a `requirements.txt` file from the terminal using the command `pip3 freeze --local > requirements.txt`.

2. Create a `Procfile` from the terminal using the command `echo web: python app.py > Procfile`.

3. `git add` and `git commit` the new requirements and Procfile and then `git push` the project to GitHub.

3. Create a new app on the [Heroku website](https://dashboard.heroku.com/apps) by clicking the "New" button in your dashboard. Give it a name and set the region to Europe.

4. From the heroku dashboard of your new app, click on "Deploy" > "Deployment method" and select GitHub.

5. In the **App connected to GitHub** section confirm the heroku app is linked to the correct GitHub repository.

6. In the heroku dashboard for the application, click on "Settings" > "Reveal Config Vars".

7. Set the following config vars:

| Key | Value |
 --- | ---
DEBUG | FALSE
IP | 0.0.0.0
MONGO_URI | `mongodb+srv://<username>:<password>@<cluster_name>-kpu2s.mongodb.net/<database_name>?retryWrites=true&w=majority`
PORT | 5000
SECRET_KEY | `<your_secret_key>`

- To get you MONGO_URI read the MongoDB Atlas documentation [here](https://docs.atlas.mongodb.com/)

8. In the heroku dashboard, click "Deploy".

9. In the **Automatic Deploys** section click **Enable Automatic Deploys** to ensure your heroku app is automatically updated everytime your github repository is updated.

10. Click on the "Open App" button at the top of the page. The [Heroku website]( https://qc-metrics-analyser.herokuapp.com/) is now successfully deployed.


## Credits

### Content

The content of this site was written by myself. 

### Media

Images were obtained from:
- [Vecteezy](https://www.vecteezy.com/)
- [iconsplace](https://iconsplace.com/)
- [iconfinder](https://www.iconfinder.com/)
- [wikipedia](https://en.wikipedia.org/)

The site logo, banner and background image were either designed or photographed by myself.

Images were edited using [GIMP](https://www.gimp.org/).

The color scheme was designed by myself. It is inspired by nature and uses a lot of pastal green and yellow colors. It is designed to create a soft natural feel in line with the sites subject matter.

## Acknowledgements

- The project is inspired by my passion for homeopathy and holistic medicine. I hope to use this site to restart my Homeopathy practice to help support people during these difficult times.

- Special thanks to my Code Institute Mentor [Simen Daehlin](https://github.com/eventyret) for his coding expertise, patience and generosity with his time.








 **Next Generation Sequencing (NGS)** users using [Illuminas](https://www.illumina.com/index-d.html) sequencing chemistries and instruments. The site has been primarily designed for employees of the [Royal Marsden Hospital](https://www.royalmarsden.nhs.uk/) working within the [Molecular Diagnostics department](https://www.royalmarsden.nhs.uk/our-consultants-units-and-wards/clinical-departments/cancer-diagnostics). The department uses [Illumina's sequencing technologies](https://emea.illumina.com/science/technology/next-generation-sequencing/sequencing-technology.html?langsel=/gb/) to detect acquired genetic mutations in patients tumour samples. Patients found to have clinically actionable mutations can then be assigned to an appropriate clinical trial for treatment.

Each NGS sequencing run generates a set of **Sequencing Metrics** which can be used to assess the quality of the sequencing data produced. These sequencing metrics are useful for QC purposes. Firstly to ensure the quality of individual runs remain high and secondly to monitor the performance of the sequencing instruments over time.

The website records and displays four types of QC metric data:

1. **Yield** - Shows the expected number of nucleotide bases sequenced for the run. Typically this is measured in gigabases.

2. **Cluster Density** - Shows the number of clusters detected for the sequencing run.

3. **Clusters Passing Filter** - Shows the percentage of clusters passing the signal purity filter.

4. **Q30 Score**  - Shows the percentage of bases that have a Q-score above or equal to 30; Q30 is a probability of incorrect base calling of 1 in 1000. A quality score, or Q-score, is a prediction of the probability of an incorrect base call. A higher Q-score implies that a base call is higher quality and more likely to be correct.

In addition the website records the following related run information:

1. **Sequencing Chemistry** - The type of chemistry used can be Mid150, Mid300 or High300. This effects the amount of sequencing that can be performed and therefore the expected yield.

2. **Sequencing Experiment** - The type of experiment performed can be Capture, Exome or Genome. This determines the amount of sequencing required and effects the type of chemistry used and therefore the expected yield.

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
