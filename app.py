import os, requests, random, math, time
from flask import Flask, render_template, url_for
from apiTest import travelPlan, parseObjectToString

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about_us')
def about_us():
    return render_template("about_us.html")


@app.route('/recommendations')
def recommendations():
    return render_template("recommendations.html")


@app.route('/planner', methods=['GET', 'POST'])
async def planner():
    travelPlans = travelPlan("32.361668,-86.279167", 50, 1)
    travelPlans.dataPopulate()
    # we need for loop to solve this
    return render_template("planner.html",
                           breakfastList=parseObjectToString(travelPlans.breakfastList[0]),
                           lunchList=parseObjectToString(travelPlans.lunchList[0]),
                           dinnerList=parseObjectToString(travelPlans.dinnerList[0]),
                           activityOneList=parseObjectToString(travelPlans.attractionList[0]),
                           activityTwoList=parseObjectToString(travelPlans.attractionList[1]),
                           activityThreeList=parseObjectToString(travelPlans.attractionList[2]),

                           )


if __name__ == "__main__":
    app.run(debug=True)
