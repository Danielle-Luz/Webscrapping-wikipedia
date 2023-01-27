import requests;

class RandomWikipediaPage:
    url = "https://en.wikipedia.org/wiki/Wikipedia:Random"

    @staticmethod
    def getRandomWikipediaPage ():
        randomwWikipediaPage = requests.get(RandomWikipediaPage.url)
        pageHtml = randomwWikipediaPage.text()
        

RandomWikipediaPage.getRandomWikipediaPage()