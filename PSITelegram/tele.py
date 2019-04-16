import telepot
from telepot.loop import MessageLoop
from pprint import pprint

bot = telepot.Bot('875919915:AAEBaJkCoVmL4SXOZMky8-ZYGkklQPIEQBI')
region_list = ('north','south','east','west','central')

def handle(msg):
    userid = msg['chat']['id']
    region = msg['text']
    if region not in region_list:
        bot.sendMessage(userid),"Welcome to a PSI Alert Bot! When the PSI level flucuates"

MessageLoop(bot,handle).run_forever()