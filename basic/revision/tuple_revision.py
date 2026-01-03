
# tuple is a collection which is ordered and unchangeable. In Python, tuples are defined by enclosing elements in parentheses (). 
# Tuples allow duplicate members.
# Tuples are indexed, the first item has index [0], the second item has index [1] etc.
# Tuples are used to store multiple items in a single variable.

my_tuple = ("apple", "banana", "cherry","apple", "cherry")

# print(my_tuple.count("cherry")) # count how many times cherry is present in tuple

# def iteration(tup):
#     for key,index in enumerate(tup):
#         print(key,index)
# iteration(my_tuple)

# add , update , remove item
# first covert tuple into list then perform operation and again convert list into tuple

# my_tuple = list(my_tuple)
#  
# my_tuple[1] = "orange"
# my_tuple.append("mango")
# my_tuple.remove("apple")
# del my_tuple[0]

# my_tuple = tuple(my_tuple)

# print(my_tuple)

# join two tuples
# new_tuple = ("kiwi", "grapes") + my_tuple


# print(new_tuple)