#imports para o boot
import sys
import time
import telepot
import telegram
from unidecode import unidecode
#opção para botão: types
#from telebot import types

from telepot.loop import MessageLoop

from telepot.namedtuple import ForceReply, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

TOKEN = sys.argv[1:]  # get token from command-line

nivel = 0
nome= ''
endereco= ''
complemento = ''
pizza = []
refrigerante = []
tamanhoP = []
tamanhoR = []

def handle(msg):
    global nome, endereco, complemento
        
    global pizza, tamanhoP
    global refrigerante, tamanhoR
    global nivel
    
    content_type, chat_type, chat_id = telepot.glance(msg)
    #print(content_type, chat_type, chat_id)
    
          
    #Cardápios
    cardapio_pizza= {1:'1 Pizza calabreza', 2:'2 Pizza 4 queijos', 3: '3 Pizza escarola'}
    cardapio_refri= {1:'1 Coca-cola', 2:'2 Fanta-uva', 3:'3 Guaraná'}
    
    #usuário cadastro
    if nivel == 0:
        if content_type == 'text':  
            bot.sendMessage(chat_id, 'Olá, Qual seu nome?')
            
        nivel+=1
    elif nivel == 1:
        if content_type =='text':
            nome = msg['text']
            bot.sendMessage(chat_id, 'Espero poder te ajudar '+ nome+', me chamo PizzaBoy e vou anotar seu pedido')
            bot.sendMessage(chat_id, 'Informe seu endereco.')                            
        nivel+=1
        
    elif nivel == 2:
    
        endereco = (msg['text'])
        bot.sendMessage(chat_id, 'Informe o complemento.')  
        nivel+=1
    elif nivel ==3:
        complemento = (msg['text'])
        bot.sendMessage(chat_id, 'Faça seu pedido, digite o numero para a opção para pizza')
            
        for piz in cardapio_pizza:
            bot.sendMessage(chat_id, cardapio_pizza[piz])                
                
        nivel+=1
           
    elif nivel == 4:
        if content_type == 'text':
            print("Nivel 3")
            pizza.append(cardapio_pizza[int(msg['text'])])
            keyboard=ReplyKeyboardMarkup(
            keyboard=[[
                    KeyboardButton(text="Brotinho"),
                    KeyboardButton(text="Média"),
                    KeyboardButton(text="Grande"),
                                
                        ]],resize_keyboard=True)
            bot.sendMessage(chat_id, 'Qual o tamanho da pizza?', reply_markup=keyboard) 
            
            nivel+=1
    
    #confirmar pizza
  
    elif nivel == 5:
        if content_type == 'text':
            print("Nivel 4")
            tamanhoP.append(msg['text'])
            keyboard=ReplyKeyboardMarkup(
            keyboard=[[
                    KeyboardButton(text="Sim"),
                    KeyboardButton(text="Não")                             
                        ]],resize_keyboard=True)
            bot.sendMessage(chat_id, 'Mais alguma?', reply_markup=keyboard )

        nivel+=1
    elif nivel == 6:
        print("Nivel 5")
        if (msg['text'].lower() == 'sim'):
            print("Nivel 5 sim")
            bot.sendMessage(chat_id, 'Faça seu pedido, digite o numero para a opção para pizza')
            nivel = 4
        elif (unidecode(msg['text'].lower()) == 'nao'):

            bot.sendMessage(chat_id, 'Faça seu pedido, digite o numero para a opção para refrigerante')
            
            for ref in cardapio_refri:
                bot.sendMessage(chat_id, cardapio_refri[ref])                
                
            nivel = 7

    
    elif nivel == 7:
        if content_type == 'text':
            print("Nivel 7")
            
            refrigerante.append(cardapio_refri[int(msg['text'])])
            
            keyboard=ReplyKeyboardMarkup(
            keyboard=[[
                    KeyboardButton(text="600 mL"),
                    KeyboardButton(text="1.5 L"),
                    KeyboardButton(text="2 L"),
                                
                        ]],resize_keyboard=True)
            bot.sendMessage(chat_id, 'qual o tamanho do refrigerante?', reply_markup=keyboard )
            
        nivel+=1
    
    #confirmar REFRI
    elif nivel == 8:
        if content_type == 'text':
            print("Nivel 8")
            tamanhoR.append(msg['text'])
            keyboard=ReplyKeyboardMarkup(
            keyboard=[[
                    KeyboardButton(text="Sim"),
                    KeyboardButton(text="Não")                             
                        ]],resize_keyboard=True)
            bot.sendMessage(chat_id, 'Mais alguma?', reply_markup=keyboard )
            

        nivel+=1
        
    ### arrumar nivel 9 sim e nao
    
    elif nivel == 9:
        if content_type == 'text':
            print("Nivel 9")
            if(msg['text'].lower() == 'sim'):
                print("Nivel 9 sim")
                bot.sendMessage(chat_id, 'Faça seu pedido, digite o numero para a opção para refrigerante')
                nivel = 7
            elif (unidecode(msg['text'].lower()) == 'nao'):
                print("Nivel 9 nao")
                bot.sendMessage(chat_id, 'Obrigado '+ nome +', seu pedido é: ')
                for k in range(len(pizza)):
                    bot.sendMessage(chat_id, pizza[k][2:] + ' de tamanho ' + tamanhoP[k])
                for m in range(len(refrigerante)):
                    bot.sendMessage(chat_id, refrigerante[m][2:]+ ' de '+ tamanhoR[m])

                nivel = 10

                
    elif nivel == 10:
        if content_type == 'text':
            print("Nivel 10")
            
            #bot.sendMessage(chat_id, "No endereço: {}".format(endereco[0]))
                            
            keyboard=ReplyKeyboardMarkup(
            keyboard=[[
                    KeyboardButton(text="Sim"),
                    KeyboardButton(text="Não")                             
                        ]],resize_keyboard=True)
            bot.sendMessage(chat_id, 'Posso confirmar?', reply_markup=keyboard )
        nivel+=1
    
    elif nivel == 11:
        if content_type == 'text':
            print("Nivel 11")
            if (msg['text'].lower() == 'sim'):
                print("Nivel 11 sim")
                bot.sendMessage(chat_id, 'Obrigado pela preferência!')
            elif (unidecode(msg['text'].lower()) == 'nao'):
                print("Nivel 11 nao")
                pizza = []
                refrigerante = []
                tamanhoP = []
                tamanhoR = []
                nivel = 2


bot = telepot.Bot(token='830025759:AAGFXGtpWrWyEkWI_eQO1Q6karejEZv8Yxs')
MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)

