import os

from flask import Flask, render_template, url_for, request, redirect, session
from apiTest import travelPlan, parseObjectToString
from locationAPI import returnCoordinates
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
db = SQLAlchemy(app)


def itineraryObjectCreator(breakfastList, lunchList, dinnerList, attractionList):
    itineraryObject = {
        "breakfastList": breakfastList,
        "lunchList": lunchList,
        "dinnerList": dinnerList,
        "attractionList": attractionList,
    }

    return itineraryObject


class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    savedData = db.Column(db.String(1000))

    def __repr__(self):
        return f'<Account {self.username}>'


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about_us')
def about_us():
    return render_template("about_us.html")


@app.route('/recommendations')
def recommendations():
    return render_template("recommendations.html")


@app.route('/itinerary')
def itinerary():
    return render_template("itinerary.html")


@app.route('/planner', methods=['GET', 'POST'])
def planner():
    if request.method == 'POST':
        location = request.form['location']
        ll = returnCoordinates(location)
        radius = int(request.form['radius'])
        days = int(request.form['totalDays'])
        travelPlans = travelPlan(ll, radius, days)
        travelPlans.dataPopulate()
        saveObject = itineraryObjectCreator(travelPlans.breakfastList, travelPlans.lunchList, travelPlans.dinnerList, travelPlans.attractionList)
        session['saveObject'] = saveObject
        totalDays = []

        for day in range(days):
            totalDays.append(day)
        return render_template("itinerary.html",
                               duration=totalDays,
                               breakfastList=travelPlans.breakfastList,
                               lunchList=travelPlans.lunchList,
                               dinnerList=travelPlans.dinnerList,
                               attractionsList=travelPlans.attractionList,
                               parseString=parseObjectToString,
                               )
    else:
        return render_template("planner.html")


@app.route('/sign-up', methods=['GET', 'POST'])
def signUp():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        savedData = ","

        newAccount = Account(username=username, password=generate_password_hash(password), savedData=savedData)

        try:
            db.session.add(newAccount)
            db.session.commit()

            return redirect("/sign-up")

        except:
            return "There was an error with this operation"

    return render_template("registration.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['loginUsername']
        password = request.form['loginPassword']

        user = Account.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            return render_template(
                "welcome.html",
                username=username
            )
        else:
            return "Invalid username or password"

    return render_template("registration.html")

@app.route('/save', methods=['GET', 'POST'])
def save():
    if request.method == 'POST':
        my_var = session.get('saveObject')
        try:
            user_id = session['user_id']
            currUser = Account.query.get(user_id)
            currUser.savedData += f"{my_var}"
            db.session.commit()

        except KeyError:

            return "You need to be logged in"

    return render_template("planner.html")
    # check to make sure they are logged in. And add this to the third column saved data
# session['user_id'] = user.id play around with this is: 100% how you determine if a player is logged in

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)
