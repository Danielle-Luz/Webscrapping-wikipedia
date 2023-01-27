import requests
from bs4 import BeautifulSoup


class RandomWikipediaPage:
    url = "https://pt.wikipedia.org/wiki/Special:Random"

    @staticmethod
    def getRandomWikipediaPage():
        randomwPage = requests.get(RandomWikipediaPage.url)
        randomPageHtml = randomwPage.text

        soupObject = BeautifulSoup(randomPageHtml, "html.parser")

        pageContetWithoutSpaces = soupObject.find(
            id="mw-content-text").get_text().strip().replace("\n", " ")

        return pageContetWithoutSpaces
