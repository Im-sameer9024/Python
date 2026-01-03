

# ------------------Question-01 :- Classify a person age group : Child (<13) , Teen (13-19), Adult (20-64), Senior (65+)------------------ 


# input_age = int(input("Enter your age: "))

# def classify_age(age):
#     if age < 13:
#         return "Child"
#     elif age < 20 :
#         return "Teen"
#     elif age < 65:
#         return "Adult"
#     else:
#         return "Senior"


# print(classify_age(input_age))


# --------------------- Question-02:- Movie ticket are priced based on age adults $12 (18 and over) , for children $8 . everyone gets a $2 discount on Wednesday. --------------------------


# input_age = int(input("Enter age: "))
# today = input("Enter day : ")

# def movie_ticket(age,day):
#     price = 12 if age >= 18 else 8
#     if day == "wednesday":
#         price = price -2
#     else :
#         return  price 


# print(movie_ticket(input_age,today))


# Question-03 Leap year 


# input_year = int(input("Enter a year:- "))

# def leap_Year(year):
#     if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0) :
#         print(f"{year} is a Leap year")
#     else:
#         print(f"{year} is not Leap year")
    

# leap_Year(input_year)
