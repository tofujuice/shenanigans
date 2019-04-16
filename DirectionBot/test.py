import maps 
from pprint import pprint

result = maps.direct('760751','178902','train')
  
for r in result:
    for l in r['legs']:
        for s in l['steps']:
            if s['travel_mode'] == 'TRANSIT':
                sendMsg = "Take the MRT" + "\nFrom: " + s['transit_details']['departure_stop']['name'] + "\nTo: " + s['transit_details']['arrival_stop']['name'] + "\nNumber of stops: " + str(s['transit_details']['num_stops'])
                print(sendMsg)