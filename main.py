from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CommandHandler
import time

from wiki import serchWiki

TOKEN = ""

def wikiSelecter(update, context):
    print(context.args)
    word = " ".join(context.args)
    if word:
        update.message.reply_text("Идет поиск...")
        summary, url =serchWiki(word)
        update.message.reply_text(summary + url)
    else:
        update.message.reply_text("Вы не ввели данные")

def start(update, context):
    update.message.reply_text("Начинаю свою работу. Для большей информации напишите /help")

def help(update, context):
    update.message.reply_text("Бот поддерживет следующие команды:"
                              "\n/timer - запуск таймера"
                              "\n/wiki - запрос к википедии"
                              "\n/help - вывод команд")

def echo(update, context):
    txt = update.message.text
    if txt.lower() in ['привет', 'hello']:
        txt = 'Ну привет'
    update.message.reply_text(txt)

def timer(update, context):
    sec = "".join(context.args)
    sec = int(sec)
    update.message.reply_text(f"Таймер запущен {int(sec/60)}:{(sec%60):02} до конца")
    while sec > 0:
        time.sleep(1)
        sec -= 1
    update.message.reply_text("Таймер закончил свою работу")


def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    print("Бот запущен...")

    dp.add_handler(CommandHandler("wiki", wikiSelecter))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("timer", timer))
    dp.add_handler(MessageHandler(Filters.text, echo))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__" :
    main()
