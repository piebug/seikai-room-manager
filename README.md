# seikai-room-manager

This project is a room scheduler for the Seisho Kaichi high school in Tottori, Japan. It will allow teachers and 
students to reserve rooms for meetings and events while preventing double-bookings and misuse of space. It is also an
excellent practice project 🐱‍👓

## Getting started

`seikai-room-manager` is a Django/Python web app with a PSQL database. To run this on your machine, you must 
install:

- [Python 3.9.4](https://www.python.org/downloads/release/python-394/)
  - _Optional, but recommended:_ Use a Python version manager such as `pyenv` or `asdf` for the installation.
    - [Instructions for `pyenv`](https://realpython.com/intro-to-pyenv/) and [`pyenv-win` documentation](https://github.com/pyenv-win/pyenv-win)
    - [`asdf` documentation](http://asdf-vm.com/guide/getting-started.html)
- [PSQL 13.4](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads)
  - [Installation instructions for Windows](https://www.postgresqltutorial.com/install-postgresql/)

[Django 3.2](https://docs.djangoproject.com/en/3.2/releases/3.2/) and other Python dependencies will be installed using 
`pip`, which is a command-line tool that comes included with Python. You will install them as part of the project setup.

We also use [Sass](https://sass-lang.com/) and [Bootstrap 5](https://getbootstrap.com/) for our styling on the frontend. 
These tools can be installed using the [`yarn` package manager](https://classic.yarnpkg.com/en/), but this is an 
optional dependency for all backend development. Go to the [Sass development](#sass-development) section if you'd like 
to set it up.

### Setup

1. Clone the project onto your machine using `git clone <repo-url>` and change into the project directory.

    ```shell
    git clone https://github.com/pies-n-loaf/seikai-room-manager.git
    cd seikai-room-manager
    ```

2. Create a virtual environment and activate it.
   
    ```shell
    python -m venv .venv
    source .venv/Scripts/activate
    ```

3. Install the requirements.

    ```shell
    pip install -r requirements.txt
    ```

4. Separately, create a database. To do this, you will need to open the Postgres console using either the `psql` command 
in your terminal, if you have added it to the path, or by pulling up the SQL shell that was bundled with your PostgreSQL 
installation. You might need to log in using the username and password you chose during setup.

   - Once you are in the Postgres console, first create a user to be the database owner:

       ```sql
       CREATE USER superseikai WITH PASSWORD '<db_password>';
       ```
   
       `<db_password>` is the password of our database. You can get this by being Justin or Sandy. Or you can set it to 
any password of your choosing if you're just trying to run it locally. Whichever case you go with, make sure to create a 
`local_settings.py` file in the `seikairooms/` directory with the constant: 
   
        ```python
        DB_PASSWORD = '<db_password>'
        ```
     
   - Finally, create the database with the above user set as an owner:
        
        ```sql
        CREATE DATABASE seikairooms OWNER superseikai;
        ```

5. Back in your project directory, migrate the database. You may need to reactivate your virtual environment first.

    ```shell
    python manage.py migrate
    ```

6. Run the server and navigate to http://127.0.0.1:8000/ to interact with the app.

    ```shell
    python manage.py runserver
    ```
   
    You may also create a superuser to log into the admin interface: 

    ```shell
    python manage.py createsuperuser --username <your_admin_user>
    ```

### Sass development

1. If you want to work on frontend styling, you will need to install those dependencies. 
Run `yarn install` or `npm install` to do so.
    - [`yarn` installation](https://classic.yarnpkg.com/en/docs/install)
    - [Node.js and `npm` installation](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)

3. Activate your virtual environment (`source .venv/Scripts/activate`) and install the Python requirements 
(`pip install -r requirements.txt`).

4. While writing your new Sass styles, run `python manage.py sass <app_dir>/static/<app_name>/scss/ <app_dir>/static/<app_name>/css --watch`
to actively compile the `.scss` files into `.css`. Run this command without the `--watch` flag to compile on demand. 

## Functional requirements

- Students and teachers need to be able to make a user account and set a password.

  - Accounts can only be made with emails that end with `@seishokaichi`.
  - A confirmation email will be sent on account creation and users must verify their account to log in.
  - Teachers will be manually confirmed and given special permissions.

- All users should be able to:

  - Browse the reservable rooms in the school and their capacities.
  - Click on a room to see its features/contents and the schedule for when it is booked/available.
  - Reserve a room at a time when it is available. Reservations are always approved unless changed by an admin.

- Teachers should also be able to:

  - See who booked a specific room at a given point in time. 
  - Make recurring reservations that can span the entire semester.
  - See a list of conflicts for a recurring event, including who scheduled the conflicting event.

- Admins should also be able to:

  - Manage user accounts using the django admin interface.
  - Resolve scheduling conflicts and cancel events.

- The system will email users when:

  - A user creates an account and needs to confirm it.
  - An event has a conflict due to a teacher or admin scheduling a recurring event over that time.
  - An admin has modified or cancelled another user's event.

- Eventually, the homepage will include a clickable map of the school that shows all the reservable rooms.
