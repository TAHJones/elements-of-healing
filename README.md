<h1 align="center">
  <a href="https://elements-of-healing.herokuapp.com/" target="_blank" style="width: 100%;">
    <img src="/media/logo.png" alt="elements of healing logo">
  </a>
</h1>

<img src="/media/homeopathy-montage--large.png" alt="elements of healing logo" style="width: 100%;">

## Introduction

[Elements of Healing](https://elements-of-healing.herokuapp.com/) is a website that is avaliable to the general public. It is designed to appeal to users seeking homeopathic treatment or who have a general interest in holistic medicine and more specifically **homeopathic treatment**. The site is designed to provide four core services:

1. To educate users who have an interest in holisitic medicine, but little or no knowledge of homeopathy, with an understanding of it's health benefits and key healing principles e.g The law of similars.

2. To provide users who are interested in homeopathic treatment with an understanding of how a homeopathic consultation works, my background as a holistic healer and homeopathic qualifications. Also to provide these users with a means of contacting me should they have further questions about homeopathy, my homeopathic practice or how a homeopathic consultation works.

3. To provide new/regular clients who want a homeopathic treatment with a means to provisionally book a homeopathic consultation with myself.

4. To provide users (primarily existing homeopathy clients) with the ability to self-treat acute illnesses by purchasing homeopathic remedies and remedy kits from the online store.


## Table of Contents

1. [UX](#ux)
    - [User Requirements](#user-requirements)
    - [User Stories](#user-stories)
    - [Wireframes](#wireframes)
      - [Site Layout](#site-layout)
      - [How to Use the Site](#how-to-use-the-elements-of-healing-website)
        - [As an Unregistered User](#using-the-site-as-an-unregistered-user)
        - [As a Registered User](#using-the-site-as-a-registered-user)
        - [As a Registered User with Admin Privileges](#using-the-site-as-a-registered-user-with-admin-privileges)
2. [Main Features](#main-features)
     - [Home Page](#home-page)
     - [Homeopathy Page](#homeopathy-page)
     - [Consultation Page](#homeopathy-page)
     - [About Page](#about-page)
     - [Contact Page](#contact-page)
     - [Login Page](#login-page)
     - [Signup Page](#signup-page)
     - [Signout Page](#signout-page)
     - [Products Page](#products-page)
     - [Product Page](#product-page)
     - [Appointments Page](#appointment-page)
     - [Shopping Basket Page](#shopping-basket-page)
     - [Checkout Page](#checkout-page)
     - [Checkout Success Page](#checkout-success-page)
     - [Profile Page](#profile-page)
     - [Calendar Page](#calendar-page)
     - [Appointment Details Page](#appointment-details-page)
     - [Search Form](#search-form)
     - [Product Management Page](#product-management-page)
     - [Features Left to Implement](#features-left-to-implement)
3. [Technologies Used](#technologies-used)
4. [Testing](#testing)
     - [Testing Stories](#testing-stories)
5. [Deployment](#deployment)
     - [How to Deploy Project Using Gitpod](#how-to-deploy-project-using-gitpod)
     - [How to Deploy Project Using Heroku](#how-to-deploy-project-using-heroku)
     - [How to add Google Calendar API](#how-to-add-google-calendar-api)
     - [How to add AWS S3 Bucket](#how-to-add-aws-s3-bucket)
6. [Credits](#credits)
     - [Content](#content)
     - [Media](#media)
     - [Acknowledgements](#acknowledgements)


## UX

This site is designed to be used by the general public. It is specifically designed to appeal to users with an interest in holistic medicine, specifically **homeopathy**. The site is also designed to allow new & existing homeopathy clients to book appointments and purchase remedies and remedy kits.

There are three types of user with three different levels of access to the Elements of Healing website:

- **Unregistered Users** - Users of the site that don't have a user account, who have little or no knowledge of Homeopathy but are curious and wish to understanding it's health benefits and basic healing principles. Unregistered users can contact the site owner via the contact form should they require any further information about homeopathy or homeopathic treatment.

- **Registered Users** - Users of the site that are new/regular homeopathy clients who have created a user account, who can book appointments and purchase remedies and remedy kits.

- **Registered Users with Admin Privileges** - Users of the site with a user account with admin privileges, who are able to view, edit or delete appointment information for other registered users. They are also able to view, edit or delete user accounts.


### User Requirements

The user requirements for Elements of Healing are as follows:

- The site must be easy and intuitive to use.

- The site must be designed to have a soft natural feel in line with the sites subject matter.

- The site must provide basic information about homeopathy's health benefits and basic healing principles.

- The site must provide the user with basic information about how a homeopathy consultation works and what to expect during the process.

- The site must provide the user with basic information about myself, my background and my homeopathic qualifications.

- The site must provide the user with ability to contact me for more information about homeopathy or homeopathic treatment via the sites contact form.

- The site must have different levels of access depending on whether the user has registered for an account and has admin privileges.

- Unregistered users must be able to view basic information about homeopathy and the service I provide. They also have the ability to contact me via the contact page. They don't have the ability to book appointments or purchase remedies or remedy kits.

- Unregistered users must be able to become registered users by creating a user account by entering a unique username, email address and a password into the sign-in page.

- Registered users must be able to log into their user account using a unique username or email address and a password. Once successfully logged in, the user has the ability to to book appointments or purchase appointments, remedies or remedy kits.

- Resistered user must be able to view their order and appointment history.

- Registered users without admin privileges shouldn't be able to edit appointment information, view other users appointments or edit product informations.

- Registered users with admin privileges i.e. the site owner, must be able to use a unique username or email address and password to log into their user account. Once successfully logged in with admin privileges they are able to view, confirm, edit or delete all appointment information for all registered users. They are also able to add, delete or edit product information.

- Registered users with admin privileges i.e. the site owner, must be able to use a unique username or email address and password to log into the site admin panel. From the admin panel they are able to view, edit add or delete all information in the database including individual user accounts.


### User Stories

As an unregistered user:

1. I want to be able to access basic information about homeopathy and it's health benefits the homeopathic services provided by the site as easily possible.

2. I want to be able to access information about the homeopathic services provided by Elements of Healing.

3. I want to be able to access information about Thomas Jones and his homeopathic qualifications.

4. I want to be able to contact Thomas for more information about homeopathy or the homeopathic services provided by Elements of Healing.

5. When I use the contact form I want to be sent an email confirming that the message has been recieved by the site administrator.

6. I may want to be able to register for a user account so I can book a provisional appointment or purchase homepathic products from the site.

7. I may not be familiar with the layout of the site so it must be easy and intuitive to use.

8. I only want to be able to view relevant information about homeopathy and the homeopathic services on offer. I don't want to be able to accidentally book appointments or purchase homepathic products from the site.


As a registered user:

1. I want to be able to log into my account using my account details as quickly and easily as possible.

2. I want to be able to provisionally book an appointment for a homeopathic consultation.

3. I want to be prevented from adding more than one appointment to my shopping basket.

4. I want to be able to delete appointments from my shopping basket.

5. I want to be prevented from booking more than one appointment on the same day.

6. I want to be prevented from booking an appointment on the same date and time as another user.

7. I want to be prevented from booking an appointment in the past.

8. I want to be able to view all my appointments on the site calendar.

9. I want to be able to see if my appointment has been confirmed by the site administrator.

10. I want to be able to access my appointment details from the site calendar.

11. I want my confirmed appointments to automatically appear on my google calendar (if the user has a google account).

12. I want to be able to purchase homeopathic remedies and remedy kits from the site.

13. When I make a purchase I want to be sent an email confirming that my order has been recieved by the site administrator.

14. I want to be able to add, delete or update my shopping basket before purchasing items.

15. I want to be able to view my order and appointment history.

16. I don't want to be able to accidentally book appointments or purchase homepathic products for other user.

17. I want my payment information and order history data to be secure.


As a registered user with admin privileges:

1. I want to be able to log into my account or the admin panel using my account details as quickly and easily as possible.

2. I want to be able to view all appointments for all users on the site calendar.

3. I want to be able to confirm provisionally booked appointments.

4. I want to be able to easily distinguish between confirmed and unconfirmed appointments on the site calendar.

5. I want confirmed appointments to automatically appear on my and the clients google calendar (if the client has a google account).

6. I want to be able to add, delete and update appointments and for this to sync with my google calendar.

7. I want to be able to add, delete and update products on the site shopping cart.

8. I want to be able to view, add, delete and update user accounts when logged in on the site admin panel.


### Wireframes

Wireframes for this project were created using [Balsamiq](https://balsamiq.com/) and can be found [here](https://github.com/TAHJones/qc-metrics-analyser/tree/master/wireframes).


### How to Use the Elements of Healing Website

#### Using the Site as an Unregistered User

##### Viewing the Home, Homeopathy, Consultation and About Page
The home page is automatically displayed when users access the site. It can also be accessed in the main navbar. The homeopathy, consultation and about pages can be accessed by clicking on the `info` dropdown link in the main navbar.

<div align="center">
    <a href="https://elementsofhealing.herokuapp.com" target="_blank">
        <img src="https://i.ibb.co/kQv58hZ/home-page.png" alt="home-page">
    </a>
</div>
<br>

##### Using the Contact Page
The contact form can be accessed by clicking on the `contact` link. Unregistered users must enter their name, email and message into the form before submitting their message. An email will be send to the email address submitted in the form to confirm that the message has been recieved by the site administrator.

<div align="center">
    <a href="https://elements-of-healing.herokuapp.com" target="_blank">
        <img src="https://i.ibb.co/Cvh5zLT/contact-page.png" alt="contact-page">
    </a>
</div>
<br>

##### Creating a User Account
Unregistered users can create a user account by entering a unique username, email address and password in the form on the sign-up page. An email with a link to register the new account will be sent to the email address submitted in the form. The sign-up page can be accessed by clicking on the `account` dropdown link in the main navbar then clicking on the `register` link.

#### Using the Site as a Registered User

##### Logging into a User Account
Registered users can log into their user account by entering a unique username, email address and password in the form on the sign-in page. The sign-in page can be accessed by clicking on the `account` dropdown link in the main navbar then clicking on the `login` link.

##### Purchasing Items from the Products Page
Registered users can purchase appointments, remedies and remedy kits using the shopping cart.

 Step 1 - The products page can be accessed by clicking on the `info` dropdown link in the main navbar then clicking on the `products` link. The products page allows users to view all the available homepathic products. From the products page the user is able to access individual product pages by clicking on the product link. It is also possible to filter the products by category, price or rating or search for an individual product by entering keywords into the search form in the main navbar.

<div align="center">
    <a href="https://elements-of-healing.herokuapp.com" target="_blank">
        <img src="https://i.ibb.co/bgxFXFz/products-page.png" alt="products-page">
    </a>
</div>
<br>

 Step 2 - The product page allows the registered user to view individual product details including a product image, description, price, rating and category. The user can update the quantity and if the product is a remedy to select a potency. Finally the user can either add the product to their shopping basket or return to the products page. Items in the shopping basket will remain for the users session and can be accessed at anytime by clicking on the basket icon in the main navbar.

<div align="center">
    <a href="https://elements-of-healing.herokuapp.com" target="_blank">
        <img src="https://i.ibb.co/12CYvnB/product-page.png" alt="product-page">
    </a>
</div>
<br>

 Step 3 - The shopping basket contains all the products selected for purchase by the registered user. This includes appointments, remedies or remedy kits. Products in the shopping basket can be updated or removed. From the shopping basket the user can proceed to the checkout or return to the products page and make more purchases.

<div align="center">
    <a href="https://elements-of-healing.herokuapp.com" target="_blank">
        <img src="https://i.ibb.co/ftDVfN3/shopping-basket.png" alt="shopping-basket">
    </a>
</div>
<br>

##### Booking an Appointment
Registered users can book and purchase appointments using the appointment form and shopping cart.

 Step 1 - Registered users can book an appointment by clicking on the `appointments` link in the main navbar. The user can enter their name, email address, message and an appointment date & time into the appointment form.
 
<div align="center">
    <a href="https://elements-of-healing.herokuapp.com" target="_blank">
        <img src="https://i.ibb.co/H2J7ZkS/appointment-page.png" alt="appointment-page">
    </a>
</div>
<br>

 Step 2 - Once the user has submitted the form they are redirected to the appointment details page where they can review there appointment request then add it to the shopping basket or return to the appointment page if they wish to make changes.

<div align="center">
    <a href="https://elementsofhealing.herokuapp.com" target="_blank">
        <img src="https://i.ibb.co/mvMJ8pT/appointment-details-page.png" alt="appointment-details-page">
    </a>
</div>
<br>

 Step 3 - The shopping basket contains all the products selected for purchase by the registered user. This includes appointments, remedies or remedy kits. Only one appointment can be in the shopping cart at one time. The current appointment must be purchased from the checkout page or deleted from the shopping basket if the user wishes to book another appointment.

#### Completing the Purchase of Appointments, Remedies and Remedy Kits

 Step 1 - From the shopping basket click on the `Secure Checkout` button to navigate to the checkout page.
 
 Step 2 - On the checkout page the registered user can review all the products selected for purchase. It also has a form for the user to enter order details and purchase information. From the checkout page the user can finalise their purchase or return to the shopping basket and update their purchases. To complete the purchase and navigate to the checkout success page click on the `Complete Order` button.

<div align="center">
    <a href="https://elementsofhealing.herokuapp.com" target="_blank">
        <img src="https://i.ibb.co/cgqCCy2/checkout-page.png" alt="checkout-page">
    </a>
</div>
<br>

 Step 3 - The checkout success page confirms that the purchase has been successful and provides the registered user with a summary of the order. From the checkout success page the user can return to the home page.

<div align="center">
    <a href="https://elementsofhealing.herokuapp.com" target="_blank">
        <img src="https://i.ibb.co/c66S4jG/checkout-success-page.png" alt="checkout-success-page">
</div>
<br>

##### Viewing Appointments in the Calendar
Registered users can view all of their appointments by clicking on the calendar icon in the main navbar. Appointments can be viewed on a month by month basis. Appointments in red are unconfirmed and appointments in yellow have been confirmed by the site administrator. By clicking on the individual appointments in the calendar the user is able to view the appointment details for that appointment. This includes the name, email, message, date, time and confirmation status.

<div align="center">
    <a href="https://elementsofhealing.herokuapp.com" target="_blank">
        <img src="https://i.ibb.co/0nZKLQz/appointment-calendar.jpg" alt="appointment-calendar">
    </a>
</div>
<br>

<div align="center">
    <a href="https://elementsofhealing.herokuapp.com" target="_blank">
        <img src="https://i.ibb.co/P94qydr/appointment-details-page-2.png" alt="appointment-details-page-2">
    </a>
</div>
<br>

##### Viewing Order and Appointment history
Registered users can view their order and appointments history in the profile page. This can be accessed by clicking on the `account` dropdown link in the main navbar then clicking `my profile`. The users order delivery information can be view and updated in the profile page.


#### Using the Site as a Registered User with Admin Privileges
As well as being able to use all the features available to regular registered users, the user with admin privileges is able to do the following:

###### Logging into a User Admin Account
Registered users with admin privileges or superusers can log into their user account by entering a unique username, email address and password in the form on the sign-in page. The sign-in page can be accessed by clicking on the `account` dropdown link in the main navbar then clicking on the `login` link. These credentials can be created by entering the following command in the terminal `python3 manage.py createsuperuser` where you will then be prompted to enter a unique username, email address and password.

##### Viewing User Appointments in the Calendar
Superusers can view all user appointments by clicking on the calendar icon in the main navbar. Appointments can be viewed on a month by month basis. Appointments in red are unconfirmed and appointments in yellow have already be confirmed. By clicking on the individual appointments in the calendar the superuser is able to view the appointment details and confirm, update or delete that appointment. When an appointment is confirmed it is automatically added to the superusers google calendar. An invitation to the event is also sent to the client (if the client has a google account).

<div align="center">
    <a href="https://elementsofhealing.herokuapp.com" target="_blank">
        <img src="https://i.ibb.co/3hGtgZ5/appointment-calendar-2.jpg" alt="appointment-calendar-2">
    </a>
</div>
<br>

<div align="center">
    <a href="https://elementsofhealing.herokuapp.com" target="_blank">
        <img src="https://i.ibb.co/KxWzSrL/appointment-details-page-3.png" alt="appointment-details-page-3">
    </a>
</div>
<br>

##### Updating and Deleting Homepathic Products
Registered users with admin privileges or superusers can update or delete products in the products page. Each item in the products page has two links. The first is an `update` link which navigates to the product management page where the product details can be edited and saved. The second is a `delete` link which deletes the product from the database. To add a new product the superuser must click on the `account` dropdown link in the main navbar then click on the `product management` link. The superuser can when enter the new product details in the empty form.

##### Updating the Site Database Using the Admin panel
A feature of the django website is that users with admin privileges are able to log into the inbuilt site admin panel. This is achieved by adding `/admin` to the root url then entering their unique username or email address and password in the admin panel sign-in page. Once logged in the superuser has access to all data in the site database and can add, delete or update user accounts.


## Main Features

### Home Page

The home page allows all users of the site to see some basic information about homeopathy and the homeopathic practice of Thomas Jones. From the home page the user is able to access the homeopathy, consultation, about, contact, signup and login page.

### Homeopathy Page

Provides all users with more information about homeopathy.

### Consultation Page

Prodvides all users with information about the homeopathy consutation process.

### About Page

Provides all users with background information about Thomas Jones and his homeopathic qualifications.

### Contact Page

Provides all users with a contact form to contact the site administrator.

### Login Page

The login page allows a registered user to log into their user account using their unique username or email address and password.

### Signup Page

The signup page allows unregistered users to create a user account by entering a unique username, email address and password into the signup form.

### Signout Page

The signout page allows a registered user to log out of the site and end their current session.

### Products Page

Allows registered users to view homepathic products which includes appointments, remedies and remedy kits. From the products page the registered user is able to access individual product pages. It is possible to filter the products by category, price or rating.

### Product Page

Allows registered users to view details for individual homepathic products. The product page allows the registered user to add the product to the shopping basket or return to the products page.

### Appointments Page

Allows registered users to book/purchase homeopathic appointments. The appointments page allows the registered user to enter their name, email address, message and a appointment date & time into a form which they can submit. Once the user has submitted the form they are redirected to the appointment details page where they can review there appointment request and add it to the shopping basket or return to the appointment page if they wish to make changes.

### Shopping Basket

The shopping basket contains all the products selected for purchase by the registered user. This includes appointments, remedies or remedy kits. Products in the shopping basket can be updated or removed. From the shopping basket the user can proceed to the checkout or return to the products page and make more purchases.

### Checkout Page

The checkout page contains all the products selected for purchase by the registered user. It also has a form for the user to enter order details and purchase information. From the checkout page the user can finalise their purchase or return to the shopping basket and ammend their purchases.

### Checkout Success Page

The checkout success page confirms that the purchase has been successful and provides the registered user with a summary of the order. From the checkout success page the user can return to the home page.

### Profile Page

The profile page allows the registered user to view their order and appointment history. It also allows the user to edit order delivery information.

### Calendar Page

The calendar page allows the registered user to view all of their appointments. It allows registered users with admin privileges to view all user appointments. By clicking on individual appointments the user is able to access the appointment details page for that appointment.

### Appointment Details Page

The appointment details page allows the registered user to view the details for individual appointments. It allows registered users with admin privileges to confirm provisionally booked appointments and to delete or update appointments.

### Search Form

The search form allows registered users to search for individual products using keywords.

### Product Management Page

The product management page is only accessible to users with admin privileges. It allows the user to add, delete or update products on the site.

### Features Left to Implement

- Prevent users from booking appointments for the current week. Appointments should be booked at least a week in advance.

- Currently appointments are automatically deleted from the calendar if they are removed from the shopping basket. However appointments deleted from the calendar are not automatically deleted from the shopping basket.

- Link up the purchase of appointments with the confirmation of appointments.

- There are several small javascript errors that need to be fixed.

- The copyright statement fails to appear when the page is first downloaded. This has been temporarily fixed by adding a default HTML copyright statement and inserting the current year as a template variable. However a permanent javascript solution needs to be found.

- Add a blog site to the website that can be viewed by registered users. 

- Add video media to the site so online remote appointments can be offered to registered users.

- The python code in many views has become quite complicated and needs reorganising.


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
- [google-auth-oauthlib/](https://pypi.org/project/google-auth-oauthlib/)
- [google-auth-httplib2](https://pypi.org/project/google-auth-httplib2/)
- [google-api-python-client](https://pypi.org/project/google-api-python-client/)
- [AWS S3 Bucket](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingBucket.html)
- [Google Calendar API](https://developers.google.com/calendar/quickstart/python)


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

- When adding a product to the shopping basket a http 500 internal server error occurred with the following error message `KeyError at /basket/add/22/, 'appointment_details'`. This error was traced back to the add_to_basket view and was fixed by replacing `appointment_de
tails = request.session['appointment_details]` with `appointment_details = request.session.get('appointment_details', {})`.

- Found a security problem with the shopping basket. The appointment form input field is designated as readonly to prevent more than one appointment being entered at a time. However this can be overridden by the client using the developer tools. This was fixed by resetting the appointment quantity to 1 in the checkout view.

- Tested appointment booking / email using the temporary email website `https://temp-mail.org` and my gmail account.

- Tested shopping basket & checkout pages using temporary email website `https://temp-mail.org` and Stripes payment page.

- Error message when using the contact form  `invalid literal for int() with base 10: '2020-11-30'`. This was fixed by replacing `datetime.today()` with `datetime.today().year` which provided necessary integer value without the need for extra steps which were causing the error above.

- `Server Error (500)` & `ProgrammingError at /contact/` occurs when navigating to contact form after deployment to heroku.This was caused by migration changes not being added to postgres database. These Errors were fixed by adding DATABASE_URL to gitpod environment variables so that migration changes were updated to postgres rather than mysqlite database.

- When an appointment is purchased & an appointment is already in the shopping basket the 'remove' link for that appointment stops working.  The following error `Internal Server Error: "POST /basket/remove/2/ HTTP/1.1" 500 0` is displayed in the terminal. This was fixed by adding a conditional statement to the appointments view and add_to_basket view to check if the basket already contains an appointment. If it does it redirects to the basket page instead of trying to add a new appointment and breaking the link. 

- When an appointment is deleted from the shopping basket, the appointment is still displayed on the calendar. This was fixed by adding the calendar appointment `id number` to the `appointment_details` session variable. This could then be used to delete the appointment from the calendar if the appointment was removed from the basket. Two other session variables, `confirmed` & `eventID` were used to delete the corresponding google calendar event if the appointment was removed from the basket.


## Deployment

### How to Deploy Project Using Gitpod

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


### How to Deploy Project Using Heroku

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
EMAIL_HOST_PASS | `<your_secret_key>`
EMAIL_HOST_USER | `<your email address>`

14. In the heroku dashboard, click "Deploy".

15. Click on the "Open App" button at the top of the page. Your [Heroku website]( https://elementsofhealing.herokuapp.com/) is now successfully deployed.


## How to add Google Calendar API

### Create a New Google Calendar API Project

1. Go to the [Google Developer Console]( https://console.developers.google.com)

2. To create a new google developer project click on the dropdown link in the navbar then select `NEW PROJECT`.

3. In the search form enter `google calendar api` and select ` Google Calendar API`. Then click `ENABLE`.

4. In the sidebar click on the link `Credentials` followed by `+ CREATE CREDENTIALS`. Then select the authorisation method named `OAuth client ID`.

5. In the `Application type` dropdown menu select `Desktop app`, change the default name for your OAuth 2.0 client if you wish, then click `CREATE`.

6. A pop message will appear telling you that you OAuth client has been created. Your new client id and your client secret will also be displayed. Click OK.

7. In the credentials page under the OAuth 2.0 Client IDs section, your new OAuth client should be visible. Click on the download icon on the far right to download a copy of your `client_secret.json` file.


### Add Credentials to Connect Your Project to the Google Calendar API

In the terminal run the following command to install the library using pip3:

1. Check that you have the following libraries installed in your project (they should have been installed during deployment):

- google-api-python-client
- google-auth-httplib2
- google-auth-oauthlib

2. If they aren't installed run the following command in the terminal:
```
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```

3. Place your `client_secret.json` file in the root directory of your project.

4. Create a file called `googleCalendarAPI.py` as follows:
```
from apiclient.discovery import build

from google_auth_oauthlib.flow import InstalledAppFlow

import pickle


scopes = ['https://www.googleapis.com/auth/calendar']

flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", scopes=scopes)

credentials = flow.run_console()

pickle.dump(credentials, open(‘token.pkl’, ‘wb’))
```

5. Run the python script in the terminal from the root of your project:
```
python3 googleCalendarAPI.py
```

6. Click on the url address in the terminal then sign in with your google account credentials when prompted.

7. Click `Allow` to grant permissions to see, edit, share and delete your google calendars (you may need to go into advanced settings to do this).

8. Copy the authorization code that is generated and paste it into the terminal where it says: `Enter the authorization code:`

9. This should create a file called `token.pkl` in your root directory which will allow your project to connect to the google calendar api.

10. For security purposes, you should now delete the `client_secret.json` file. You can also delete the `googleCalendarAPI.py` script.

11. If you make any changes to your current scope settings you will need to delete the current token file and use the client_secret.json to generate a new token file.


### Google Calendar API Tutorials

For more information about integrating the google calendar api into your project see the following tutorials:
 - [www.youtube.com/watch?v=j1mh0or2CX8](https://www.youtube.com/watch?v=j1mh0or2CX8)
 - [developers.google.com/calendar/create-events#python_1](https://developers.google.com/calendar/create-events#python_1)
 - [developers.google.com/calendar/quickstart/python](https://developers.google.com/calendar/quickstart/python)
 - [gist.github.com/nikhilkumarsingh](https://gist.github.com/nikhilkumarsingh/8a88be71243afe8d69390749d16c8322)


## How to add AWS S3 Bucket
The AWS S3 bucket was added to the site using the codeinstitute Boutique Ado django project tutorial. More information on adding a AWS S3 bucket can be found [here](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingBucket.html).


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

- The shopping cart is based on the codeinstitute Boutique Ado django project and was modified by myself for the purposes of this site.
