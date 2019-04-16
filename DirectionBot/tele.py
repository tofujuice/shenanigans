import telepot 
from telepot.loop import MessageLoop
from pprint import pprint
import time
import maps

def handle(msg):
    teleID = msg['chat']['id']
    try:
        teleLocation = msg['location']
        result = maps.location(teleLocation)
        pprint(result)
    except KeyError:
        try:
            telePostal = msg['text'].split(',')
            result = maps.direct(telePostal[0],telePostal[1],telePostal[2])
            sendMsg = "Travelling from " + telePostal[0] + " to " + telePostal[1] + "\n\n"
            
            for r in result:
                for l in r['legs']:
                    for s in l['steps']:
                        if s['travel_mode'] == 'TRANSIT':
                            if telePostal[2] == 'bus':
                                sendMsg = sendMsg + "Take Bus " + s['transit_details']['line']['name'] + "\nFrom: " + s['transit_details']['departure_stop']['name'] + "\nTo: " + s['transit_details']['arrival_stop']['name'] + "\nNumber of stops: " + str(s['transit_details']['num_stops'])
                            elif telePostal[2] == 'train':
                                sendMsg = sendMsg + "Take the MRT" + "\nFrom: " + s['transit_details']['departure_stop']['name'] + "\nTo: " + s['transit_details']['arrival_stop']['name'] + "\nNumber of stops: " + str(s['transit_details']['num_stops'])
                            bot.sendMessage(teleID, sendMsg)
        except:
            bot.sendMessage(teleID,'BEEP BOOP ERROR ERROR BEEP BOOP!')


bot = telepot.Bot('799998798:AAECPb8IURiqYFItSezv8tFYE6N0J2Muw4M')
bot.message_loop(handle, run_forever=True)