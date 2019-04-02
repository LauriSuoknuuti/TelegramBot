import telegram as tg
from telegram.ext import Updater, CommandHandler

#Lisää tähän listaan uudet komennot
commands_list = ["/paul", "/commands"]


def paul(bot, update):
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text="Paul on nörtti!")


def start(bot, update):
    update.message.reply_text("Moro Kalex-kamut. "
                           "Kirjoita /commands saadaksesi lista komennoista. ")

#:TODO parantele outputtia
def commands(bot, update):
    chat_id = update.message.chat_id
    commands_string = ",".join(commands_list)
    bot.send_message(chat_id=chat_id, text=commands_string)


def main():
    updater = Updater('545436423:AAGy60La5xAtpJC3ccl7ziXSzKsoAV__QVE')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("paul", paul))
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("commands", commands))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
