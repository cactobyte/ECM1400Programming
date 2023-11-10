import json

with open('gb-news.json', 'r') as f:
    news_dict = json.load(f)
    articles = news_dict["articles"]
    for article in articles:
        print(article['title'])
