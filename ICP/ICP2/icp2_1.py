
'''
1. Write a program, which reads height(feet.) of N students into a list and convert these heights
to cm in a separate list:

N: No of students (Read input from user)
Ex: L1: [5.2,5.4, 5.6, 6.1]
Output: [158.4, 164.5, 170.6, 185.9]

'''

# Scott McElfresh sme1d1 Deep Learning 1/25/2021


# function to input student heights in feet and add them to a list
def student_list(studentcount):
    my_heights = []
    count = 0
    for i in range(studentcount):
        count = count + 1
        x = float(input("Input your #" + str(count) + " student's height in feet (ex. 4.2). "))
        my_heights.insert(i, x)  # add value to list
    return my_heights


# function to convert student height from feet to cm
def converttocm(listofstudentheights):
    my_cmheights = []
    count = 0
    for i in listofstudentheights:
        # hard coded feet to cm conversion (1 foot = 30.48 cm)
        c = i * 30.48  # convert to cm
        d = float("{:.1f}".format(c))  # format to 1 decimal places (rounded up)
        my_cmheights.insert(count, d)  # add value to list
        count = count + 1
    return my_cmheights


# take inputs, feed to functions, and print output
n = int(input("Input how many students you have: "))
my_students = student_list(n)
print("Student's height in feet:")
print(my_students)
cm_students = converttocm(my_students)
print("Student's height in cm: ")
print(cm_students)
