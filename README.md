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
