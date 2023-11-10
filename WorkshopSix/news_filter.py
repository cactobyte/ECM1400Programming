import json

keywords = ["covid", "bbc"]

def get_news(keywords, articles):
    for article in articles:
        for words in keywords:
            if words in article["title"].lower():
                print(article["title"])
    return


with open('gb-news.json', 'r') as f:
    news_dict = json.load(f)
    articles = news_dict["articles"]

    get_news(keywords, articles)

    for article in articles:
        for words in keywords:
            if words in article["title"].lower():
                print(article["title"])

