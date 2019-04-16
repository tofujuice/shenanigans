import googlemaps
from datetime import datetime
from pprint import pprint

def location(msg):
    gmaps = googlemaps.Client(key='AIzaSyCUQWs_Wp6b2lAg81a48dCikGbO77HyJFU')
    reverse_geocode_result = gmaps.reverse_geocode((msg['latitude'], msg['longitude']))
    return reverse_geocode_result

def direct(locationFrom,locationTo,locationMode):
    gmaps = googlemaps.Client(key='AIzaSyCUQWs_Wp6b2lAg81a48dCikGbO77HyJFU')
    directionTime = datetime.now().replace(hour = 14)
    directions_result = gmaps.directions(locationFrom,
                                        locationTo,
                                        mode='transit',
                                        transit_mode=locationMode,
                                        departure_time=directionTime)
    return directions_result