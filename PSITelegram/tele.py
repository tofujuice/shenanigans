import telepot
from telepot.loop import MessageLoop
from pprint import pprint
import database

bot = telepot.Bot('875919915:AAEBaJkCoVmL4SXOZMky8-ZYGkklQPIEQBI')
region_list = ('north','south','east','west','central')

def handle(msg):
    userid = msg['chat']['id']
    region = msg['text']
    if region == 'remove':
        database.removeUser(userid)
        bot.sendMessage(userid, "PS:I will cherish the hours we had together :(")
    elif region not in region_list:
        bot.sendMessage(userid,'Welcome to PSI Alert Bot!\n\n How this works: When the PSI level flucuates, the bot will send you an alert regarding the details of the current PSI.\n\n How to get it started: Just type in the region you live in (north,south,east,west,central) (e.g. north) without the brackets. \n\n I no longer want this: Just type (remove) without the brackets')
    else:
        region = region_list.index(region) + 1
        database.storeUser(userid,region)
        bot.sendMessage(userid,"Alert activated!")

def psi_alert(userid,msg):
    bot.sendMessage(userid,msg)

MessageLoop(bot,handle).run_as_thread()