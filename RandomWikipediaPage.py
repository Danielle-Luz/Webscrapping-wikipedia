import requests
import re
from bs4 import BeautifulSoup


class RandomWikipediaPage:
    url = "https://pt.wikipedia.org/wiki/Special:Random"

    @staticmethod
    def getRandomWikipediaPage():
        randomwPage = requests.get(RandomWikipediaPage.url)
        randomPageHtml = randomwPage.text

        soupObject = BeautifulSoup(randomPageHtml, "html.parser")

        pageTitle = soupObject.find("title").get_text()
        pageContetStripped= soupObject.find(
            id="mw-content-text").get_text().strip()
        pageContetWithoutSpaces = re.sub(r'\s+', " ", pageContetStripped)

        return [pageContetWithoutSpaces, pageTitle]
