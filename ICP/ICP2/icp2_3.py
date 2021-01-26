"""
Write a python program to find the wordcount in a file for each line and then
print the output.Finally store the output back to the file.
Input:a file includes two line
Python Course
Deep Learning Course

Output:
Python: 1
Course: 2
Deep: 1
Learning: 1

Note: Your program should work for any number of lines
"""
# Scott McElfresh sme1d1 1/26/2021
with open('words.txt') as reader:
    # open our text file to read and close it when we exit
    bigstring = ''  # create a string to add out file text to
    wordcount = []  # create a list to store the word count
    countlist = []  # create a list to store the words concatenated with the word count
    for x in reader:
        bigstring += x  # add text to our string
    wordlist = bigstring.split()  # build a list by splitting our string

    # debug print(wordlist)
    for words in wordlist:
        # go through each word in our our world list, count them, and add the count to our wordcount list
        wordcount.append((wordlist.count(words)))
    i = 0
    for words in wordlist:
        countlist.append(wordlist[i] + ": " + str(wordcount[i]))  # build our concatenated list of words and counts
        i += 1
    countlist = list(dict.fromkeys(countlist))  # remove duplicates from the list by dictionary conversion

    i = 0
    output = "\n"  # create a blank line string to append on our text file
    for words in countlist:
        s = str(countlist[i])
        print(s)
        output += "\n" + s  # add the program output to our output string
        i += 1

with open('words.txt', 'a') as writer:
    writer.write(output)  # append the file with the output string

