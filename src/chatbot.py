from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

import logging, os

logger = logging.getLogger()
logger.setLevel(logging.CRITICAL)


class Bot:
    def __init__(self):
        self.bot = ChatBot(
            "Bot 1",
            storage_adapter='chatterbot.storage.SQLStorageAdapter',
            logic_adapters=[
                'chatterbot.logic.MathematicalEvaluation',
                'chatterbot.logic.BestMatch'
            ],
            database_uri='sqlite:///database.sqlite3'
        )
        self.trainer = ListTrainer(self.bot)
        self.responses = list()

    def train(self):
        with open(os.getcwd()+'\\src\\responses.txt') as file:
            for line in file:
                self.responses.append(line.rstrip())

        print(self.responses)
        self.trainer.train(self.responses)


if __name__ == "__main__":
    bot = Bot()
    bot.train()
    while True:
        try:
            bot_input = bot.bot.get_response(input())
            print(bot_input)

        except(KeyboardInterrupt, EOFError, SystemExit):
            break
