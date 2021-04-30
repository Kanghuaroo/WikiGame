import requests
from bs4 import BeautifulSoup

def getLinksOut(website):
    urlStart = 'https://en.wikipedia.org'
    res = requests.get(urlStart + website)
    txt = res.text

    soup = BeautifulSoup(res.content, 'html.parser')

    #get links 
    arr = []
    for link in soup.findAll('a'):
        temp = link.get('href')
        if temp and temp.startswith('/wiki/'):
                #print(temp)
                arr.append(temp)
    return arr

def getWikiOnlyLinks(arr):
    special = ['Category', 'Help', '%', '#', ':', '(identifier)', 'Timeline', 'Main_Page']
    flag = False
    uniqueLink = set()

    for link in arr:
        for char in special:
            if char in link:
                flag = True
                break
        if flag:
            flag = False
            continue
        uniqueLink.add(link)

    return uniqueLink

def breadthSearch(start, end, depth):
    queue = []
    #Path so far, next dir
    queue.append(([start], start))
    seen = set()
    seen.add(start)
   
    while len(queue) > 0:
        curr = queue.pop(0)
        
        nextLink = getWikiOnlyLinks(getLinksOut(curr[1]))
        for i in nextLink:
            #Don't do double takes
            if i in seen:
                continue
            else:
                seen.add(i)

            newPath = curr[0].copy()
            newPath.append(i)
            #check
            if i == end:
                return newPath

            queue.append((newPath, i))

start = '/wiki/Alan_Turing'
#end = 'https://en.wikipedia.org/wiki/World_War_II'
#end = '/wiki/Data'
#end = '/wiki/Computer_scientist'
#end = '/wiki/Midlands'
#end = '/wiki/Philosophy'
end = '/wiki/Algebraic_number'
#getWikiOnlyLinks(getLinksOut(start))
#tmp = getLinksOut(start)
#getWikiOnlyLinks(tmp)

tmp = breadthSearch(start, end, 0)
#print("=============================")
print(tmp)
