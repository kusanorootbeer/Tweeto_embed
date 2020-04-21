from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import default_reply
from slacker import Slacker
import slackbot_settings
import requests
import os

slacker = Slacker(slackbot_settings.API_TOKEN)
# channel = 'fanart'
# file_name = '.logs.txt'


@listen_to(r'twitter')
def get_tw_link(message):
    ch = get_channel(message)
    logs_overwrite(message, ch)


@listen_to(r'^del$')
def del_logs(message):
    ch = get_channel(message)
    os.system('echo '' > .logs_{}.txt'.format(ch))
    message.send('delete logs')


@listen_to(r'^sum$')
def up_summary(message):
    ch = get_channel(message)
    file_name = '.logs_{}.txt'.format(ch)
    slacker.files.upload(file_=file_name, channels=ch)
    message.send('ファイルをアップロードしました')
    os.system('echo '' > .logs_{}.txt'.format(ch))
    message.send('delete logs')
    


def get_html(tweet_url):
    params = (
        ('url', tweet_url),
        ('data-conversation', 'none'),
        ('lang', 'ja'),
    )
    response = requests.get(
        'https://publish.twitter.com/oembed', params=params)
    html = "".join(response.json()['html'].split('\n'))
    return html


def get_channel(message):
    try:
        channel_name = message.channel._body['name']
    except:
        channel_name = ''
    return channel_name


def logs_overwrite(message, ch):
    url = message.body['text'].strip('<').strip('>')
    html = get_html(url)
    message.send(html)

    with open('.logs_{}.txt'.format(ch), mode='a')as f:
        f.write(html)
