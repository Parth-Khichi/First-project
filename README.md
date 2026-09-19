# Flask Users Table

This is a simple Flask project that displays a list of users in an HTML table.

## What I did

1. Created a `/users` route in Flask.
2. Added sample user data in `app.py`.
3. Passed the user data to the HTML page using Jinja2.
4. Created an HTML table to display the users' names and emails.

## Files

- `app.py` - Contains the Flask application and user data.
- `templates/users.html` - Displays the users in an HTML table.

## How it works

When I open the `/users` route, Flask sends the user data to `users.html`.

Jinja2 loops through the users and displays their name and email in the table.

## Technologies Used

- Python
- Flask
- HTML
- Jinja2

## How to run

Install Flask:

```bash
pip install flask

python app.py

then
http://127.0.0.1:5000/users

