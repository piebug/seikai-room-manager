# seikai-room-manager
This is the room scheduler for the Seisho Kaichi high school. Event management!

Step 1: Create and start venv
    - install python, venv
Step 2: Install requirements ('pip install -r requirements.txt')
Step 3: Create your database (install PostgreSQL, v13)
    - Create user and password in PostgreSQL shell
        - `(CREATE USER <user> WITH PASSWORD 'password';) > will return "Create Role'`
    - Create database in PostgreSQL shell
        - `(CREATE DATABASE seikairooms;) > will return "Create Database"`
Step 4: Migrate the database `python manage.py migrate`
Step 5: Run server `python manage.py runserver`