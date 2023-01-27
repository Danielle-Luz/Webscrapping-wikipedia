from RandomWikipediaPage import RandomWikipediaPage

class WordsSearcher:
    def readSearchData():
        searchedWord = input("Digite a palavra buscada: ")

        while True:
            try:
                pagesQuantity = int(input("Digite o número de páginas com a palvra que devem ser obtidas: "))

                return {"pagesQuantity": pagesQuantity, "searchedWord": searchedWord}
            except:
                print("Digite um número inteiro.")

    