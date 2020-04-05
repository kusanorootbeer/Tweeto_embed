import requests
import argparse

# Reference
#      https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference/get-statuses-oembed


def get_html(tweet_url):
    params = (
        ('url', tweet_url),
        ('data-conversation', 'none'),
        ('lang', 'ja'),
    )
    response = requests.get(
        'https://publish.twitter.com/oembed', params=params)
    html = "".join(response.json()['html'].split('\n'))
    print(html)


def debug():
    parser = argparse.ArgumentParser()
    parser.add_argument('--tweet_url', '-t',
                        help='tweet URL ex: https://twitter.com/jack/status/20')
    args = parser.parse_args()

    get_html(args.tweet_url)


if __name__ == "__main__":
    debug()
