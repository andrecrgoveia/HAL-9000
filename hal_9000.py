from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Name of the bot
bot = ChatBot('HAL 9000')
# Local database
bot = ChatBot(
    'HAL 9000',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3'
)
# Conversation in format of list
small_talk = ListTrainer(bot)
small_talk.train([
    'Hello',
    'Hi',
    'What is your name?',
    'My name is HAL 9000',
    'Are you a robot?',
    "Yes I'm a robot, and you?",
    "I'm a human",
    'Are you online?',
    "Yes I'm online right now",
    'Are you male?',
    "No, I don't have a sex, I'm a machine",
    'Are you female?',
    'Nice to meet you',
    'Nice to meet you to!',
    'Can you open the door?',
    "I’m sorry Dave, I’m afraid I can’t do that"
])
# Infinite loop to get responses
while True:
    try:
        resp = bot.get_response(input("User: "))
        if float(resp.confidence) > 0.5:
            print("HAL 9000: ", resp)
        else:
            print("I don't get it :(")
    except(KeyboardInterrupt, EOFError, SystemExit):
        break
