# ICP 2: Loops, List, Tuples, Functions in Python


#### 1. Write a program, which reads height(feet.) of N students into a list and convert these heights to cm in a separate list:

N: No of students (Read input from user)

- Ex: L1: [5.2,5.4, 5.6, 6.1]
- Output: [158.4, 164.5, 170.6, 185.9]

#### My Code:
![ICP2_1](https://github.com/sme1d1/UMKC_DeepLearning2021/blob/master/images/icp2_1_program.PNG?raw=true "ICP2_1")

My program takes an input asking for the number of students. This int feeds into a function that asks the height of each student in feet and adds those heights (as floats) to a list. The list of heights is then fed into a function that converts the heights from feet to centimenters. The program outputs the entered heights in feet and the converted height in centimeters, rounded to a single decimal place (ex: 170.7).

![ICP2_1_out](https://github.com/sme1d1/UMKC_DeepLearning2021/blob/master/images/icp2_1_output.PNG?raw=true "ICP2_1_out")

---
#### 2. Given a non-negative integernum, return the number of steps to reduce it to zero.
If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.”

Example 1:
- Input:num = 14
- Output: 6

Explanation:
- Step 1) 14 is even; divide by 2 and obtain 7.
- Step 2) 7 is odd; subtract 1 and obtain 6.
- Step 3) 6 is even; divide by 2 and obtain 3.
- Step 4) 3 is odd; subtract 1 and obtain 2.
- Step 5) 2 is even; divide by 2 and obtain 1.
- Step 6) 1 is odd; subtract 1 and obtain 0.

#### My Code:
![ICP2_1_out](https://github.com/sme1d1/UMKC_DeepLearning2021/blob/master/images/icp2_2_program.PNG?raw=true "ICP2_1_out")

My program intializes an int (num) to a negative and starts a loop that runs until the value is positive. User input is assigned to num and tested with try to be an integer. If the user inputs a positive value or non integer value, the ValueError: prints "Invalid input" and the loop continues. 
A correct input is fed into a function that checks if the number is greater than zero, if even, else odd. If even, the number is divided by two and if odd, one is subtracted from it. A counter (steps) increments by one with each operation. The function runs recursively until the value reaches zero and steps is returned. The program then outputs how many steps it took to reduce the user input to a value of zero. 

![ICP2_1_out](https://github.com/sme1d1/UMKC_DeepLearning2021/blob/master/images/icp2_2_output.PNG?raw=true "ICP2_1_out") 

---
#### 3. Write a python program to find the wordcount in a file for each line and then print the output.Finally store the output back to the file.

Input: a file includes two lines: 
- Python Course
- Deep Learning Course

Output:
- Python: 1
- Course: 2
- Deep: 1
- Learning: 1

Note: Your program should work for any number of lines
#### My Code:
![ICP2_1_out](https://github.com/sme1d1/UMKC_DeepLearning2021/blob/master/images/icp2_3_program.PNG?raw=true "ICP2_1_out") 

My program opens the file words.txt to read its contents. A string is created to add the text of the file to and then is split to a list (wordlist). A list of word counts is created with a for loop performing the .count function on each word in the wordlist. These values of these two lists are concatenated together and added to another list (countlist). countlist is then converted to a dictionary to remove duplicate entries and back again to a list. The values from countlist are then outputted and added to a string (output) separated by new lines. Finally the program appends word.txt with the output string. 

![ICP2_1_out](https://github.com/sme1d1/UMKC_DeepLearning2021/blob/master/images/icp2_3_console_output.PNG?raw=true "ICP2_1_out")

File input: 

![ICP2_3_words](https://github.com/sme1d1/UMKC_DeepLearning2021/blob/master/images/icp2_3_words_input.PNG?raw=true "ICP2_1_out")

Appended file:

![ICP2_3_words](https://github.com/sme1d1/UMKC_DeepLearning2021/blob/master/images/icp2_3_words_output.PNG?raw=true "ICP2_1_out")

#### Learnings from the lesson 

In this lesson, I gained a greater understanding of how for and while loops functioned. Additionally I understand how to iterate through and manipulate lists, as well as how to interact with text files through code.

#### Issues with the lesson  

I had the most issues with the third program and had a number of different failed attempts at the problem before I arrived at my solution. Originally I was working with a generated list from text file but was having difficulty extracting the words. I experimented with finding spaces and creating new lists through slicing, but had trouble getting the result I wanted. Adding the text to string and splitting it to a list solved my main issue.



