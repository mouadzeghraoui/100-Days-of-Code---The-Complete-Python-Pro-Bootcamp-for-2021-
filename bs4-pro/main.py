from bs4 import BeautifulSoup
import requests
import pandas as pd

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")


articles = soup.select(selector=".storylink")
article_texts = [article_text.string for article_text in soup.select(selector=".storylink")]
print(article_texts)
article_links = [article_link.get("href") for article_link in soup.select(selector=".storylink")]
print(article_links)
article_upvotes = [article_upvote.string for article_upvote in soup.select(selector=".score")]
article_upvotes = [article_upvote.split(" ")[0] for article_upvote in article_upvotes]
print(article_upvotes)

d = {'Title': article_texts[0:29], 'Link': article_links[0:29], 'UpVote': article_upvotes}
df = pd.DataFrame(data=d)
print(df.head())

