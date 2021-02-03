# ICP 1: Fun with Python


#### 1. State differences between Python 2 and Python 3 versions.

Python 2 and Python 3 have several differences:

Python 2 is legacy software that was retired at the start of 2020. The codebase is no longer maintained.


In Python 2, integer division rounds down a calculation to the nearest whole number.
- Python2: 5/3 = 1 whereas in Python 3: 5/3 = 1.666667

Python 2 stores strings as ASCII by default but by default, Python 3 stores strings as Unicode.

Python 2 does not use parentheses for a print statement but Python 3 requires them.
- ex: python 2 => print "Hello"
- ex: python 3 => print ("Hello")

Additionally, Python 3 includes a string formatted in the string class str.format(). 

- ex: print("{} / {} = {}".format(8, 2, 8/2)) outputs "8 / 2 = 4".
---
#### 2. Write a python program for the following:
1. Input the string “Python” as a list of characters from the console, delete at least 2 characters, reverse the resultant string and print it. 
- Sample input: python
- Sample output: ntyp

2. Take two numbers from the user and perform arithmetic operations on them.

#### My Code:
![ICP1_1](https://github.com/sme1d1/UMKC_DeepLearning2021/blob/master/images/icp1_1_sme1d1.PNG?raw=true "ICP1_1")

My program assigns a user input string to 'name'. It then generates two random indices, x, and y, of the string to access. The characters of 'name' are assigned to a list 'name_list'. This was done because string objects don't support item assignment. Blank characters '' are assigned the 
x and y indices of 'name_list'. A new string 'new_name' is then created from the characters in 'name_list'. This word is the original user-inputted name with the random two characters removed from it. This is then printed out in reverse.

The second part of the program takes two user-inputted integers then performs addition, multiplication, and division on the given integers. The sum, product, and quotient are printed. 

![ICP1_1output](https://github.com/sme1d1/UMKC_DeepLearning2021/blob/master/images/icp1_1_output_sme1d1.PNG?raw=true "ICP1_output")

Video: 
https://youtu.be/740SVJDxPN0

---
#### 3.  Write a program that:
1. Accepts a sentence and replace each occurrence of ‘python’ with ‘pythons’ without using regex
- Sample input: "I love playing with python"
- Sample output: I love playing with pythons

![ICP1_2](https://github.com/sme1d1/UMKC_DeepLearning2021/blob/master/images/icp1_2_sme1d1.PNG?raw=true "ICP1_2")

My program asks the user to input a string and replaces any instance of 'python' or 'Python' with 'pythons' and 'Pythons' respectively. 

![ICP1_2output](https://github.com/sme1d1/UMKC_DeepLearning2021/blob/master/images/icp1_2_output_sme1d1.PNG?raw=true "ICP1_2_output")

Video:
https://youtu.be/n883IYsEUy4

#### Lessons learned from project and lesson

I learned about the differences between Python 2 and 3. It was sunsetted a year ago, but I think this might have been more relevant in the past when programmers were in a transistion period between Python 2 and 3. Additionally, I learned quite a lot about basic python syntax. 

#### Issues with project

Python is new to me: I have a some knowledge of C and C# but I'm still relatively new to programming. This first assignment was a nice introduction to how Python programs are formatted. I'm sure it will take some time to translate the knowledge I have into a new language but so far this hasn't been too frustratring.

