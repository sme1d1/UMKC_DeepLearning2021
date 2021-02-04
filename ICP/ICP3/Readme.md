Scott McElfresh

# Python_Lesson3: Object-Oriented Python

a. ICP 3 was about the utilization of classes, web-scraping via the requests library with Beautiful-Soup, and Numpy. 

b. Our objective was to create three programs:

1b. The first program objective was to write a program that created a class 'Employee' and a class 'Fulltime Employee' that inherited the properties of 'Employee'. A data member was created to count the total number of instances of 'Employee'. Constructors that initialized name, family, salary, and department created for the Employee class. Additionally, a function to average the salary of all Employees was created. Instances were to be created for both classes and have their member functions called. 

1c. Implementation: I created an Employee class and class variables to see to track the number of employees and their combined salaries. Then I created and initialized the class's constructors. Next, I made methods to calculate the average salary and print object constructor values. I created the FulltimeEmployee class which inherits Employee's properties and initialized its inherited constructors. Finally, I created objects for both classes and called their member functions.
![ICP3_1a](https://github.com/sme1d1/UMKC_DeepLearning2021/blob/master/ICP/ICP3/images/ICP3_1_code1.PNG?raw=true "ICP3_1a")
![ICP3_1b](https://github.com/sme1d1/UMKC_DeepLearning2021/blob/master/ICP/ICP3/images/ICP3_1_code2.PNG?raw=true "ICP3_b1")

Output: the program prints out both instances' constructor values and the average salary of employees. 
***
![ICP3_1](https://github.com/sme1d1/UMKC_DeepLearning2021/blob/master/ICP/ICP3/images/ICP3_1.PNG?raw=true "ICP3_1")

***
1d.

1e. This was an insightful introduction to classes and parameterized constructors. I learned how to define classes and create objects. Additionally, I understand how class variables function and how to call member functions. I didn't find this program that challenging once I understood how to define classes and constructors. 
***
2b. The objective of the second program was to create a web scrapping program that extracted all the links from the Deep Learning wiki page and outputted them to a file. Additionally, the program would print the page's title.

2c. Implementation: After importing the requisite libraries, I used requests.get to pull the data from the specified wiki page. I open a text file 'webscrape.txt' to append to. Next, I parse the requests data using BeautifulSoup as HTML. Then I complete the first objective of the program: printing this title. I then loop through the 'a' elements getting all the 'href' elements as strings. The program appends the internal links, the #cite references and removes the top anchor using some if/else logic. In each cycle, the link is written to the 'webscrape' textfile. 
![ICP3_2a](https://github.com/sme1d1/UMKC_DeepLearning2021/blob/master/ICP/ICP3/images/ICP3_2_code1.PNG?raw=true "ICP3_2a")
Output: The program prints the page's title: print and outputs the links to [webscrape.txt](https://github.com/sme1d1/UMKC_DeepLearning2021/blob/master/ICP/ICP3/source/webscrape.txt)
***
![ICP3_2](https://github.com/sme1d1/UMKC_DeepLearning2021/blob/master/ICP/ICP3/images/ICP3_2.PNG?raw=true "ICP3_2")
***

2d.

2e. After looking further into the possibilities of web-scrapping, I feel like our program just scratches the surface of the use of the requests library and Beautiful Soup. Even so, I learned how to use the 'request.get' method to pull data from websites and how to parse that data with Beautiful Soup. The biggest challenge I faced in this assignment, was in formatting the extracted links. Wiki pages use a lot of internal links and citations as well as a top page anchor; all of these are collected using Soup's find_all('a') method. I chose to format the links so they were all functional outside of the website and excluded the top anchor from the outputted file. 
***
3b. The objective for our third program was to use the Numpy library to create a vector of size 20 with random float values between 1 and 20. That vector was then to be reshaped into a 4 by 5 array and replace the maximum values of each row with zero without using a loop.

3c. Implementation: I created the vector of random floats using the np.random.uniform method and reshaped it to a 4,5 array with '.reshape' in a single line. I then used np.max to find the maximum values in each row. Next, I utilized np.in1d to create a 4 by 5 array of True False comparing the initial array and the max value array. Finally, I create a new array with the maximum values replaced with zero by using np.where. It uses the 'true/false' array as the condition to determine which values of the initial array to replace with zero.
![ICP3_3a](https://github.com/sme1d1/UMKC_DeepLearning2021/blob/master/ICP/ICP3/images/ICP3_3_code1.PNG?raw=true "ICP3_3a")
***
![ICP3_3](https://github.com/sme1d1/UMKC_DeepLearning2021/blob/master/ICP/ICP3/images/ICP3_3.PNG?raw=true "ICP3_3")

3d.

3e. Numpy looks to be an incredibly powerful library with the capability to easily manipulate data. I learned who to generate vectors, reshape them into arrays, create zero-filled arrays, before some evaluations and conditional evaluations on data (min, max, greater than, etc.), and how to manipulate the data within arrays. Creating this program challenged me the most out of all the IPC programs (I thought it would be the easiest). The biggest issue I ran into was figuring out how to compare values in my arrays. Finding the max values was easy but I couldn't figure out how to compare the two arrays directly with np.where. My max value array was a different size than the initial array - this yielded other errors when trying to compare them directly with Numpy. Finding np.in1d in the documentation was key for my solution.






