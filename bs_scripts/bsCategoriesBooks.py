import requests
from bs4 import BeautifulSoup

def extract_categories_books() :
    url = "http://books.toscrape.com/"
    try :
        response = requests.get(url)
    except :
        pb = "Un problème de connexion est survenue, pas de code Réponse 200"
        return pb
    if response.ok:
        soup = BeautifulSoup(response.text, 'lxml')
        categoriesBook = {}
        # extraction des "li" présent dans la 2e div de l'aside
        # sinon extrait que le lien Book
        liInAside = soup.aside.li.a.find_next().findAll("li")
        for element in liInAside:
            a = element.find("a")
            link = url + a["href"]

            # extraction du nom de la catégorie
            for content in a.contents:
                """ Modification String title car sinon : 
                '\n                            \n                                Health\n                            \n                        '
                """
                title = content.split("\n")
                title = title[2].strip("  ")
            categoriesBook[title] = link
        return categoriesBook
