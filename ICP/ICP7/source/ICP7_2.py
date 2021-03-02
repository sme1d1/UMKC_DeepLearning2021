# Scott McElfresh ICP 7-2 sme1d1

import requests
from bs4 import BeautifulSoup

'''
page = requests.get("https://en.wikipedia.org/wiki/Google")  # specified webpage to scrape info from

with open('input.txt', 'a', encoding='utf-8') as writer:
    soup = BeautifulSoup(page.content, 'html.parser')
    #print(soup)
    text = soup.find_all(text=True)
    zed = {t.parent.name for t in text}
    #print(zed)
    bigString = ''
    garbage = [
        'html',
        'head',
        'meta',
        'script',
        'header',
        'li',
        'div',
        'ul',
        '[document]',
        'style',
            ]

    for t in text:
        if t.parent.name not in garbage:
            bigString +='{} '.format(t)
    bigString = bigString.replace("\\", "")
    bigString = bigString.replace("\n", "")
    writer.write(bigString)
'''
#import nltk
#nltk.download('maxent_ne_chunker')
#nltk.download('words')

from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from nltk import ngrams
from nltk import wordpunct_tokenize, ne_chunk
with open('input.txt', 'r', encoding='utf-8') as reader:
    bigString = reader.read()
    # print(bigString)

    # Tokenization

    stokens = sent_tokenize(bigString)  # sentence tokenization
    wtokens = word_tokenize(bigString)  # word tokenization
    # print(stokens)
    # for s in stokens:
    #    print(s)
    #for w in wtokens:
    #    print(w)

    # POS

    pos = pos_tag(wtokens)  # POS on words
    # print(pos)

    # Stemming

    ps = PorterStemmer()
    ls = LancasterStemmer()
    ss = SnowballStemmer('english')

    stemlist_P = []
    stemlist_L = []
    stemlist_S = []

    for w in wtokens:
        stemlist_P.append((w + " : " + ps.stem(w)))
        stemlist_L.append((w + " : " + ls.stem(w)))
        stemlist_S.append((w + " : " + ss.stem(w)))
    #print(stemlist_P)

    # Lemmatization
    lemlist = []
    lem = WordNetLemmatizer()
    for w in wtokens:
        lemlist.append((w + " : " + lem.lemmatize(w)))
    #print(lemlist)

    # Trigrams
    trilist = ngrams(bigString.split(), 3)
    #for trips in trilist:
    #    print(trips)


    # Named Entity Recognition
    sentlist = []
    nerlist = []

    for s in stokens:
        ner = ne_chunk(pos_tag(wordpunct_tokenize(s)))
        nerlist.append(ner)
    print(stokens[5])
    print(nerlist[5])
