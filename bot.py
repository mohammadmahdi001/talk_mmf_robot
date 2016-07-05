# -*- coding: utf-8 -*-
import telebot
import json
import requests
import time


bot = telebot.TeleBot('YOURTOKEN')

@bot.message_handler(func=lambda m: True)
def on_message(m):
    url = 'http://api.program-o.com/v2/chatbot/'
    args = ' '.join(m.text.split()[1:])
    cid = m.chat.id
    params = {
        'bot_id' : '6',
        'say' : args,
        'convo_id' : 'chatterbot',
		    'format' : 'json'
    }
    jstr = requests.get(url, params=params, headers=None, files=None, data=None)
    data = json.loads(jstr.text)
    if jstr.status_code != 200:
        bot.reply_to(m, "*Fuck. An error was found. Please report this to my Developer:* " + str(jstr.status_code))
    else:
        bot.send_chat_action(cid, 'typing')
        time.sleep(1)
        bot.reply_to(m, "IRob says: *" + data['botsay'] + "*" , disable_web_page_preview="True", parse_mode="Markdown")
#    else:
#        bot.reply_to(m, "*Owww no! An error was found.*", parse_mode="Markdown") //TODO

bot.polling(none_stop=True)
