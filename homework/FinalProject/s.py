import telebot
import code
import json
import random
def Molder():
    with open ('glob.json','r',encoding='utf-8') as k:
        glob=json.load(k)
    a=random.choice(glob)
    res=''
    while True:
        if res == '':
            res+=a[0].capitalize()
        else:
            res+=a[0]
        m1=a[2].keys()#znak prepinaniya
        m1=list(m1)
        m2=a[2].values()
        m2=list(m2)
        znak=random.choices(m1,weights=m2,k=1)
        res+=znak[0]
        if znak[0]!=' ':
            res+=' '
        m1=a[1].keys()#next word
        m1=list(m1)
        m2=a[1].values()
        m2=list(m2)
        a=random.choices(m1,weights=m2,k=1)[0]
        for v in glob:
            if v[0]==a:
                a=v
                break
        if res[-2]=='.':
            break
    return(res)
bot=telebot.TeleBot(code.TOKEN)
@bot.message_handler(func=lambda m: True)    
def sendtheword(message):
    bot.send_message(message.chat.id,Molder())
if __name__ == '__main__':
    bot.polling(none_stop=True)
