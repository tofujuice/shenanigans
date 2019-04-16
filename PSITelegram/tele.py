import telepot
from pprint import pprint

bot = telepot.Bot('875919915:AAEBaJkCoVmL4SXOZMky8-ZYGkklQPIEQBI')
response = bot.getUpdates()
pprint(response)