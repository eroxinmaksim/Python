import math
import re
import networkx as nx
import matplotlib.pyplot as plt
import operator

import numpy
from bs4 import BeautifulSoup
import requests

# url = "https://www.winealign.com/privacy"
url = "http://vega-craft.ru/"

badExtentions=['.digital','.hash','.eps','.ppt','.pptx','.pdf','.jpeg','.jpg','.png','.gif','.rar','._gromad','.doc','.txt','.xls','.xml','.zip']
d=0.5
E=0.001
allKink=[]
G=nx.DiGraph()
dictNumToLink=dict()
dictNumToCountOfLink=dict()


chekedLink=[]

def cleanFromHTTPorHTTPS(url):
    if(url[4]=='s'):
        return url[5:]
    else:
        return url[4:]

def validation(href):
    for i in badExtentions:
        if i in href:
            return False
    return True

numOfLink=0
def recursion(mHref):
    global numOfLink
    global dictNumToLink
    chekedLink.append(mHref)
    internalLink=[]
    page = requests.get(mHref)
    data = page.text
    soup = BeautifulSoup(data, "html.parser")
    for link in soup.find_all('a', href=re.compile('^(/)')):
        href = link.get('href')
        href = url + href[1:]
        if(validation(href)):
            if href not in dictNumToLink.keys():
                dictNumToLink[href] = numOfLink
                numOfLink = numOfLink + 1
            internalLink.append(href)
            G.add_edge(dictNumToLink[mHref], dictNumToLink[href])
            if href in chekedLink:
                continue
            recursion(href)

    allSoup = soup.find_all('a', href=re.compile('^http[s]{0,1}' + urlCut + '.*\.html'))
    allSoup = allSoup + soup.find_all('a', href=re.compile('^http[s]{0,1}' + urlCut + '.*$'))
    for link in allSoup:
        href = link.get('href')
        if (validation(href)):
            internalLink.append(href)
            if href not in dictNumToLink.keys():
                dictNumToLink[href] = numOfLink
                numOfLink = numOfLink + 1
            G.add_edge(dictNumToLink[mHref], dictNumToLink[href])
            if href in chekedLink:
                continue
            recursion(href)
    dictNumToCountOfLink[dictNumToLink[mHref]]= len(internalLink)
    G.add_node(dictNumToLink[mHref])
    return

def yakobi(B):
    global dictNumToLink
    solveVector=[]
    newvector = []
    for i in range(0, len(B)):
        solveVector.append(B[i][len(B)])
    eps=1
    while eps>E:
        for i in range(0, len(B)):
            sum=0
            for j in range(0, len(solveVector)):
                sum=sum+solveVector[j]*B[i][j]
            sum=sum+B[i][len(B)]
            newvector.append(sum)
        eps=0
        for j in range(0, len(solveVector)):
            eps=eps+math.fabs(newvector[j]-solveVector[j])

        solveVector=newvector.copy()
        newvector.clear()
    finalDict=dict()
    for j in range(0, len(solveVector)):
        finalDict[j]=solveVector[j]
    finalDict=sorted(finalDict.items(), key=operator.itemgetter(1),reverse=True)
    print(finalDict)
    for j in range(0,10):
        print(j+1,list(dictNumToLink.keys())[list(dictNumToLink.values()).index(finalDict[j][0])],"pr:",finalDict[j][1])

urlCut=cleanFromHTTPorHTTPS(url)
dictNumToLink[url]=numOfLink
numOfLink=numOfLink+1
recursion(url)


nx.draw(G,with_labels=True)
plt.show()
print(dictNumToLink)
B = [[0 for x in range(len(G.nodes)+1)] for y in range(len(G.nodes))]
for n in G.edges:
    B[n[1]][n[0]] = d / dictNumToCountOfLink[n[0]]
for i in range(0, len(G.nodes)):
    B[i][len(G.nodes)]=1-d
yakobi(B)
