from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import default_reply
from slacker import Slacker
import slackbot_settings
import requests
import os

slacker = Slacker(slackbot_settings.API_TOKEN)
channel = 'fanart'
file_name = '.logs.txt'


@listen_to(r'twitter')
def get_tw_link(message):
    ch = get_channel(message)
    logs_overwrite(message, ch)


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


# @respond_to('del')
@listen_to('del')
def del_logs(message):
    ch = get_channel(message)
    os.system('echo '' > .logs{}.txt'.format(ch))
    message.send('delete logs')


# @respond_to('sum')
@listen_to('sum')
def up_summary(message):
    ch = get_channel(message)
    slacker.files.upload(file_=file_name, channels=ch)
    message.send('ファイルをアップロードしました')
    os.system('echo '' > .logs{}.txt'.format(ch))
    message.send('delete logs')


# @default_reply()
# def default(message):
#     import pdb
#     pdb.set_trace()
#     url = message.body['text'].strip('<').strip('>')
#     html = get_html(url)
#     message.send(html)

#     with open('.logs.txt', mode='a') as f:
#         f.write(html)


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
