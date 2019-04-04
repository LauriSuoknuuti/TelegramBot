import telegram as tg
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import scraper
import weather_API
import random

# Lisää tähän dictionaryyn uudet komennot ja selitteet (komento -> selite)
commands_dict = {"/paul": "Printtaa faktan Paulista.",
                 "/menu": "Printtaa päivän ruokalistan.",
                 "/commands": "Printtaa listan komennoista.",
                 "/weather": "Printtaa tämänhetkisen lämpötilan"}


def paul(bot, update):
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text="Paul on nörtti!")


def start(bot, update):
    update.message.reply_text("Moro Kalex-kamut. "
                              "Kirjoita /commands saadaksesi lista komennoista. ")

# TODO parantele outputtia, esim tyhjät pois
# TODO weatheriin parempi output


def menu(bot, update):
    chat_id = update.message.chat_id
    message = scraper.main()
    message_string = "\n".join(message)
    bot.send_message(chat_id=chat_id, text=message_string)


def weather(bot, update):
    chat_id = update.message.chat_id
    message = weather_API.main()
    message_string = "".join(str(message))
    bot.send_message(chat_id=chat_id, text=message_string)


def echo(bot, update):
    chat_id = update.message.chat_id
    random_text = ["vitun homo", "vitun köyhä", "vitun läski", "tapa ittes"]
    bot.send_message(chat_id=chat_id, text=random.choice(random_text))


def commands(bot, update):
    chat_id = update.message.chat_id
    commands_string_unform = []
    for x, y in commands_dict.items():
        commands_string_unform.append(str(x) + " -> " + str(y))
    commands_string = "\n".join(commands_string_unform)
    bot.send_message(chat_id=chat_id, text=commands_string)


def main():
    updater = Updater('545436423:AAGy60La5xAtpJC3ccl7ziXSzKsoAV__QVE')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("paul", paul))
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("commands", commands))
    dp.add_handler(CommandHandler("menu", menu))
    dp.add_handler(CommandHandler("weather", weather))
    dp.add_handler(MessageHandler(Filters.reply, echo))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
