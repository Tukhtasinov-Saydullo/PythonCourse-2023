from telebot import TeleBot, types

BOT_TOKEN = '5942048652:AAGtp3Hq1Y2Lxgxh4V8iKCxVkvXSCpYfmaw'

bot = TeleBot(BOT_TOKEN)
markup = types.InlineKeyboardMarkup()


@bot.message_handler(commands=['start'])
def welcome_message(message):
    user_id = message.from_user.full_name
    uz_btn = types.InlineKeyboardButton('Uzbek🇺🇿', callback_data='help')
    markup.add(uz_btn)
    bot.send_message(chat_id=message.chat.id, text=f'Hello User! {user_id}', reply_markup=markup)


@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(chat_id=message.chat.id, text='Hello SSSS')


if __name__ == '__main__':
    bot.polling()
