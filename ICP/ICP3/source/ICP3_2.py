"""
Write a simple program that parse a Wiki page mentioned below and follow the instructions:
https://en.wikipedia.org/wiki/Deep_learning
Print out the title of the page
Find all the links in the page (‘a’ tag)
Iterate over each tag(above) then return the link using attribute "href" using get
Save all the links in the file

Scott McElfresh sme1d1 Deep Learning 2021 2/3/2021
"""

import requests
from bs4 import BeautifulSoup

page = requests.get("https://en.wikipedia.org/wiki/Deep_learning")  # specify our webpage

with open('webscrape.txt', 'a') as writer:  # open our file to write to
    soup = BeautifulSoup(page.content, 'html.parser')
    print(soup.title.string)
    x = soup.find_all('a')
    bigstring = ''  # create an empty string to append all of our links to
    for i in x:
        link = str(i.get('href'))
        if 'http://' in link:
            bigstring = link
        elif 'https://' in link:
            bigstring = link
        elif '//en' in link:
            bigstring = 'https:' + link
        elif '#cite' in link:  # append citation links in webpage
            bigstring = "https://en.wikipedia.org/wiki/Deep_learning" + link
        else:
            if link == "None":  # remove top anchor link
                bigstring = ""
            else:
                bigstring = "http://en.wikipedia.org" + link  # append internal links
        writer.write(bigstring + "\n")  # append our web-scraped links to file with a new line between
