# Scott McElfresh ICP 7-2 sme1d1
import requests
from bs4 import BeautifulSoup

''' # commented out this section so we're not continually web-scraping after our input.txt file is made
page = requests.get("https://en.wikipedia.org/wiki/Google")  # specified webpage to scrape info from

with open('input.txt', 'a', encoding='utf-8') as writer:  # create input.text and append to file
    soup = BeautifulSoup(page.content, 'html.parser') # parse page content as html
    #print(soup)
    text = soup.find_all(text=True) # get all text from our html
    zed = {t.parent.name for t in text} # return all tags 
    #print(zed)
    bigString = ''  # create string to add page text
    # define list of tags for content we don't want to include in our text corpus
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

    # add all off our desired text to corpus bigString.
    for t in text:
        if t.parent.name not in garbage:
            bigString +='{} '.format(t) # format all of our good tags as text
    bigString = bigString.replace("\\", "")  # replace slashes with blank
    bigString = bigString.replace("\n", "")  # remove new lines
    writer.write(bigString)  # write to our file the contents of our corpus bigString
'''
# import nltk
# nltk.download('maxent_ne_chunker')
# nltk.download('words')

# import our nlp methods
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from nltk import ngrams
from nltk import wordpunct_tokenize, ne_chunk

# read from our input.txt file
with open('input.txt', 'r', encoding='utf-8') as reader:
    bigString = reader.read()  # create a string from our content to act as our corpus
    # print(bigString)

    # Tokenization
    stokens = sent_tokenize(bigString)  # sentence tokenization
    wtokens = word_tokenize(bigString)  # word tokenization
    # print(stokens)
    # for s in stokens: # print contents of our sentence token list
    # print(s)
    # for w in wtokens: # print contents of our word token list
    #    print(w)

    # POS
    pos = pos_tag(wtokens)  # POS on word list
    # print(pos)

    # Stemming
    ps = PorterStemmer()  # 3 different stem methods
    ls = LancasterStemmer()
    ss = SnowballStemmer('english')

    stemlist_P = []  # create list for our Porter Stemmer output
    stemlist_L = []  # create list for our Lancaster Stemmer output
    stemlist_S = []  # create list for our Snowball Stemmer output

    for w in wtokens:
        stemlist_P.append((w + " : " + ps.stem(w)))  # append to our lists the word and our stemming
        stemlist_L.append((w + " : " + ls.stem(w)))
        stemlist_S.append((w + " : " + ss.stem(w)))
    print(stemlist_P[5:10])

    # Lemmatization
    lemlist = []  # create list for lemmatization output
    lem = WordNetLemmatizer()
    for w in wtokens:
        lemlist.append((w + " : " + lem.lemmatize(w)))  # append to our list the word and its
    # print(lemlist)

    # Trigrams
    trilist = ngrams(bigString.split(), 3)  # set up Trigrams
    # for trips in trilist:
    #    print(trips[0:10])

    # Named Entity Recognition
    nerlist = []  # create list for NER output

    for s in stokens:
        ner = ne_chunk(pos_tag(wordpunct_tokenize(s)))  # apply NER to each sentence in our stoken list
        nerlist.append(ner)  # append our ner output list
    # print(stokens[5])
    # print(nerlist[5])
