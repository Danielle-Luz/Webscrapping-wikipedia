import webbrowser
import string
from RandomWikipediaPage import RandomWikipediaPage


class WordsSearcher:
    @staticmethod
    def readSearchedWords():
        searchedWords = set()

        while True:
            word = input("Digite a palavra buscada: ")

            searchedWords.add(word)

            if input("Digite 1 caso queira inserir outra palavra: ") != "1":
                return searchedWords

    @staticmethod
    def readPagesQuantity():
        while True:
            try:
                pagesQuantity = int(
                    input("Digite o número de páginas com a palavra que devem ser obtidas: "))

                return pagesQuantity
            except:
                print("Digite um número inteiro.")

    @staticmethod
    def getTitlesFromPagesWithTheSearchedWord():
        pagesQuantity = WordsSearcher.readPagesQuantity()
        searchedWords = WordsSearcher.readSearchedWords()
        
        foundPagesTitles = []

        while len(foundPagesTitles) < pagesQuantity:
            pageContent, pageTitle, pageUrl = RandomWikipediaPage.getRandomWikipediaPage().values()

            pageContentWithoutPunctuation = pageContent.translate( pageContent.maketrans("", "", string.punctuation)).lower()

            pageContentWords = pageContentWithoutPunctuation.split(" ")

            pageContainsAllWords = all(
                [searchedWord.lower() in pageContentWords for searchedWord in searchedWords])

            if pageContainsAllWords:
                foundPagesTitles.append(pageTitle)
                webbrowser.open(pageUrl)

        return foundPagesTitles

    @staticmethod
    def storeFoundPagesTitles():
        foundPageTitles = WordsSearcher.getTitlesFromPagesWithTheSearchedWord()

        with open("PagesTitles.md", "w", encoding="utf-8") as pagesTitlesFile:
            formattedFileText = "# Títulos das páginas\n- " + \
                "\n- ".join(foundPageTitles)

            pagesTitlesFile.write(formattedFileText)

        print(
            "Os textos das páginas encontradas foram inseridos no arquivo: 'PagesTitles.md'")
