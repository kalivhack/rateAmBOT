import time
import requests
from bs4 import BeautifulSoup
from cgitb import text
import telebot 

bot = telebot.TeleBot('5687207648:AAGRV6efI2-FbzbfugTipY9H19wyIHTFfdc')

bot.polling(non_stop=True)
text = ''

url = "https://rate.am/am/armenian-dram-exchange-rates/exchange-points/cash"

classes = ["bank", "best"]

numbers = []
AllTR = []
GettedINFO = []
bank = []
tiv = 0
tiv_2 = 0


def second():
    global tiv, tiv_2
    r = requests.get(url)
    AllTR = []
    urlBS = []
    urlBS = BeautifulSoup(r.content, "html.parser").find()
    AllTR = urlBS.findAll("tr")

    for i in range(len(AllTR)):
        if AllTR[i].attrs != {} and len(AllTR[i].attrs["id"]) == 36:
            GettedINFO.append(AllTR[i])
            tiv+=1  
            td = AllTR[i].findAll("td")
            span = AllTR[i].findAll("span")

            
            for i in td:
                if 'class' in i.attrs and 'bank' in i.attrs['class']:    
                    print(str(i.find("a").getText()), end = " ")
                    bank.append(i.find("a").getText())
                    # print(bank)
               
                
            for i in span:
                # print(tiv) 
                if 'class' in i.attrs and 'best' in i.attrs['class'] and tiv == 1 and tiv_2 != 2:
                    numbers.append(float(i.getText()))
                    tiv_2 += 1
                    # print(numbers)

                if i.attrs != {} and i.attrs['class']:
                    print(i.getText(), end = " ")

            print("\n")
    print(numbers)

def main():
    global text
    # while True:

    second()
    print("END")
    print(numbers)
    if len (numbers) > 0 and numbers[0] >= 410:
        text = f"все курсы из <b>rate.am</b> в {bank[0]} банке доллар стоит пример {numbers[0]} драм при продаже и {numbers[1]} драм при покупке."

    elif len (numbers) == 0 or numbers[0] < 410:
        text = f"Сейчас Доллар стоит меньше 410 драм почти во всех банках"
    
    # time.sleep(1800)    

print("You Can Start")
@bot.message_handler(commands=['start'])
def start(message):
    textt = f'Hi,{message.from_user.first_name} this bot will help you find the best bank in Armenia where the dollar is worth more than 410 drams.<b>FOR START TYPE /check</b>  '
    bot.send_message(message.chat.id, textt, parse_mode='html')
    print("Sending Message")

@bot.message_handler(commands=['check'])
def check(message):
    numbers = []
    bank.clear()
    print(bank, "fdnjksfhsdhfsdhfkjahfds")
    main()
    bot.send_message(message.chat.id, text, parse_mode='html')

@bot.message_handler(commands=['help'])
def check(message):
    
    bot.send_message(message.chat.id, "Problems with bot say me @AAFF25", parse_mode='html')


bot.polling(non_stop=True)  