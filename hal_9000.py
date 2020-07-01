from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('HAL 9000')

# Criando uma lista
conversa = []

bot.set_trainer(ListTrainer)
bot.train(conversa)

while True:
    pergunta = input('VocÊ')
    resposta = bot.get_response(pergunta)
    if float(resposta.confidence) > 0.5:
        print('HAL 9000: ', resposta)
    else:
        print('HAL 9000: ')
