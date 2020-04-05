# coding: utf-8
import json

with open('./slackbot/plugins/.config.json') as f:
    jdata = json.load(f)

# botアカウントのトークンを指定
API_TOKEN = jdata['API_TOKEN']


# プラグインスクリプトを置いてあるサブディレクトリ名のリスト
PLUGINS = ['plugins', 'plugins.module']
