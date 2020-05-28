import requests
import re
from bot import Bot

def fetchWords(numberOfWords, toggleSwear):
    numberOfWords = str(numberOfWords)
    toggleSwear = str(toggleSwear)

    baseUrl = 'https://random-word-api.herokuapp.com/word'
    query = '?number={numberOfWords}&swear={toggleSwear}'

    response = requests.get(baseUrl + query.format(numberOfWords = numberOfWords, toggleSwear = toggleSwear))
    return response.json()


## MAIN
if __name__ == '__main__':
    words = fetchWords(100, 1)

    receiver = input('Select a receiver (give its serial number)')
    receiver = int(receiver)

    # init bot
    bot = Bot()
    # login on messenger
    bot.login()

    # select a chat
    bot.selectReceiver(receiver)

    # send messages
    for i in range(len(words)):
        bot.sendMessage(words[i])
