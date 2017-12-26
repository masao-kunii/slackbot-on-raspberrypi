from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re
import boto3
import subprocess
import time
import hashlib
import os.path
from random import shuffle

from plugins.error_handler import onError
from plugins.error_handler import onErrorWithText
from polly import createMp3 
from player import play

@respond_to('hi', re.IGNORECASE)
def hi(message):
    message.reply('I can understand hi or HI!')
    # react with thumb up emoji
    message.react('+1')

@respond_to('I love you')
def love(message):
    message.reply('I love you too!')

@respond_to('show ip')
def showIp(message):
    res = subprocess.Popen(['ip', 'addr'], stdout=subprocess.PIPE, shell=False)
    message.reply(str(res.stdout.readlines()))

@respond_to('say')
def say(message):
    channel = message.body['channel']
    fulltext = message.body['text']
    cmd, text = fulltext.split(None, 1)
    
    filepath = createMp3(text)
    print(filepath)
    play(filepath) 

    message.reply(text)

@listen_to('.*')
def hearall(message):
    print(str(message.body))
    subtype = message.body.get('subtype', '')
    botId = message.body.get('bot_id', '')
    channel = message.body.get('channel', '')
    print('subtype:{} channel:{} botId:{}'.format(subtype, channel, botId))

    # Handle bot message
    if (botId == ''): 
        print('not a bot!'+ botId + subtype)
        return 

    attachment = message.body.get('attachments', '')
    print('attachment type:{} is list {}'.format(type(attachment), isinstance(attachment, list)))
    onError(message)

@respond_to('error')
def error(message):
    channel = message.body['channel']
    fulltext = message.body['text']
    print("channel:{} fulltext:{}".format(channel, fulltext))
    cmd, text = fulltext.split(None, 1)
    onErrorWithText(channel, text)

@listen_to('show message obj')
def showMessage(message):
    message.reply(str(message.body))

@listen_to('play')
def showMessage(message):
    channel = message.body['channel']
    fulltext = message.body['text']
    print("channel:{} fulltext:{}".format(channel, fulltext))
    cmd, filename = fulltext.split(None, 1)
    filepath="mp3/{}".format(filename)
    if os.path.exists(filepath):
       play(filepath)
       message.reply("I'm playing {} for you".format(filename))
    else:
       message.reply("I don't have such file.")
