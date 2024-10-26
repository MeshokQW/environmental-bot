import telebot
from config import TOKEN

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.send_message(
        message.chat.id, '''Привет! Я бот, который рассказывает советы по экологии\n\n
        Мои команды: \n\n
        \sort  - советы по сортировке мусора, напишите название предмета и команду\n
        \\time - советы по переработке мусора, напишите название предмета и команду
        '''
        )
    

@bot.message_handler(commands=['sort'])
def sort_item(message):
    key = telebot.util.extract_arguments(message.text)
    list_utils = [
        'телевизор',
        'батарейки',
        'пылесос',
        'бытовая техника',
        'шины',
        'аккумуляторы',
        'нефтепродукты',
        'грудусник',
        'медецинские отходы'        
        ]
    if key in list_utils:
        bot.send_message(message.chat.id, f'{key} необходимо отдать на переработку')
    else:
        bot.send_message(message.chat.id, f'{key} можно выбрость в обычную урну')

@bot.message_handler(commands=['time'])
def time(message):
    key = telebot.util.extract_arguments(message.text).lower()
    decompose_items = {
        'пластиковая бутылка': '450 лет',
        'стеклянная бутылка': '1-2 млн лет',
        'бумага': '2-5 лет',
        'папирус': '2-5 лет',
        'книга': '50-100 лет',
        'журнал': '5-10 лет',
        'батарейки':  '1-5 лет',
        'аккумуляторы': '5-10 лет',
        'нефтепродукты': '100-500 лет',
        'грудусник': '100-500 лет',
        'медецинские отходы': '100-500 лет',
        'телевизор': '100-500 лет',
        'пылесос': '100-500 лет',
        'шины': '100-500 лет',
        'бытовая техника': '100-500 лет',
    }
    if key in decompose_items:
        bot.send_message(message.chat.id, f'Время разложения {key} - {decompose_items[key]}')
    else:
        bot.send_message(message.chat.id, f'Время разложения {key} неизвестно')
    

bot.infinity_polling()
