from flask import Flask, render_template, url_for

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

@app.route('/planner')
def planner():
    return render_template("planner.html")


if __name__ == "__main__":
    app.run(debug=True)
