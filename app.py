from flask import Flask, render_template

app = Flask(__name__)

users = [
    {"name": "Ajay", "email": "ajay@gmail.com"},
    {"name": "Vikas", "email": "vikas@gamil.com"},
    {"name": "Bhushan", "email": "bhushan@gmail.com"}
]

@app.route("/users")
def users_list():
    return render_template("users.html", users=users)

if __name__ == "__main__":
    app.run(debug=True)
