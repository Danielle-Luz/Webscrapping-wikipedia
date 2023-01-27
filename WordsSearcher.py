from RandomWikipediaPage import RandomWikipediaPage

class WordsSearcher:
    def readPagesQuantity():
        while True:
            try:
                pagesQuantity = int(input("Digite o número de páginas com a palvra que devem ser obtidas: "))

                return pagesQuantity
            except:
                print("Digite um número inteiro.")