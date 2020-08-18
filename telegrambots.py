from telegram.ext import Updater, MessageHandler , Filters , CommandHandler
import random
import sqlite3


#data needed
letters = [
    'الف','ب','پ','ت یا ط','ج','چ','خ','د'
    ,'ر','ز یا ض یا ظ یا ذ','ژ','ش','ص یا س یا ث',
    'ع','ف','ق یا غ','ک','گ','ل','م','ن','و',
    'ه یا ح','ی'
]
category = [
    'اسم','فامیل','شهر','کشور','میوه','غذا','رنگ','حیوان',
    'ماشین','اشیاء','گل','شغل','اعضای بدن','پوشاک','مشاهیر'
]
sen = ["شما باید با حرف '",
       "' در موضوع "," کلمه بگید"]

token_bot = "1118640921:AAEA-DoYAk5BlDmzzDNhUhdeKAknoR5l1qw"

updater = Updater(token=token_bot)

dispatcher = updater.dispatcher

def games(bot , update):
    reply = sen[0] + letters[random.randint(0, len(letters))] + sen[1] + category[random.randint(0, len(category))] + sen[2]
    update.message.reply_text(reply)

def jokes(bot , update):
    conn = sqlite3.connect('sms.db')

    c = conn.cursor()

    c.execute("SELECT * FROM Sms WHERE Category = 'جوک'")

    items = c.fetchall()

    update.message.reply_text(items[random.randint(0, len(items))][1])

    conn.commit()

    conn.close()

def fun(bot , update):
    conn = sqlite3.connect('sms.db')

    c = conn.cursor()

    c.execute("SELECT * FROM Sms WHERE Category = 'طنز'")

    items = c.fetchall()

    update.message.reply_text(items[random.randint(0, len(items))][1])

    conn.commit()

    conn.close()

def poem(bot , update):
    conn = sqlite3.connect('sms.db')

    c = conn.cursor()

    c.execute("SELECT * FROM Sms WHERE subcategory = 'شعر'")

    items = c.fetchall()

    update.message.reply_text(items[random.randint(0, len(items))][1])

    conn.commit()

    conn.close()

def loves(bot , update):
    conn = sqlite3.connect('sms.db')

    c = conn.cursor()

    c.execute("SELECT * FROM Sms WHERE subcategory = 'عاشقانه'")

    items = c.fetchall()

    update.message.reply_text(items[random.randint(0, len(items))][1])

    conn.commit()

    conn.close()

def did_you_know(bot , update):
    conn = sqlite3.connect('sms.db')

    c = conn.cursor()

    c.execute("SELECT * FROM Sms WHERE Category = 'آیا می دانید؟'")

    items = c.fetchall()

    update.message.reply_text(items[random.randint(0, len(items))][1])

    conn.commit()

    conn.close()

def help(bot , update):
    reply = """
    /esm : بازی اسم و فامیل
    /joke : جک های بی مزه و با مزه
    /love : متن های عشقولانه 😍
    /fun : متن های طنز  
    /poem : شعر 
    /aya : آیا میدانستید
    """
    update.message.reply_text()



dispatcher.add_handler(CommandHandler("esm",games))
dispatcher.add_handler(CommandHandler("joke",jokes))
dispatcher.add_handler(CommandHandler("love",loves))
dispatcher.add_handler(CommandHandler("fun",fun))
dispatcher.add_handler(CommandHandler("poem",poem))
dispatcher.add_handler(CommandHandler("aya",did_you_know))
dispatcher.add_handler(CommandHandler("help",help))


updater.start_polling()

updater.idle()