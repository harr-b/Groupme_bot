#!/usr/bin/env python

from groupy import Client
import groupy
from groupy.api.bots import Bots, Bot


token = "lg9nNd7cUA0jLSCpPUZu4T2NjTwp02H9A6hvway9"

client = Client.from_token(token)

myGroups = client.groups.list_all()

for group in myGroups:
    if(group.name == 'Admins'):
        message_page = group.messages.list()
        #for message in group.messages.list_all():
            #print(message.text)
        #'df723fe34e4bbf1870cff4111a'
        #group.create_bot('Ben Shapiro', 'https://www.dailywire.com/sites/default/files/styles/article_full/public/authors/ben-shapiro.jpg?itok=yw1Jk2k6', 'http://faxmyguy.com/groupmebot.py', 'none')
        #shapiro = group.create_bot('Ben Shapiro', 'https://www.dailywire.com/sites/default/files/styles/article_full/public/authors/ben-shapiro.jpg?itok=yw1Jk2k6', 'http://faxmyguy.com/groupmebot.py', 'none')
        #shapiro.post('I am ready to eviscerate some liberals beep boop', None)

myBots = client.bots.list()
for bot in myBots:
    if(bot.bot_id == '6c3295198546ce1d2c2553be26'):
        shapiro = bot;
        #shapiro.post('I am ready to eviscerate some liberals beep boop', None)
        
    #print(bot.bot_id)
    