import telebot
token=''
bot = telebot.TeleBot(token)
import random

@bot.message_handler(commands=['start'])
def welkome (message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

    item1 = telebot.types.KeyboardButton('Znak Zadiaka')
    item2 = telebot.types.KeyboardButton('Ugadayka')
    item3 = telebot.types.KeyboardButton('Hochu stiker')

    markup.add(item1, item2,item3)

    bot.send_message(message.chat.id, 'Vyberite nujnyy punkt:', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def zadiak (message):
    if message.text == 'Znak Zadiaka':
        markup = telebot.types.InlineKeyboardMarkup(row_width=2)
        item1= telebot.types.InlineKeyboardButton('Oven', callback_data='1')
        item2 = telebot.types.InlineKeyboardButton('Telec', callback_data='2')
        item3 = telebot.types.InlineKeyboardButton('Bliznec', callback_data='3')
        item4 = telebot.types.InlineKeyboardButton('Rak', callback_data='4')
        item5 = telebot.types.InlineKeyboardButton('Lev', callback_data='5')
        item6 = telebot.types.InlineKeyboardButton('Deva', callback_data='6')
        item7 = telebot.types.InlineKeyboardButton('Vesy', callback_data='7')
        item8 = telebot.types.InlineKeyboardButton('Scorpion', callback_data='8')
        item9 = telebot.types.InlineKeyboardButton('Strelec', callback_data='9')
        item10 = telebot.types.InlineKeyboardButton('Kozerog', callback_data='10')
        item11 = telebot.types.InlineKeyboardButton('Vodoley', callback_data='11')
        item12 = telebot.types.InlineKeyboardButton('Ryba', callback_data='12')
        markup.add(item1, item2, item3, item4, item5, item6, item7, item8, item9, item10, item11, item12)
        bot.send_message(message.chat.id, 'Vyberite svoy znak:', reply_markup=markup)
    elif message.text == 'Ugadayka':
        chislo=bot.send_message(message.chat.id, 'Ugaday chislo ot 1 do 3')
        bot.register_next_step_handler(chislo, ugadayka)
    elif message.text == 'Hochu stiker':
        bot.send_sticker(message.chat.id,f'{stiker(5)}')


@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
    znak=int(call.data)
    if call.data == '1':
        bot.send_message(call.message.chat.id, f'{opisanie(znak)}')
    elif call.data == '2':
        bot.send_message(call.message.chat.id, f'{opisanie(znak)}')
    elif  call.data == '3':
        bot.send_message(call.message.chat.id, f'{opisanie(znak)}')
    elif call.data == '4':
        bot.send_message(call.message.chat.id, f'{opisanie(znak)}')
    elif call.data == '5':
        bot.send_message(call.message.chat.id, f'{opisanie(znak)}')
    elif call.data == '6':
        bot.send_message(call.message.chat.id, f'{opisanie(znak)}')
    elif call.data == '7':
        bot.send_message(call.message.chat.id, f'{opisanie(znak)}')
    elif call.data == '8':
        bot.send_message(call.message.chat.id, f'{opisanie(znak)}')
    elif call.data == '9':
        bot.send_message(call.message.chat.id, f'{opisanie(znak)}')
    elif call.data == '10':
        bot.send_message(call.message.chat.id, f'{opisanie(znak)}')
    elif call.data == '11':
        bot.send_message(call.message.chat.id, f'{opisanie(znak)}')
    elif call.data == '12':
        bot.send_message(call.message.chat.id, f'{opisanie(znak)}')
def opisanie (call):

    with open('text.txt', 'r', encoding='utf-8') as file:
        for i in range (1,13):
            dikt=file.readline()
            if i == call:
                return dikt

def ugadayka (message):
    rand= random.randint(1,3)
    mess= int(message.text)
    if mess==rand:
        bot.send_message(message.chat.id, 'Ty Ugadal')
        bot.send_sticker(message.chat.id, 'CAACAgQAAxkBAAEHI69jtzlKYZiOWSPDMEdfpm39Abt1QAACOBAAAkRoaFCJRL1_2gIV5S0E')
    elif mess!= rand and mess<3 and mess>0:
        bot.send_message(message.chat.id, 'Ne Ugadal')
        bot.send_sticker(message.chat.id, 'CAACAgQAAxkBAAEHI7Vjtzn13pzVlPf7Ve0nGnYzCk3WagAC-w0AApUCaFCcIlkE41NiwS0E')
    else:
        bot.send_message(message.chat.id, 'Ne coreknoe chislo')
        bot.send_sticker(message.chat.id,'CAACAgQAAxkBAAEHI7NjtzlhaLDDk1A41A9HgiW74jB1YQACrwwAAsDXaVBqZuQtKwoDaC0E')

def stiker (p):
    rand= random.randint(1,p)
    with open ('stiker.txt', 'r') as file:
        for i in range (1,p):
            dikt= str(file.readline())
            if i == rand:
                return dikt

bot.polling(none_stop=True)
