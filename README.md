# Tweeto_embed

slack の Bot 作ってる．
Bot に tweet のリンクを，送ると，それを HTML 形式で埋め込める形にしてくれる．
(WordPress 用)

## Process
- tweetのリンクを送ると，HTML形式で埋め込んだ形で返してくれる．
- sum と送ると，そのchannelで，これまでのHTMLをまとめて返してくれる．(logは消える)
- del と送ると，そのchannelのlogを消す．


## Demo
![demo](https://user-images.githubusercontent.com/49409264/79048469-38322c80-7c58-11ea-8144-4d0f16867410.gif)
## Reference

- https://github.com/lins05/slackbot
- https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference/get-statuses-oembed
