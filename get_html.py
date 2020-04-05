import requests
import argparse


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


def debug():
    parser = argparse.ArgumentParser()
    parser.add_argument('--tweet_url', '-t',
                        help='tweet URL ex: https://twitter.com/jack/status/20')
    args = parser.parse_args()

    html = get_html(args.tweet_url)
    print(html)


if __name__ == "__main__":
    debug()
