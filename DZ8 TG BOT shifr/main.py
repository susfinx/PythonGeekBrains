import telebot
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

"""Komanda Start"""


@bot.message_handler(commands=['start'])
def welkome (message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

    item1 = telebot.types.KeyboardButton('Kodirovat tekst')
    item2 = telebot.types.KeyboardButton('Dekodirovat tekst')

    markup.add(item1, item2)

    bot.send_message(message.chat.id, 'Dobro Pojalovat! Vyberite nujnyy punkt:', reply_markup=markup)
@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Kodirovat tekst':
        messg = bot.send_message(message.chat.id, 'VVedite tekst')
        bot.register_next_step_handler(messg, get_user_text)
    elif message.text == 'Dekodirovat tekst':
        bot.send_message(message.chat.id, f'dekodirovanyi tekst: {decompress ()}')

@bot.message_handler()
def get_user_text (message):
    text=message.text
    bot.send_message(message.chat.id, f'Kodirovanyi text: {compress(text)}')

def compress (text):
    with open ('text.txt', 'w') as file:
        same_str=text
        count=1
        i=0
        compress_str=''
        while i< len(same_str)-1:
            if same_str[i]==same_str[i+1]:
                count+=1
            else:
                if count == 1:
                    compress_str +=same_str[i]
                else:

                    compress_str+=str(count)+same_str[i]
                count=1
            i+=1
        file.write(compress_str)
        return compress_str

def decompress ():
    with open ('text.txt',encoding='utf-8') as file:
        compres =file.read()
        decompress_str=''
        for i in range(1,len(compres)):
            if compres[i-1].isdigit():
                decompress_str+=(int(compres[i-1])*compres[i])
            else:
                if compres[i].isdigit():
                    i+=1
                else:
                    decompress_str += compres[i]
        return decompress_str

bot.polling(none_stop=True)
