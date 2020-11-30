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

- Tested appointment booking / email using the temporary email website `https://temp-mail.org` and my gmail account.

- Tested shopping basket & checkout pages using temporary email website `https://temp-mail.org` and Stripes payment page.


## Deployment

## How to Deploy Project Using Gitpod

1. Navigate to the github repository located at https://github.com/TAHJones/qc-metrics-analyser.

2. Create a Gitpod workspace using one of the following methods:

- Prefix the github repository URL in the address bar of your browser with https://gitpod.io/# e.g. https://gitpod.io/#https://github.com/TAHJones/qc-metrics-analyser

- If you have installed the Gitpod [extension](https://www.gitpod.io/docs/browser-extension/) for Chrome or Firefox click on the green 'Gitpod' button located on the top right of the github repository homepage.

3. If using Gitpod for the first time, you will have to authorize access to your GitHub account. This is necessary so you can access your data from within Gitpod.

4. Gitpod will create a workspace container for you in the cloud, containing a full Linux system. It will also clone the GitHub repository branch based on the GitHub page you were coming from.

5. Click 'Select Python interpreter' in the blue bar at the bottom of the page then select 'Python 3.8.3 64-bit ('3.8.3': pyenv) from the dropdown menu.

6. Open a terminal and run the following command to install project dependencies:
```
pip3 install -r requirements.txt
```
7. In the gitpod settings page enter the following environment variables:

| Key | Value |
 --- | ---
SECRET_KEY | `<your_secret_key>`
STRIPE_PUBLIC_KEY | `<your_public_key>`
STRIPE_SECRET_KEY | `<your_secret_key>`
STRIPE_WH_SECRET | `<your_secret_key>`
DEVELOPMENT | True

8. To migrate your models and generate your database use the following command:
```
python3 manage.py migrate
```

9. Use the following command create a superuser account to access the django admin panel and database:
```
python3 manage.py createsuperuser
```

10. You can now run the application locally from the terminal using the following command:
```
python3 manage.py runserver
```

11. Once the local server is running, add `/admin` to the end of the base url to access the admin panel login page.


## How to Deploy Project Using Heroku

1. Create a `requirements.txt` file from the terminal using the command `pip3 freeze --local > requirements.txt`.

2. Create a `Procfile` from the terminal using the command `echo web: gunicorn your-projects-name.wsgi:application > Procfile`.

3. `git add` and `git commit` the new requirements and Procfile and then `git push` the project to GitHub.

4. Create a new app on the [Heroku website](https://dashboard.heroku.com/apps) by clicking the "New" button in your dashboard. Give it a name and set the region to Europe.

5. Type the following command into the terminal: `heroku login -i` then enter your heroku username and password.

6. Disable the collection of static files during deployment using the following command:
```
heroku config:set DISABLE_COLLECTSTATIC=1 --app your-project-name
```

7. Initalise your heroku git remote using the following command:
```
heroku git:remote -a your-project-name
```

8. Deploy your project to heroku with the following command:
```
git push heroku master
```

9. From the heroku dashboard of your new app, click on "Deploy" > "Deployment method" and select GitHub.

10. In the **App connected to GitHub** section confirm the heroku app is linked to the correct GitHub repository.

11. In the heroku dashboard for the application, click on "Settings" > "Reveal Config Vars".

12. In the **Automatic Deploys** section click **Enable Automatic Deploys** to ensure your heroku app is automatically updated everytime your github repository is updated.

13. Set the following config vars:

| Key | Value |
 --- | ---
AWS_ACCESS_KEY_ID | `<your_secret_key>`
AWS_SECRET_ACCESS_KEY | `<your_secret_key>`
DATABASE_URL | `postgres://your_projects_database_url`
SECRET_KEY | `<your_secret_key>`
USE_AWS | True
STRIPE_PUBLIC_KEY | `<your_public_key>`
STRIPE_SECRET_KEY | `<your_secret_key>`
STRIPE_WH_SECRET | `<your_secret_key>`

14. In the heroku dashboard, click "Deploy".

15. Click on the "Open App" button at the top of the page. Your [Heroku website]( https://elementsofhealing.herokuapp.com/) is now successfully deployed.


## Credits

### Content

The content of this site was written by myself. 

### Media

Images were obtained from:
- [iconsplace](https://iconsplace.com/)
- [iconfinder](https://www.iconfinder.com/)
- [wikipedia](https://en.wikipedia.org/)

The site logo, banner and background image were either designed or photographed by myself.

Images were edited using [GIMP](https://www.gimp.org/).

The color scheme was designed by myself. It is inspired by nature and uses a lot of pastal green and yellow colors. It is designed to create a soft natural feel in line with the sites subject matter.

## Acknowledgements

- The project is inspired by my passion for homeopathy and holistic medicine. I hope to use this site to restart my Homeopathy practice to help support people during these difficult times.

- The shopping cart is largely based on the codeinstitute Boutique Ado django project and was modified by myself for the purposes of this site.








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
