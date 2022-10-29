from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CommandHandler

from wiki import serchWiki

TOKEN = "5683994914:AAHvBl6EUt-qvS27aJANTefwe5LBVB6kAdU"

def wikiSelecter(update, context):
    print(context.arg)
    word = "".join(context.arg)
    if word:
        update.message.reply_text("Идет поиск...")
        summary, url =serchWiki(word)
        update.message.reply_text(summary + url)
    else:
        update.message.reply_text("Вы не ввели данные")

def start(update, context):
    update.message.reply_text("Начинаю свою работу")

def echo(update, context):
    txt = update.message.text
    if txt.lower() in ['привет', 'hello']:
        txt = 'Ну привет'
    update.message.reply_text(txt)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    print("Бот запущен...")

    dp.add_handler(CommandHandler("wiki", wikiSelecter))
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text, echo))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__" :
    main()