import requests
from bs4 import BeautifulSoup as bs4
import pprint
# gets articles with score > 99 on front page of hacker news (30 in a pool)

res = requests.get("https://news.ycombinator.com/news?p=1")
soup = bs4(res.text, "html.parser")
links = soup.select(".storylink")
votes = soup.select(".score")


def create_custom_hn(links, votes):
    hn = []
    for index, item in enumerate(links):
        title = links[index].getText()
        href = links[index].get("href", None)
        try:
            points = int(votes[index].getText().replace(" points", ""))
        except IndexError:
            points = 0
        if points > 99:
            hn.append({"title": title, "link": href, "score": points})
            hn.sort(key=lambda k: k["score"], reverse=True)
    return hn


pprint.pprint(create_custom_hn(links, votes))
