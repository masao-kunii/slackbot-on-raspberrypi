# slackbot-on-rasberrypi
## Overview
Basic slackbot implementation using [slackbot](https://github.com/lins05/slackbot).

## Feature
- Speak texts in slack channel by `say` command. 
- Speak error log and URI in alert message in slack channel.
- You can see `plugins/plugin.py` for other features.

## Pre-requisite
- OS: Raspbian
- Any speaker device HDMI or 3.5mm jack
- Python3 and pip3
- Export these environment variables
  - AWS_CLIENT_SECRET
  - AWS_ACCESS_KEY
  - AWS_REGION
  - SLACK_API_TOKEN

## Installation & Run
1.Install python libraries 
```
pip3 install -r requirements.txt
```
2.Export environment variables
3.Execute `python3 run.py`
4.If you want to run as a daemon edit `slackbot.service` and copy it to `/etc/systemd/system`

## Help
If you cannot install `pygame`, install the dependencies.
```
sudo apt-get install libsdl-dev libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev
sudo apt-get install libsmpeg-dev libportmidi-dev libavformat-dev libswscale-dev
```

