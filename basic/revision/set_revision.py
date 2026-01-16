# This set will automatically remove duplicates
# Sets are unordered collections of unique items in Python, defined by curly braces {}.


# my_set = {"apple", "banana",  "cherry"}

# access items in set 

# for item in my_set:
#     print(item)

# add item to set
# my_set.add("orange")
# my_set.add("banana") # adding duplicate item will have no effect

# update set with multiple items
# my_set.update(["mango", "grapes", "apple"]) # adding duplicate item will have no effect

# add any iterable (list, tuple, dictionary etc.)
# my_set.update(("kiwi", "papaya"))
# my_set.update({"name": "John", "age": 30})  # only keys will be added
# my_set.update("hello") # each character will be added
# my_set.update(["h", "e", "l", "o"]) # adding duplicate item will have no effect


# remove item from set
# my_set.remove("banana") # raises error if item not found
# my_set.discard("banana") # does not raise error if item not found
# removed_item = my_set.pop() # removes and returns an arbitrary item

# print(my_set)

# join two sets 

# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3  = {4,5,6}
# set4 = set1.union(set2,set3)
# print(set4)


# insertion operator
# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3  = {4,5,6}
# set4 = set1 & set2 & set3
# set4 = set1.intersection(set2,set3)



# print(set1 | set2 | set3)


# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set3 = set1.difference(set2)

# print(set3)


