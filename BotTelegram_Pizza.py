#!/usr/bin/env python
# coding: utf-8

#imports para o boot
import sys
import time
import telepot
import telegram
#opção para botão: types
#from telebot import types

from telepot.loop import MessageLoop

from telepot.namedtuple import ForceReply, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton



nivel = 0
nome= []
endereco= []
pizza = ''
refrigerante = ''
tamanhoP = ''
tamanhoR = ''
confirm = ''
def handle(msg):
    global pizza
    global tamanhoP
    global refrigerante
    global tamanhoR
    
    global confirm
    global nivel
    global usuario
    global nome
    global endereco
    content_type, chat_type, chat_id = telepot.glance(msg)
    #print(content_type, chat_type, chat_id)
    
          
    #Cardápios
    cardapio_pizza= {1:'1 pizza calabreza', 2:'2 pizza 4 queijos', 3: '3 pizza escarola'}
    cardapio_refri= {1:'1 Coca-cola', 2:'2 Fanta-uva', 3:'3 Guaraná'}
    
    #usuário cadastro
    if nivel == 0:
        if content_type == 'text':  
            bot.sendMessage(chat_id, 'olá, Qual seu nome?')
            
        nivel+=1
    elif nivel == 1:
        if content_type =='text':
            nome.append(msg['text'])
            bot.sendMessage(chat_id, 'Qual seu endereço?')
           
        nivel+=1
    elif nivel == 2:
        if content_type =='text':
            endereco.append(msg['text'])
            bot.sendMessage(chat_id, 'Faça seu pedido, digite o numero para a opção para pizza')
            
            for i in cardapio_pizza:
                bot.sendMessage(chat_id, cardapio_pizza[i])                
                
        nivel+=1

    
    elif nivel == 3:
        if content_type == 'text':
            pizza = cardapio_pizza[int(msg['text'])]
            bot.sendMessage(chat_id, 'qual o tamanho da pizza?')
            
        nivel+=1
    
    #confirmar pizza
  
    elif nivel == 4:
        if content_type == 'text':
            tamanhoP = msg['text']
            bot.sendMessage(chat_id, 'Mais alguma?')
        
        
            if (msg['text'].lower() == 'sim' or msg['text'].lower() == 's'):
                nivel = 2
            elif (msg['text'].lower() == 'não' or msg['text'].lower() == 'n' or msg['text'].lower() == 'nao'):
                nivel = 5
            else:
                nivel =4
        nivel+=1
        
     #pedidio refri
    elif nivel == 5:
        if content_type =='text':
           
            bot.sendMessage(chat_id, 'Faça seu pedido, digite o numero para a opção para refrigerante')
            
            for refrigerante in cardapio_refri:
                bot.sendMessage(chat_id, cardapio_refri[refrigerante])                
                
        nivel+=1

    
    elif nivel == 6:
        if content_type == 'text':
            refrigerante = cardapio_refri[int(msg['text'])]
            bot.sendMessage(chat_id, 'qual o tamanho do refrigerante?')
        nivel+=1
    
    #confirmar REFRI
    elif nivel == 7:
        if content_type == 'text':
            tamanhoR = msg['text']
            bot.sendMessage(chat_id, 'Mais alguma?')
            if(msg['text'].lower() == 'sim' or msg['text'].lower() == 's'):
                nivel = 5
            elif (msg['text'].lower() == 'não' or msg['text'].lower() == 'n' or msg['text'].lower() == 'nao'):
                nivel = 6
            else:
                nivel = 7
        nivel+=1
        
    ### Confirmação de pedido ___Terminar isso___
    
    elif nivel == 8:
        if content_type == 'text':
            bot.sendMessage(chat_id, 'Seu pedido é: ')
            bot.sendMessage(chat_id, pizza[1:])
            bot.sendMessage(chat_id, tamanhoP)
            bot.sendMessage(chat_id, refrigerante[1:])
            bot.sendMessage(chat_id, tamanhoR)

            bot.sendMessage(chat_id, "No endereço: {}".format(endereco[0]))
            bot.sendMessage(chat_id, 'Posso confirmar?')
        nivel+=1;
    
    elif nivel == 9:
        if content_type == 'text':
            
            if(msg['text'].lower() == 'sim' or msg['text'].lower() == 's'):
                nivel = 0
            elif (msg['text'].lower() == 'não' or msg['text'].lower() == 'n' or msg['text'].lower() == 'nao'):
                nivel = 0
    
        
TOKEN = sys.argv[1:]  # get token from command-line

bot = telepot.Bot(token='830025759:AAGFXGtpWrWyEkWI_eQO1Q6karejEZv8Yxs')
MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
