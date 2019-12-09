StuffToDo
==================

About
######

As busy college students, one of the biggest challenges we face is keep track of all the things to do. Students have many classes throughout the day, multiple assignments to do, study for other classes, and may have their own errands to run. With this issue in mind, our group felt this to be an interesting challenge to take on and decided to create **StuffToDo**.

Getting Started
################

The computer should have Python version 3.6 as well as pip installed to setup a localhost web server for the development of the project.

Prerequisites:
****************

- Flask
- Flask-SQLAlchemy
- Flask-WTF
- Flask-Login
- Flask-mail
- Flask-Bootstrap
- WTForms
- SQLAlchemy
- Werkzeug
- Jinja2
- datetime

Installing
************

Clone this git repo then install the required extensions. Use Terminal to install each extension

Install Flask::

  pip install Flask

Install Flask-WTF, Flask-SQLAlchemy, Flask-Login::

  pip install flask-wtf flask-sqlalchemy flask-login

Apply the above command until every  extension is installed

Running Flask Project
**********************

Export the main file of the project by one of two following commands:

For Windows::

  set FLASK_APP=<filename.py>

For Mac::

  export FLASK_APP=<filename.py>

Then, type::

  flask run

Navigating the app
###################

*Login*

.. image:: /Images/SignIn.png

Existing users can enter their login information to view their tasks. New users can click on **Register** to sign up.
If a user forgets their password, they can reset it by clicking **Forgot password?**

*Register*

.. image:: /Images/Register.png

New users enter their name, email, and a password to create an account.

*Forgot Password*

.. image:: /Images/ForgotPassword.png

Users enter their email where an email to reset their message will be sent.

*Index*

.. image:: /Images/Index.png

This is the homepage of the app. Automatically, users are able to view complete and incomplete
tasks. In the navbar, users can navigate to the homepage, create a task, send a message,
and logout.

*Create Task*

.. image:: /Images/CreateTask.png

To create a task, users enter in the name of the task, followed by an optional short
description. After hitting submit, the task will be displayed on the homepage.

*Message*

.. image:: /Images/Message.png

To send a message, users enter the destination (an email address), the subject, and
the message they would like to send. After hitting submit, the message will be sent as
an email to the given destination.

*Task Options*

.. image:: /Images/TaskOptions.png

Each individual task on the homepage under **Task's to Do** each have the option to
**delete**, **edit**, **complete**, or **share**.

*Edit Task*

.. image:: /Images/EditTask.png

When editing a task, the existing title and description will show up. Users have the
option edit the name or description.

*Share Task*

.. image:: /Images/ShareTask.png

To share a task, users enter the destination (an email address) for the task to be sent
to. After sending, the task's name and description will be sent to the destination
in the form of an email.


app directory
###############







.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
