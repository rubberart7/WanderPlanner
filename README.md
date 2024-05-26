# WanderPlanner

The objective of this project is to create an accessible and simple travel itinerary to provide useful suggestions for users. Our application specifically focused on recommending attractions that are considered hidden gems to our users. We utilized both frontend (js, css, python) and backend (python) languages with the Flask framework for the technical side of the project. Our project utilized a system Scrum master, Kanban Boards, and three-week sprints to complete the project. Essentially, the project was built through an Agile/ Scrum methodology. 

## Setting Up the Environment

This section will outline the necessary steps to set up the environment, the dependencies and packages. 

### Cloning the Git Repo
##### 1. Go to the project repository on gitlab (https://gitlab.cci.drexel.edu/fds24/ci10x-student-teams/62/02/ci-102-lab-62-group-02)
##### 2. Click on the green code button, copy and paste the ssh key and pull up your terminal/ command line interface on your computer
##### 3. Do git clone (the ssh key) and press enter. It then will ask you for a username and key to login. The username is your school user (ex. lw873) and the password is the passcode we created in CS164 lab 2. If you forgot this code, you can create a new one in the access tokens section of gitlab. 

### Downloading Necessary Dependencies ofr the application
<br />
1. Once you open the website on the IDE, download all the dependencies and libraries from this video (https://www.youtube.com/watch?v=Z1RJmh_OqeA) 5:30 - 9:05
<br />
2. After following the steps above, you should now create an .env file that's completely empty. In our discord group chat, go to the pinned messages and copy-paste the message that has three lines of secret keys and api keys. 
<br />
3. The pinned comments on the discord server should also have all the extra libraries you need to download, copy and paste that into your IDE's terminal. 
<br />
4. Now, run your code on your IDE through python3 app.py (mac) or python app.py (windows)





## Git Workflow (How to work on project)

Git workflow will be posted here (Follow it step by step): https://docs.google.com/document/d/1cxKUMrTeb3NJ40x8wjpGM7iA5bGtKzq_QGtelMirSdc/edit?usp=sharing



## Navigation and explanation of our repository

In our project, we follow the grouping format of normal flask applications. Therefore, we use the env, instance, and static folders are all utilized in the project.
<br />
<br />
The **_instance_** folder holds the mySQL database that we use for the login functionality. 
<br />
The **_static_** folder holds the css and images files of our application. 
<br />
The **_templates_** folder will hold all the html pages that you can navigate through the navigation bar. 
<br />

For our backend code however, we have python files scattered right under the main directory of the repository as they are each very significant. 

### Functionality of the main files
#### Python Files: 
(app.py)
<br />
The app.py file is the main file that the application runs on. This file is where the front end connects with the backend via flask. There are many endpoints laid throughout the file with each of them connecting a specific html file with necessary information derived from the backend. 
##### Example: 
```python 
@app.route('/toggleLog', methods=['GET', 'POST'])
def toggleLog():
    print(session["logState"])
    if request.method == "POST":
        logState = request.form["hiddenForm"]
        session["logState"] = logState
        if logState != "Log Out":
            allData.clear()

        db.session.close()

    return render_template("registration.html")
```
The snippet of code is an endpoint that's called when the /toggleLog endpoint is toggled in a html form. When this endpoint is toggled, the application will check the session variable of logState and depending on whether the user is logged in or not, we will apply different changes on the application. After this, we will return renderTemplate which will bring us to the form inside the function (In this instance registration html)

(locationAPI.py)
<br />
The locationAPI.py file utilizes the OpenCageGeoCode API to convert addresses into coordinate locations which we need in apiTest.py (One of the inputs)

```python 

load_dotenv()


def returnCoordinates(address):
    key = os.getenv("LOCATION_API_KEY")
    if key == None:
        key = os.environ.get("LOCATION_API_KEY")

    geocoder = OpenCageGeocode(key)


    results = geocoder.geocode(address)

    return f"{results[0]['geometry']['lat']},{results[0]['geometry']['lng']}"

```
The function just takes the address that we send it in app.py and returns the specific latitude and longtiude of that address

(apiTest.py)
<br />

The apiTest.py file houses a class that will create the date plan object that our application uses to parse data. It's a large data file where multiple steps such as gathering data, organizing data, and redistributing data all take place. It utilizes the FourSquare API in gathering the attractions that we will reccomend to the users.  

#### Information Gathering:

```python 

def dataPopulate(self):
    # Implement system that can check for repeats
    # Implement system to check when the location open and close

    breakfastParam = parameterChange("breakfast", self.coordinates, self.radius)
    response = requests.get(url, headers=headers, params=breakfastParam)
    responseJson = response.json()
    for day in range(0, self.totalDays):
        breakfastObject = locationObjectCreator(responseJson["results"][day]["name"],
                                                responseJson["results"][day]["location"]["formatted_address"], 8,
                                                10)
        self.breakfastList.append(breakfastObject)


```
When this method is called, we will call the foursquare API to give us all the breakfast locations in a certain area and add it to the return list later. We repeat this for attractions, lunchList, dinnerList and eventually will have a full list of travel plans to send to app.py. 
#### HTML Files: 
(base.html)
<br />
The base.html file is the main file that all of the other html files inherit from. This file is where the general formatting of each page lies and it contains items like the navigation bar, the help toolbar button, and the footer. 
##### Example: 
```html 
      <img class="logoImg" src="../static/css/images/wander2.png" alt="" onclick="window.location.href='/'"/>
      <h1 class="logoName" onclick="window.location.href='/'">WanderPlanner</h1>
      <div class="buttonContainer">
        <button class="button" onclick="window.location.href='/'">Home</button>
        <div class="dropdown">
          <button class="button" onclick="window.location.href='/planner'">
            Planner
          </button>
          <div id="dropdownContent">
            <a class="link" onclick="window.location.href='/savedPlans'">
              Saved Plans
            </a>
          </div>
        </div>
        <button class="button" onclick="window.location.href='/recommendations'">
          Recommendations
        </button>
        <button class="button" onclick="window.location.href='/map'">
          SimpleMap
        </button>
        <button class="button" onclick="window.location.href='/about_us'">
          About Us
        </button>
```
The snippet of code shows some of the html code for the navigation bar. Here we can see that there is an image tag for the logo, and several button tags for each of the tabs the navigation bar allows navigation to. We can also see that there is an onclick event with every button that brings the page to its dedicated html page.

(index.html)
<br />
The index.html file is the home page of Wanderplanner. It contains a general overview of the website and a button that leads to the main functionality of the website which is the form required to generate the itinerary plan (planner.html).
##### Example: 
```html 
    <div class="info">
        <div class="infoHeader">
            <h1>A tool to embark on your perfect adventure</h1>
        </div>
        <div class="infoText">
            <p>
                "Discover boundless horizons with WanderPlanner, your gateway to
                personalized journeys. Unleash the extraordinary as we meticulously
                craft seamless itineraries, turning your wanderlust into unforgettable
                adventures. Start planning now."
            </p>
        </div>
        <div class="startNowBtn">
            <button onclick="window.location.href='/planner'">Plan Now -></button>
        </div>
    </div>
```
An information div is shown here and it contains a header, some information, along with a button that brings the user to the planning page.

(planner.html)
<br />
The planner.html file contains the form that takes the input of the user's destination and number of days to generate an intinerary. The form is proccessed in the backend which then generates the detailed itinerary (from apiTest.py) to output on itinerary.html.
##### Example: 
```html 
    <div class="link-container">
        <form action="/planner" method="post" class="travelForm">
            <h2>Travel Budget Form</h2>

            <label for="totalBudget">Total Budget (Dollars):</label>
            <input type="number" id="totalBudget" name="totalBudget" placeholder="e.g. 1000" required>

            <label for="radius">Radius (Miles):</label>
            <input type="number" id="radius" name="radius" placeholder="e.g. 20" required>

            <label for="totalDays">Total Days:</label>
            <input type="number" id="totalDays" name="totalDays" placeholder="e.g. 4" required>

            <label for="location">Location:</label>
            <input type="text" id="location" name="location" placeholder="e.g. 3675 Market Street" required>

            <label for="departure">Departure Date:</label>
            <input type="date" id="departure" name="departure" placeholder="mm/dd/yyyy" required>

            <label for="return">Return Date</label>
            <input type="date" id="return" name="return" placeholder="mm/dd/yyyy" required>

            <button type="submit" class="formSubmit">Submit</button>

            <a href='/recommendations'>Don't know where to go?</a>
        </form>
    </div>
```
This snippet of code shows the form with all of the required inputs the user needs to enter to generate an itinerary. The required fields contains: budget, radius (how far user is willing to travel), totals days, address of location, and departure/return date. This is also a link that leads to the reccomendation page which shows a variety of countries with a short description.

(about_us.html)
<br />
The about_us.html file contains information about Wanderplanner's team and the roles of each member. Additionally, it contains our mission statement, our goals, and a way to send feedback or contact us.
##### Example: 
```html 
     <div class="fullscreen">
      <h1>Contact Us</h1>
      <form action="https://formspree.io/f/xdoqvnev" method="POST">
        <textarea id="query" class="textarea" name="query"></textarea>
        <input type="submit" value="Send" id="textsubmit">
      </form>
  </div> 
```
This snippet of code contains the "Contact Us" form for users to input some sort of feedback or message which is then sent to us.

(login.html)
<br />
The login.html file contains both the login and signup form to create an account for Wanderplanner.
##### Example: 
```html 
    <div class="login-container hideForm">
        <form class="login">
            <h1>Login</h1>

            <label for="loginUsername">Username</label>
            <input
            type="text"
            name="loginUsername"
            id="loginUsername"
            placeholder="Enter Username"
            />

            <label for="loginPassword">Password</label>
            <input
            type="password"
            name="loginPassword"
            id="loginPassword"
            placeholder="Enter Password"
            />

            <button>Login</button>

            <p>Don't have an account?</p>
        </form>
    </div>
```

Here is the login form and it requires a username and password to login. The username and password input is checked in the backend when the form is submitted. If the username/password combination is invalid (not in the database) an error message will appear. There is also a link on the bottom that redirects the user to the signup form if they do not have an account.

#### CSS Files: 
(main.css)
<br />
The main.css file contains all of the css for every single html page. 
##### Example: 
```css
    @import url("https://fonts.googleapis.com/css2?family=Ubuntu:wght@300;400;500;600&display=swap");

    :root {
        /*https://colorhunt.co/palette/eef5ffb4d4ff86b6f6176b87  (Link to color palette)*/
        --lightgray: #EEF5FF;
        --lightblue: #B4D4FF;
        --darkerlightblue: #98b4d9;
        --skyblue: #86B6F6;
        --deepblue: #176B87;
        --bodybackground: #f0f0f0;
        --fontcolor: #808080;
    }

```
This snippet of code imports the Ubuntu font that we use throughout all of our html pages. There is also the a bunch of colors that we use for the theme of our website that is easily accessible in the root selector.






