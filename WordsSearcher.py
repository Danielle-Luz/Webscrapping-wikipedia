from RandomWikipediaPage import RandomWikipediaPage

class WordsSearcher:
    @staticmethod
    def readSearchData():
        searchedWord = input("Digite a palavra buscada: ")

        while True:
            try:
                pagesQuantity = int(input("Digite o número de páginas com a palavra que devem ser obtidas: "))

                return {"pagesQuantity": pagesQuantity, "searchedWord": searchedWord}
            except:
                print("Digite um número inteiro.")

    @staticmethod
    def getTitlesFromPagesWithTheSearchedWord():
        pagesQuantity, searchedWord = WordsSearcher.readSearchData().values()
        foundPagesTitles = []
  
        while len(foundPagesTitles) <= pagesQuantity:
            pageContent, pageTitle = RandomWikipediaPage.getRandomWikipediaPage().values()

            if searchedWord in pageContent:
                foundPagesTitles.append(pageTitle)

        return foundPagesTitles

    @staticmethod
    def storeFoundPagesTitles():
        foundPageTitles = WordsSearcher.getTitlesFromPagesWithTheSearchedWord()

        with open("PagesTitles.md", "w", encoding="utf-8") as pagesTitlesFile:
            formattedFileText = "# Títulos das páginas" + "\n- ".join(foundPageTitles)

            pagesTitlesFile.write(formattedFileText)

        print("Os textos das páginas encontradas foram inseridos no arquivo: 'PagesTitles.md'")
    
WordsSearcher.storeFoundPagesTitles()