#------------------- Repetition of task is called loop ---------------

# ----------------Q-1 - Count positive number in a List ------------


# def count_positive_nums(list):

#     positive_number_count = 0

#     for num in list:
#         if num > 0 :
#             positive_number_count += 1
        
#     return positive_number_count


# print(count_positive_nums([1,-2,-3,4,5,3,10,9,-8]))


#-------------------- Q-2 Sum of even numbers---------------------- 

# def sum_even_nums(n):
#     sum = 0

#     for i in range(1,n+1):
#         if i % 2 == 0:
#             sum+=i
    
#     return sum

# print(sum_even_nums(100))


# ------------------ Q-3 Print the multiplication table ---------------

# def multiplication_table(n):
#     print(f"Multiplication Table of {n} is here")
#     for i in range(1,11):
#         if i == 5 :  # skip the 5th step . 
#             continue
#         print(f"{n} * {i} = {n*i} ")

# multiplication_table(5)


# ---------Q-4 reverse string------------ 

# def reverse_str(str):
#     rev_str = ""

#     for char in str:
#         rev_str = char + rev_str
    
#     return rev_str


# print(reverse_str("reversed"))



# ----------------Q-5 First Non repeat char in string --------------------

# def non_repeat_char(str):
#     for char in str:
#        if str.count(char) == 1:
#            return char


# print(non_repeat_char("teeter"))

# def non_repeat_char(str):
    
#     for i in range(len(str)):
#         count = 0
#         for j in range(len(str)):
#             if str[i] == str[j]:
#                 count+=1
        
#         if count == 1:
#             print(str[i])
#             break

# non_repeat_char("hello world")


# ------------------------- Q-6 Factorial of a number -------------

# def fact(n):
#     if n < 2 :
#         return 1
    
#     return n * fact(n-1)

# print(fact(5))

#--------------- Q-7 take input from user when enter value between (1,10 )-----------

# while True:
#     input_num = int(input("Enter the num : "))
#     if 1 <= input_num <=10:
#         print("Thanks")
#         break
#     else:
#         print("Invalid Number , try again !")


#------------------ Q-8 check prime num --------------------

# input_range = int(input("Enter a num of range : "))

# def prime(n):
#     if n < 2:
#         return False
    
#     for i in range(2,n):
#         if n % i == 0:
#             return False
    
#     return True


# def print_primes(ran):
#     for i in range(1,ran):
#         if prime(i):
#             print(i)

# print_primes(input_range)



# items = ["apple","orange","apple","mango"]


# for i in range(len(items)):
#     count = 0
#     for j in range(len(items)):
#         if items[i] == items[j]:
#             count+=1
    
#     if count == 2:
#         print(items[i])
#         break
   
    
