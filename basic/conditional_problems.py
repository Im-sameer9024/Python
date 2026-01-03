
#-------------------------------------- question:1 - Classify a person's age group : Child (<13) , Teen (13-19), Adult (20-64), Senior (65+)-------------------------------------- 

# input_age = int(input("Enter your age: "))

# if input_age < 13:
#     print("Child")
# elif input_age >= 13 and input_age < 19 :
#     print("Teen")
# elif input_age >= 19 and input_age < 65 :
#     print("Adult")
# else:
#     print("Senior")


#----------------------------------------- question:2 - Movie ticket are priced based on age $12 for adults (18 and over), $8 for children . Everyone gets a $2 discount on Wednesday-------------------------------------------

# age = int(input("Enter your age ?"))
# day = input("Enter the day ?")

# solution:1 

# price = 12 if age>= 18 else 8

# price = price - 2 if day == "Wednesday" else price 

# solution:2

# if age >= 18:
#     price = 12
# else :
#     price = 8 
    
# if day == "Wednesday":
#     price = price - 2


# print(price)


# Question : 3 - Assign a letter grade based on a student's score A(90-100) , B(80-89), C(70-79) , D(60-69) , F(below 60) 

# student_score = int(input("Enter the student score in exam ?"))

# if student_score > 100 :
#     print("Score is out of range")
#     exit() # it is used to break the loop or if else statement. 

# if student_score <= 100 and student_score >= 90 :
#     print("Student got A Grade")
# elif  student_score >= 80 :
#     print("Student got B Grade")
# elif  student_score >= 70 :
#     print("Student got C Grade")
# elif  student_score >= 60 :
#     print("Student got D Grade")
# else :
#     print("Student got F Grade")
    

# Question : 4 - Choose a mode of transportation based on the distance <3 Km : Walk , 3-15 : Bike , >15 Car 
 

# distance = int(input("Enter distance? "))

# if distance < 3 :
#     print("Go by Walk")
# elif distance < 15 :
#     print("Go by Bike")
# else :
#     print("Go by Car")
    
    
year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or  (year % 400 == 0 ) :
    print("There is a leap year")
else :
    print("Not leap")