from geopy.geocoders import Nominatim
from geopy.distance import geodesic

geolocator = Nominatim(user_agent="hackathon")


def get_location_by_name(txt):
    location = geolocator.geocode(txt)
    return location.latitude, location.longitude


def get_distance(loc1, loc2):
    location1 = geolocator.reverse(loc1)
    location2 = geolocator.reverse(loc2)
    return geodesic((location1.latitude, location1.longitude), (location2.latitude, location2.longitude)).miles


