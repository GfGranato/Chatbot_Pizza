import sys
import time
import telepot
import telegram

from telepot.loop import MessageLoop

from telepot.namedtuple import ForceReply, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

TOKEN = sys.argv[1:]  # get token from command-line

bot = telepot.Bot(token='830025759:AAGFXGtpWrWyEkWI_eQO1Q6karejEZv8Yxs')

#tentativa com o incicio,  chat e callback dentro de messageLoop tudo junto

nome =''
endereco =''
pizza = ''
tamanhoP =''
refrigerante = ''
tamanhoR = ''
    #Comeco do programa
@bot.message_handler(content_type == 'text')
def inicio(msg):
    global nome, endereco
        
    global pizza, tamanhoP
    global refrigerante, tamanhoR
        

    content_type, chat_type, chat_id = telepot.glance(msg)

    #Cardápios
    cardapio_pizza= {1:'1 pizza calabreza', 2:'2 pizza 4 queijos', 3: '3 pizza escarola'}
    cardapio_refri= {1:'1 Coca-cola', 2:'2 Fanta-uva', 3:'3 Guaraná'}

    bot.sendMessage(chat_id, 'Olá, qual é o seu nome?')
    nome = msg['text']
    endereco = bot.send_location(chat_id, lat, lon)

#cardapio e pedido de pizza.
    bot.sendMessage(chat_id, 'Faça seu pedido, digite o numero para a opção para pizza')
    for i in cardapio_pizza:
        bot.sendMessage(chat_id, cardapio_pizza[i])  
    pizza = cardapio_pizza[int(msg['text'])]

###tentativa de tamanho da pizza com bot'oes###
    keyboard = ReplyKeyboardMarkup( keyboard= [[KeyboardButton(text ='Brotinho'),KeyboardButton(text ='Média'),KeyboardButton(text ='Grande')]],resize_keyboard = True)

#cardapio e pedido de refrigerante.
    bot.sendMessage(chat_id, 'Agora seu refrigerante ')
    for refrigerante in cardapio_refri:
        bot.sendMessage(chat_id, cardapio_refri[refrigerante])
    refrigerante = cardapio_refri[int(msg['text'])]

###tentativa de tamanho do refrigerante com bot'oes###
    keyboard = ReplyKeyboardMarkup( keyboard= [[KeyboardButton(text ='600 mL'),KeyboardButton(text ='1.5L'), KeyboardButton(text ='2L'), KeyboardButton(text ='Não quero bebidas')]],resize_keyboard = True)

''' falta colocar as opcoes para caso o usuario
    queira pedir mais pizzas e refrigerantes.
    para isso eh necessario adicionar os bot'oes sim e nao,
    mudar as strings para LISTAS.
    '''

    bot.sendMessage(chat_id, 'Obrigado sr '+ nome +', seu pedido é: ')
    bot.sendMessage(chat_id, pizza[1:] +'de tamanho '+tamanhoP)
            
    bot.sendMessage(chat_id, refrigerante[1:] + 'de '+ tamanhoR)
           

    bot.sendMessage(chat_id, "No endereço: {}".format(endereco))
    bot.sendMessage(chat_id, 'Seu pedido chegara em instantes.')



def tamanhos(chat_id, msg):
###tamanhos pizza
    if (msg == 'Brotinho'):
        tamanhoP = 'Brothinho'
    elif (msg == 'Média'):
        tamanhoP = 'Média'
    elif (msg == 'Grande'):
        tamanhoP = 'Grande'
###tamanhos REFRIGERANTE
    elif (msg == '600 mL'):
        tamanhoR = '600 mL'
    elif (msg == '1.5L'):
        tamanhoR = '1.5L'
    elif(msg == '2L'):
        tamanhoR = '2L'

    elif (msg == 'Não quero bebidas'):
        tamanhoR = ''
    

MessageLoop(bot, inicio,{'chat': on_chat_message, 'callback_query': on_callback_query}).run_as_thread()

print ('Listening ...')

# Keep the program running.

while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(15)
