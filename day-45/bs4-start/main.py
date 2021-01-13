from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
articles = soup.find_all(name="a", class_="storylink")
texts = []
links = []
for article_tag in articles:
    texts.append(article_tag.getText())
    links.append(article_tag.get("href"))


article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
largest_number = max(article_upvote)
largest_index = article_upvote.index(largest_number)

print(texts[largest_index])
