import requests
from bs4 import BeautifulSoup

def getLinksOut(website):
    res = requests.get(website)
    txt = res.text

    soup = BeautifulSoup(res.content, 'html.parser')

    #get links 
    arr = []
    for link in soup.findAll('a'):
        temp = link.get('href')
        if temp and ('https://') in temp:
            print(link.get('href'))
            arr.append(temp)

start = 'https://en.wikipedia.org/wiki/Alan_Turing'
end = 'https://en.wikipedia.org/wiki/World_War_II'
getLinksOut('https://webkinz.com')
