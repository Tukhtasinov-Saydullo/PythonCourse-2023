from telebot import TeleBot, types
import API_base
BOT_TOKEN = API_base.crypto_wallet()

bot = TeleBot(BOT_TOKEN)
markup = types.InlineKeyboardMarkup()


@bot.message_handler(commands=['start'])
def welcome_message(message):
    user_id = message.from_user.full_name
    uz_btn = types.InlineKeyboardButton('Uzbek🇺🇿', callback_data='/help')
    markup.add(uz_btn)
    bot.send_message(chat_id=message.chat.id, text=f'Hello User! {user_id}', reply_markup=markup)


@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(chat_id=message.chat.id, text='Hello SSSS')


if __name__ == '__main__':
    bot.polling()
