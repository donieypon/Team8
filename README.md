# stuffToDo

As busy college students, one of the biggest challenges we face is keeping track of all the things to do. Students have many classes throughout the day, multiple assignments to do, study for other classes, and may have their own errands to run. With this issue in mind, our group felt this to be an interesting challenge to take on and decided to create **stuffToDo**. 

### Features: ###

Markup: *Register
To access the web app, a user must have an account. New users can create their own personal accounts by entering their name, a valid email address, and a password. Once registered, the user's credentials are saved via MySQL Database and will allow the user to login at any time. 

        *Login
Existing users who have made accounts can log into the web app to access its features. Once a user is logged in, they are redirected to the homepage where they will be able to create a task and logout.

        *Logout
Users who are logged into the web app are given the option to log out. Logging out will save the user's tasks/lists until the next login via database. 

        *Create Task
Creating a task is the main feature of this web app. Here, users enter a task name, task description, and a date they would like to complete the task by. Once submitted, the task will be saved and will be seen by the user on the homepage. This incomplete task will be displayed under the section *Not Completed*.

        *Complete/Remove Task
Users who have created tasks have the ability ability to manipulate tasks. They can mark a task as completed and will be displayed under the *Completed* section. Users can also remove a task completely from their lists whether it has been completed or not.  

        *Create List
Users have the ability to create a list which is a compilation of tasks for organizational purposes. Users can select which list to send the task to. Lists will be displayed on the homepage. 

      *Add Friend(s)
Users have the ability to add other users of this web app. Users can search for other user by their emails, and friend requests can be sent. Once a user is a friend, users can share their lists for viewing/editing to other users.

      *Sharing Capabilities
Sharing capabilities are only available to users who are friends. With given permission, users can collaborate on tasks/lists.


# Travis CI

[![Build Status](https://travis-ci.com/donieypon/Team8.svg?branch=master)](https://travis-ci.com/donieypon/Team8)
