from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import default_reply
import requests


# # 「respond_to」はメンションする(@でターゲットを指定すること)と応答する
# @respond_to('こんにちは')
# def greeting_1(message):
#     # Slackに応答を返す
#     message.reply('こんにちは!')


# # 「listen_to」はメンションがなくても応答する
# @listen_to('コニチハ')
# def greeting_2(message):
#     message.reply('コニチハ')

@default_reply
def default_reply(message):
    url = message.body['text'].strip('<').strip('>')
    html = get_html(url)

    message.reply(html)


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
