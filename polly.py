import re
import boto3
import subprocess
import hashlib
import os.path
import os

def createMp3(text):
    #voiceid = "Mizuki"
    voiceid = "Takumi"
    filehash = hashlib.md5(text.encode('utf-8')).hexdigest()
    filepath = "/tmp/{}-{}.mp3".format(voiceid, filehash)

    if (not os.path.exists(filepath)):
        client = boto3.client(
            'polly',
            aws_access_key_id=os.environ["AWS_ACCESS_KEY"],
            aws_secret_access_key=os.environ["AWS_CLIENT_SECRET"],
            region_name=os.environ["AWS_REGION"]
        )
        response = client.synthesize_speech(
            OutputFormat='mp3',
            Text=text,
            TextType='text',
            VoiceId=voiceid
        ) 

        f = open(filepath, 'wb')
        f.write(response['AudioStream'].read())
        f.close()

    return filepath

if __name__ == '__main__':
  import sys
  createMp3(sys.argv[1])
