import telebot

CHAVE_API = '6265342996:AAFa1jDmufKxiMGjjdhQa2_V8KleYHe3vUw'

bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(commands=["pizza"])
def pizza(mensagem):
    bot.send_message(mensagem.chat.id, "Pizza coming out, estimated wait time: 20min")


@bot.message_handler(commands=["hamburguer"])
def hamburguer(mensagem):
    bot.send_message(mensagem.chat.id, "The best is being prepared, estimated waiting time: 25min")


@bot.message_handler(commands=["salad"])
def salad(mensagem):
    bot.send_message(mensagem.chat.id, "We are out of salad, click to return to the beginning: /start")


@bot.message_handler(commands=["option1"])
def option1(mensagem):
    texto = """
    Hey, what do you want today? (Choose an option)
    /pizza Pizza
    /hamburguer Hamburguer
    /salad Salad"""
    bot.send_message(mensagem.chat.id, texto)



@bot.message_handler(commands=["option2"])
def option2(mensagem):
    bot.send_message(mensagem.chat.id, "To submit a complaint, send an email to: xxxxxxxxxx@gmail.com")


@bot.message_handler(commands=["option3"])
def option3(mensagem):
    bot.send_message(mensagem.chat.id, "Thanks! another hug.")





def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)
def responder(mensagem):
    texto = """
    Hello, choose an option to continue (click on the item):
    /option1 Make a request
    /option2 Complain about an order
    /option3 Send a hug to Bilebot"""
    bot.reply_to(mensagem, texto)

bot.polling()
