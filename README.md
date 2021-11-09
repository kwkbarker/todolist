# ToDoList
Kevin Barker

A web application to keep track of tasks.

Written in Python/Flask, HTML and JavaScript with Bootstrap and CSS styling.

## ROUTES.py

- /index

redirects to **/tasks** if user is signed in, **/login** if not.

- /tasks

This is the API endpoint, capable of processing get, post, put and delete commands.

If user is not logged in, redirects to **/login** using a **@login_required** decorator located in **helpers.py**.

If the request is GET, renders the user's tasks saved in the database and the form to create a new task. the tasks are rendered as bootstrap accordion cards with a visible title header that can be clicked to expand the description card beneath it. Each task has an '**Edit**' button, which launches a modal prefilled with the existing text to be able to edit, and a '**Done**' button which deletes the task.

The tasks can be rendered in four colors - white if given no **importance**, red if "urgent," yellow if "soon," and grey if "whenever."

If an entry is edited with an **edit modal** triggered by an **edit button**, the form sends a POST request along with a hidden input of **"protocol: put"** which tells the API to edit the task to which it is applied.

If an entry is dismissed with the **"Done" button**, the button sends a POST request with the hidden input of **"protocol: delete"** which tells the API to delete the entry from the database.

- /register

Allows the visitor to register as a new user. Uses **bcrypt** to create hashed passwords.

- /login

Logs the user in. 

- /logout

Logs the user out.


## MODELS.py

- User

Stores autoincremented id, username, hashed password, email, tasks relationship

- Task

Stores autoincremented id, title, description, importance, user (foreign key)

- /admin

Provides a Model View of the database. 

## FORMS.py

- Register, Login, and Task forms

## APPS.js

- clearFields() - clears the fields of the task form when the form is submitted.

- fillFields() - called when an edit modal is launched; prefills the edit fields with the task's existing text.

## POSSIBLE IMPROVEMENTS

- restrict admin access
- make tasks sortable (e.g. by urgency)
- move 'Done' tasks to a 'Completed' section instead of deleting them