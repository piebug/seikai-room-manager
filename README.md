# seikai-room-manager

This project is a room scheduler for the Seisho Kaichi high school in Tottori, Japan. It will allow teachers and 
students to reserve rooms for meetings and events while preventing double-bookings and misuse of space. It is also an
excellent practice project 🐱‍👓

## Getting started

`seikai-room-manager` is a django/python web app with a PSQL database. To run this on your machine, you must 
install:

- Python 3.9.4
  - (optional) I recommend using a version manager such as `pyenv` or `asdf`
- PSQL 13.4

Django 3.2 and other python dependencies will be installed using `pip`, which is a tool that comes included with python.
You will install them as part of the project setup.

### Setup

1. Clone the project onto your machine using `git clone <repo-url>` and change into the project directory.

2. Create a virtual environment and activate it.
   - `python -m venv <name_of_venv>`

3. Install the requirements.
   - `pip install -r requirements.txt`

4. Separately, create a database.
   - `CREATE USER <user_from_settings> WITH PASSWORD '<db_password>';` > will return `CREATE ROLE` as a success message
     - `ALTER ROLE WITH PASSWORD` if the user was created without a password first
   - `CREATE DATABASE <db_name>;`

5. Migrate the database.
   - `python manage.py migrate`

6. Run the server.
   - `python manage.py runserver`
   - If you want to create a superuser to log into the admin interface: 
   `python manage.py createsuperuser --username <name>`

## Functional requirements

- Students and teachers need to be able to make a user account and set a password.
  - Accounts can only be made with emails that end with `@seitokaichi`.
  - A confirmation email will be sent on account creation and users must verify their account to log in.
  - Teachers will be manually confirmed and given special permissions.

- All users should be able to:
  - Browse the reservable rooms in the school and their capacities.
  - Click on a room to see its features/contents and the schedule for when it is booked/available. Teachers and admins 
  should be able to see who booked a room.
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
