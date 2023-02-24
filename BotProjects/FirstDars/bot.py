from telebot import TeleBot, types
import API_base
from students import Student
from utils import write_csv

BOT_TOKEN = API_base.test_bot()

bot = TeleBot(BOT_TOKEN)
markup = types.InlineKeyboardMarkup()


@bot.message_handler(commands=['start'])
def welcome_message(message):
    chat_id = message.chat.id
    user = message.from_user
    full_name = f"{user.first_name}"
    bot.send_message(chat_id, f'Hello {full_name}👋')
    student = Student(chat_id, full_name)
    write_csv(student)


@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(chat_id=message.chat.id, text='Hello SSSS')


if __name__ == '__main__':
    bot.polling()
