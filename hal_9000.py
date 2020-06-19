from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

hal_9000 = ChatBot(name='HAL 9000', read_only=True)

small_talk = ['Olá!', 'Oi', 'Como você está?', 'Eu estou bem', 'Tudo blz né?', 'Sempre!', 'Qual seu nome?', 'HAL 9000']

list_trainer = ListTrainer(hal_9000)

for intem in(small_talk):
    list_trainer.train(item)
    print(hal_9000.get_response('Olá'))