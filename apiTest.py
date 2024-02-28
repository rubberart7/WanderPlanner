import requests, os, random, math

url = "https://api.foursquare.com/v3/places/search"

# https://location.foursquare.com/developer/reference/place-search (all params)

# Query: Search result of type of establishment
# ll: The coordinate of the place. (We need to use another api that will convert places (from string) into coordinate)
# radius: (In meters) How many meters around the ll should we search for establishment
# Optional Queries: Sort, min/max price, categories)

# Set params to whatever the "Post request" from js gives us
# Change query based on what we should do and what time it is. Morning we have breakfast etc


# response = requests.get(url, headers=headers, params=param)
# responseJson = response.json()
# print(responseJson)

# responseJson["results"][index number]["name"]
# This will give the name of the first breakfast store that comes out
# responseJson["results"][index number]["location"]["formatted_address"] This will give the address of the location
# responseJson["results"][index number]["categories"][0]["name"] This will give us the category of establishment

# For this project, we should extract the name of the hotel and the address


API_KEY = os.getenv("API_KEY")

if API_KEY is None:
    key = os.environ.get("API_KEY")

headers = {
    "accept": "application/json",
    "Authorization": API_KEY
}

param = {
    "query": "breakfast",
    "ll": "39.952583,-75.165222",
    "radius": 10000,
}

url = "https://api.foursquare.com/v3/places/search"
def parameterChange(query, ll, radius):
    radius = radius * 1609  # Will convert miles into meters

    param = {
        "query": query,
        "ll": ll,
        "radius": radius,
    }
    return param


def locationObjectCreator(name, address, startTime=None, endTime=None):
    locationObject = {
        "name": name,
        "ll": address,
        "startTime": startTime,
        "endTime": endTime
    }
    return locationObject

def parseObjectToString(listInput):
    return f"{listInput["name"]} - {listInput["ll"]} - {listInput["startTime"]} - {listInput["endTime"]}"

class travelPlan:
    def __init__(self, coordinates, radius, totalDays):
        self.plan = []
        self.breakfastList = []
        self.lunchList = []
        self.dinnerList = []
        self.attractionList = []
        self.coordinates = coordinates
        self.radius = math.floor(radius)
        self.totalDays = totalDays
        self.hotel = None

    # created this method to save the amount of api calls we use (we have a limit)
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

        lunchParam = parameterChange("lunch", self.coordinates, self.radius)
        response = requests.get(url, headers=headers, params=lunchParam)
        responseJson = response.json()
        for day in range(0, self.totalDays):
            lunchObject = locationObjectCreator(responseJson["results"][day]["name"],
                                                responseJson["results"][day]["location"]["formatted_address"], 13, 15)
            self.lunchList.append(lunchObject)

        dinnerParam = parameterChange("dinner", self.coordinates, self.radius)
        response = requests.get(url, headers=headers, params=dinnerParam)
        responseJson = response.json()
        for day in range(0, self.totalDays):
            dinnerObject = locationObjectCreator(responseJson["results"][day]["name"],
                                                 responseJson["results"][day]["location"]["formatted_address"], 19, 21)
            self.dinnerList.append(dinnerObject)

        touristParam = parameterChange("tourist", self.coordinates, self.radius)
        response = requests.get(url, headers=headers, params=touristParam)
        responseJson = response.json()
        for day in range(0, self.totalDays):
            touristObject = locationObjectCreator(responseJson["results"][day]["name"],
                                                  responseJson["results"][day]["location"]["formatted_address"], 10, 13)
            self.attractionList.append(touristObject)

            touristObject = locationObjectCreator(responseJson["results"][day * 2]["name"],
                                                  responseJson["results"][day * 2]["location"]["formatted_address"], 15, 17)
            self.attractionList.append(touristObject)

            touristObject = locationObjectCreator(responseJson["results"][day * 3]["name"],
                                                  responseJson["results"][day * 3]["location"]["formatted_address"], 17, 19)
            self.attractionList.append(touristObject)

    # General One hotel that we will use
    def setHotel(self):

        # Change this so that in the future it is randomized
        param = parameterChange("hotel", self.coordinates, self.radius)
        response = requests.get(url, headers=headers, params=param)
        responseJson = response.json()
        index = random.randint(0, len(responseJson["results"]) - 1)
        hotelObject = locationObjectCreator(responseJson["results"][index]["name"],
                                            responseJson["results"][index]["location"]["formatted_address"])
        self.hotel = hotelObject






# Bug List:

# Bug 1: When there is not enough data from the api, the list will break. We need to implement error catching
# Fix 1: We should have two templates, if there is not enough tourist attractions, we will follow the 2nd template

# Bug 2: We are getting a lot of repeats of same stores esp if the radius is small