import csv
import re
import collections
import gensim
import nltk
from gensim.parsing import remove_stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

slist = []
hlist = []
sDict = []
hDict = []
ps = PorterStemmer()


def stemSentence(sentence):
    token_words = word_tokenize(sentence)
    token_words
    stem_sentence = []
    for word in token_words:
        stem_sentence.append(ps.stem(word))
        stem_sentence.append(" ")
    return "".join(stem_sentence)


def word_count(lst):
    counts = dict()
    for item in lst:
        words = word_tokenize(item)

        for word in words:
            if word in counts:
                counts[word] += 1
            else:
                counts[word] = 1

    return counts


def writeFile(anyList, str):
    w = csv.writer(open(str, 'w'))
    for key, value in anyList.items():
        w.writerow([key, value])


with open('sms-spam-corpus.csv', newline='') as f:
    reader = csv.DictReader(f, delimiter=',')
    for row in reader:
        if row['v1'] == 'spam':

            slist.append(stemSentence(remove_stopwords(re.sub(r'[^A-Za-z]+', r' ', row['v2']).lower())))

        else:

            hlist.append(stemSentence(remove_stopwords(re.sub(r'[^A-Za-z]+', r' ', row['v2']).lower())))

    #print(slist)
    #print(hlist)
    amountOfHamSentence = len(hlist)
    amountOfSpamSentence = len(slist)
    all_sentence = amountOfHamSentence + amountOfSpamSentence
    P_Ham = amountOfHamSentence / all_sentence
    P_Spam = amountOfSpamSentence / all_sentence
    print("P(ham) =  ", P_Ham, "\nP(spam) = ", P_Spam)
    sDict = word_count(slist)
    hDict = word_count(hlist)
    s = input()
    l = s.split()
    #print(sDict)
    #print(hDict)
    sumS = 0
    sumH = 0
    prH = 1
    prS = 1
    i = 0
    for word in sDict:
        sumS += sDict[word]
    for word in hDict:
        sumH += hDict[word]
    print(sumS)
    print(sumH)
    for word in l:
        if word in sDict:
            prS *= (sDict[word]/sumS)
        else:
            if word in hDict:
                i += 1
                prS *= ((hDict[word]+1)/(sumH+i))
            else:
                i += 1
                prS *= (1/(sumH+i))

    pSBTxt = P_Spam*prS
    print(pSBTxt)
    for word in l:
        if word in hDict:
            prH *= (hDict[word]/sumH)
        else:
            if word in sDict:
                i += 1
                prH *= ((sDict[word]+1)/(sumS+i))
            else:
                i += 1
                prH *= (1/(sumS+i))
    pHBTxt = P_Ham*prH
    print(pHBTxt)
if pSBTxt>pHBTxt:
    print("this is spam")
else:
    print("this is ham")
