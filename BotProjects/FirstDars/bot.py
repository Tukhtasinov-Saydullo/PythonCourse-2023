from telebot import TeleBot

BOT_TOKEN = '5942048652:AAGtp3Hq1Y2Lxgxh4V8iKCxVkvXSCpYfmaw'

bot = TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    print(message)


if __name__ == '__main__':
    bot.polling()
