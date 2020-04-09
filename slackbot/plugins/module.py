from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import default_reply
from slacker import Slacker
import slackbot_settings
import requests
import os

slacker = Slacker(slackbot_settings.API_TOKEN)
channel = 'fanart'
file = '.logs.txt'


@respond_to('del')
def del_logs(message):
    slacker.files.upload(file_=file, channel=channel)
    os.system('echo '' > .logs.txt') 
    message.reply('delete logs')


@respond_to('sum')
def up_summary(message):
    slacker.files.upload(file_=file, channels=channel)
    message.send('ファイルをアップロードしました')
    os.system('echo '' > .logs.txt')
    message.reply('delete logs')


@default_reply
def default_reply(message):
    url = message.body['text'].strip('<').strip('>')
    html = get_html(url)
    message.reply(html)

    with open('.logs.txt', mode='a') as f:
        f.write(html)


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
