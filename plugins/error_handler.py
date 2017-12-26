from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re
import boto3
import time

from polly import createMp3 
from player import play

def onError(message):
    channel = message.body.get('channel', '')
    attachments = message.body.get('attachments', '')
    title = attachments[0].get('title','')
    text = attachments[0].get('text','')  + message.body.get('text', '')
    # service name is supporsed to be in the title
    service = re.findall('my\.service\.keyword\.here\.(\S*)', title)
    if (len(service) < 1):
        return
    
    onErrorWithText(service, text)

def onErrorWithText(serviceName, text):
    #looking for URI from text and extract the second path. (URI is supporsed to be like "uri=/api/<domain>/xxx" in the text)
    endpoint = set(re.findall('[\[=]\/\w*\/([\w-]{1,20}).*', text))
    textToSpeech = 'An error occured around {} {}'.format([x + " of" for x in endpoint], serviceName)
    filepath = createMp3(textToSpeech)
    play(filepath)
    time.sleep(60)

