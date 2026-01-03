
# Question 1 - Basic function syntax 

# Write a function to calculate a number os square and return 

# input_num = int(input("Enter num: "))

# def square_of_num(n):
#     return n*n
# print(square_of_num(input_num))

# Question 2 - Create a function to calculate the sum of two numbers 

# num1 = int(input("Enter num1:- "))
# num2 = int(input("Enter num2:- "))

# def sum_of_two_nums(a,b):
#     return a+b
# print("Sum of two numbers",sum_of_two_nums(num1,num2))

# Question 3 - Function for multiplication

# num1 = int(input("Enter number 1 :- "))
# num2 = int(input("Enter number 2 :- "))

# def multiplication(a,b):
#     return a*b
# print("Multiplication",multiplication(num1,num2))

# Question 4 - Write a function to greet a user 

# def greet(user):
#     print(user," Greets")
     
# greet("sameer")

# Question 5 - create a function  to calculate cube of a number by lamda function

# def cube(x):
#     return x**3


# cube = lambda x: x**3

# print(cube(5))

# Question 6 - Create a function to accept a arguments to sum of all numbers 

# def sum_of_all_nums(*args):
#      total = 0
#      for num in args:
#          total += num
#      return total
# print(sum_of_all_nums(1,2,3,4,5))  


# def sum_of_all_nums(*args):
#      return sum(args)
     
# print(sum_of_all_nums(1,2,3,4,5))

# Question 7 - Create a function to accepts any number of keyword arguments and print them in the format 
# def print_keyword_args(**kwargs):
# key:value pair


# def print_keyword_args(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key} : {value}")

# print_keyword_args(name="sameer", age=25, city="New York")


# Question 8 - Generator function with yield keyword 
# Write a generator function that yields even numbers up to a specified limit.


# def even_generator(limit):
#     for i in  range(2,limit+1,2):
#         print(i)

# even_generator(10) # 2 4 6 8 10


# Question 9 - Recursive function to calculate factorial of a number 

# def factorial(n):
#     if n == 0 or n == 1 :
#         return 1
    
#     return n * factorial(n-1)

# print(factorial(5))  # 120