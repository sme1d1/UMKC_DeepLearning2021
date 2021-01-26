## Scott McElfresh sme1d1 Deep Learning 1/25/2021
"""
Given a non-negative integernum, return the number of steps to reduce it to zero.
If the current number is even, you have to divide it by2, otherwise, you have to subtract 1 from it.”

Example 1:
Input:num = 14
Output:6

Explanation:
Step 1) 14 is even; divide by 2 and obtain 7.
Step 2) 7 is odd; subtract 1 and obtain 6.
Step 3) 6 is even; divide by 2 and obtain 3.
Step 4) 3 is odd; subtract 1 and obtain 2.
Step 5) 2 is even; divide by 2 and obtain 1.
Step 6) 1 is odd; subtract 1 and obtain 0.
"""


# Scott McElfresh sme1d1 Deep Learning 1/25/2021
def checkval(number):  # function to evaluate and perform math on input
    global steps
    if number > 0:  # when number reaches 0 we break from function
        if number % 2 == 0:  # check if number is even
            number = number / 2
            steps = steps + 1  # update steps counter
            checkval(number)  # recursion until number is zero
        else:
            number = number - 1
            steps = steps + 1
            checkval(number)
        return steps
    return steps


steps = 0

# Get user input for non-negative integer

num = -10  # initialize num to negative

while num < 0:  # loop input until a positive integer is entered
    try:  # test user input
        num = int(input("Enter an non-negative integer: "))
    except ValueError:
        print("Invalid input")

step = checkval(num)
txt1 = "Diving the number by 2 if even and subtracting 1 from it if odd, until the number reaches zero: "
txt2 = "It took {} steps to reduce {} to zero".format(step, num)
# output steps it took to reduce number to zero
print(txt1)
print(txt2)
