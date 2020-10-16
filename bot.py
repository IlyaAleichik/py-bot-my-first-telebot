import config
import telebot
import random
import re

file_id = "CAACAgIAAxkBAAOEX4l-hyLbIdCKcM7FPJCXNwKBeYAAAooBAAIQIQIQcMU5aupZY9MbBA"


question = ["Вопрос"]
answers = ["Ответ1","Ответ2", "Ответ3"]
arrMessage = ["Привет", "Ку", "Хай"]
arrText = ["Ку", "Да я тут", "Что нада","Напише мне привет хотя-б", "Я тебя не понимаю. Напиши /help."]



stopText = ["Пока", "До встречи", "До свидания"]

command = ["отключение", "stop"]

bot = telebot.TeleBot(config.token)

keyboard = telebot.types.ReplyKeyboardMarkup()
keyboard.row('Привет', 'Пока', 'Ку', 'Познакомимся')


@bot.message_handler(commands=['stop'])
def stop_bott(message):
    bot.send_message(message.chat.id, "Отключаюсь")
    bot.stop_bot()

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(
        message.chat.id, "Комманды бота \n /stop - отключение бота \n ")


@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(
        message.chat.id, "Комманды бота \n /stop - отключение бота \n ")

@bot.message_handler(commands=['poll'])
def sendpooling(message):
    bot.send_poll(message.chat.id, question, answers)

@bot.message_handler(content_types=['text'])
def send_addfriend(message):
    if message.text == "Познакомимся":
        bot.send_message(message.chat.id, " Давай знакомиться. Как тебя зовут")
        bot.register_next_step_handler(message, get_username)
    elif message.text in arrMessage:
        bot.send_message(message.chat.id, "Привет", reply_markup=keyboard)
    elif message.text in stopText:
        bot.send_message(message.chat.id, stopText[random.randrange(0, 3)])
    else:
        bot.send_message(message.chat.id, arrText[random.randrange(0, 4)])


@bot.message_handler(content_types=['text'])
def get_username(message):

    bot.send_message(message.chat.id, "Очень приятно " +
                     message.text + " а меня Бот")
    bot.send_sticker(message.chat.id, file_id)



if __name__ == "__main__":
    bot.polling()
