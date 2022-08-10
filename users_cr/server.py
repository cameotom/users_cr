from flask import Flask, render_template, request, redirect, session  # Import Flask to allow us to create our app
from user import User

app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = 'secret' # set a secret key for security purposes

@app.route('/')
def index():
    # call the get all classmethod to get all users
    users = User.get_all()
    for i in users:
        print(i.first_name, i.last_name)
    return render_template("index.html", users=users)

@app.route ('/add_user')
def add_user():
    return render_template("add.html")

@app.route('/create_user', methods=["POST"])
def create_user():
    # First we make a data dictionary from our request.form coming from our template.
    # The keys in data need to line up exactly with the variables in our query string.
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"]
    }
    # We pass the data dictionary into the save method from the user class.
    User.save(data)
    # Don't forget to redirect after saving to the database.
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
