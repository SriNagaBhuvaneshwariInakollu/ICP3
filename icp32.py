import requests
from bs4 import BeautifulSoup


def get_links():
    url = "https://en.wikipedia.org/wiki/Deep_learning"
    sourceCode = requests.get(url)
    plainText= sourceCode.text
    soup=BeautifulSoup(plainText,"html.parser")
    result=soup.find_all('a')


    for anchors in result:
        print(anchors.get('href'))
    titlePrint = soup.title
    print('The title of the page is: ')
    print(titlePrint)

get_links()
