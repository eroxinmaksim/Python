import csv
import re
from gensim.parsing.preprocessing import remove_stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

with open('sms-spam-corpus.csv', newline='') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=',')
    spam_list = []
    ham_list = []
    for row in csv_reader:
        if row['v1'] == "ham":
            ham_list.append((row['v2']).lower())
        elif row['v1'] == "spam":
            spam_list.append((row['v2']).lower())

port_stem = PorterStemmer()


def stemming(rows):
    words_list = []
    token_list = word_tokenize(rows)
    for word in token_list:
        words_list.append(port_stem.stem(word))
        words_list.append(" ")
    return "".join(words_list)


word_list_h = []
for row in ham_list:
    word_list_h.append(stemming(remove_stopwords(re.sub('[^a-z]', ' ', row))))

word_list_s = []
for row in spam_list:
    word_list_s.append(stemming(remove_stopwords(re.sub('[^a-z]', ' ', row))))

dict_spam = []
dict_ham = []


def word_count(lists):
    result = dict()
    for item in lists:
        words_list = word_tokenize(item)
        for word in words_list:
            if word in result:
                result[word] += 1
            else:
                result[word] = 1
    return result


dict_spam = word_count(word_list_s)
dict_ham = word_count(word_list_h)

wr1 = open('spam_file.csv', 'w')
with wr1:
    writer1 = csv.writer(wr1)

    for key, value in dict_spam.items():
        writer1.writerow([key, value])


wr2 = open('ham_file.csv', 'w')
with wr2:
    writer2 = csv.writer(wr2)

    for key, value in dict_ham.items():
        writer2.writerow([key, value])
