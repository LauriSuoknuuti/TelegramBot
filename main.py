import telegram as tg
from telegram.ext import Updater, CommandHandler


def test(bot, update):
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text="Paul on nörtti!")


def main():
    updater = Updater('545436423:AAGy60La5xAtpJC3ccl7ziXSzKsoAV__QVE')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('paul', test))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()

