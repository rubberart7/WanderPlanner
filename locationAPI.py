import requests, os, random, math

from opencage.geocoder import OpenCageGeocode

from dotenv import load_dotenv

load_dotenv()


def returnCoordinates(address):
    key = os.getenv("LOCATION_API_KEY")
    if key == None:
        key = os.environ.get("LOCATION_API_KEY")

    geocoder = OpenCageGeocode(key)


    results = geocoder.geocode(address)

    return f"{results[0]['geometry']['lat']},{results[0]['geometry']['lng']}"