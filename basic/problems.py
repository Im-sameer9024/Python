

# Question : 1 - Count the Positive numbers 

# numbers = [1,2,3,4,5,-6,-7,-8]

# positive_number_count = 0

# for num in numbers:
#     if num > 0 :
#         positive_number_count +=1
        
# print("Final count of positive numbers is",positive_number_count)    

    
# Question : 2 - Calculate the sum of even Numbers 


# n = int(input("Enter a number: "))
# sum_even  = 0

# for i in range(1,n+1):
#     if i % 2 == 0:
#         sum_even += i

# print("sum of evens",sum_even)

# Question : 3 - Multiplication table Print  skip the fifth iteration.

# n  = int(input("Enter a number : "))

# for i in range(1,11):
#     if i == 5 :
#         continue
#     else :
#         print(n , "x" , i ,"=", n*i)
    
# Question : 4 - Reverse a string 

# input_str  = str(input("Enter a string: "))
# reversed_str = ""

# for char in input_str:
#     reversed_str = char + reversed_str

# print("reversed",reversed_str)


# Question : 5 - Find the first non repeatable Character. 

# input_str = str(input("Enter a string : "))

# for char in input_str:
#     if input_str.count(char) == 1 :
#         print("Char is: ",char)
#         break


# Question : 6 - Factorial of a number 

# input_num = int(input("Enter a num : "))
# fact = 1

#--------- using for loop--------- 

# for n in range(1,input_num+1):
#     fact = fact*n

# print("factorial of a num:",fact) 

#-------- using while loop------------ 

# while input_num > 0 :
#     fact = fact * input_num
#     input_num = input_num -1
    
# print("factorial of a Input num",fact)

# Question 7 : --------------- Enter the number while the number is 1 to 10 range.------------------

# while True :
#     user_input_num = int(input("Enter a number : "))
    
#     if 1 <= user_input_num <=10 :
#          print("This is Right")
#          break
#     else :
#          print("Invalid number")

# Question 8 : --------------------Check Prime number ------------

# input_num = int(input("Enter a number: "))

# if input_num > 1 :
#     for n in range(2,input_num):
#         if (input_num % n == 0) :
#             print("is Not Prime.")
#             break
#     else :
#         print("Is Prime.")

# else :
#     print("is Not Prime")


# Question 9 : Check all element in a list are unique. if a duplicate is found. exit the loop and print the duplicate . 

# items = ["apple","banana","orange","apple","mango"]

# unique_item = set()

# for item in items :
#     if item in unique_item :
#         print("Duplicate",item)
#         break
#     unique_item.add(item)
    
    