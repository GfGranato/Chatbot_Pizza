# Chatbot_Pizza
>Trabalho da matéria Interação Humano Computador, da Fatec SJC.

## Introdução

Esse trabalho tem como objetivo desenvolver um bot para o **TELEGRAM** utilizando a biblioteca **_Telepot_** devido a sua varidedade de funções para efetuar diversas tarefas. Para acessar a documentação do Telepot clique [aqui](https://telepot.readthedocs.io/en/latest/)

## Principais Funções
Utilizamos um sistema para pedir pizza com as seguintes funções:
* _sendMessage_;
* _sendPhoto_;
* _InlineKeyboardMarkup_; e
* _KeyboardButton_. 

### Descrição
Para o funcionamento do sendPhoto foi adicionado no diretório do GitHub uma [imagem do cardápio](https://github.com/GfGranato/Chatbot_Pizza/blob/master/pizzaboy.PNG) cujo link é utilizado pela função.

O sistema utiliza uma lógica de níveis para o envio e recebimento das mensagens, sendo que no útimo nível ele acrescenta um valor na variável nivel para que o bot não fique em loop infinito. o sistema de nível foi o mais viável devido a variação de mensagens de texto que podem ser escritas. Com isso, após o envio de um texto, o bot inicia seu determinado nível.

##### Caso tenha alguma dúvida, entre em contato comigo.

