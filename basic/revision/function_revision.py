
# def my_func():
#     print("This is the original function.")


# my_func()  # Call the original function


# def my_country(con = "India"):
#     print("I am from", con)

# my_country()  # Call with default argument
# my_country("USA")  # Call with a different argument


# def arg(*args):
#     print(args) # print the tuple of arguments

# arg("Hello"," World!")  # Call with a string argument

# def kwarg(**kwargs):
#     print(kwargs) # print the dictionary of keyword arguments

# kwarg(name="Alice", age=30)  # Call with keyword arguments 


x = 400

def outer_function():
    global x
    x = 200  # This modifies the global variable x

outer_function()
print(x)  # This will print 200 it is a global variable