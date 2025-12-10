chai = "masala chai"
print(chai)


x = 'chai'
first_char = x[0]
print(first_char)  # 'c'


sliced_chai =  chai[0:6]
sliced_chai2 = chai.split(" ")
print(sliced_chai)  # 'masala'
print(sliced_chai2)  # ['masala', 'chai']


num_list = "0123456789"

copy_num_list = num_list[:]


print(copy_num_list)  # '0123456789'

num_list_hoped = num_list[0:7:2] 
print(num_list_hoped)  # '0246'


m = "masala chai"
print(m.replace("a","l"))


print(m.split(" "))


price = 60
chai = "masala chai"
txt = "The price is {} rupees {}"

print(txt.format(price,chai))  # The price is 60 rupees


newStr = "This Is a String with leading and trailing spaces"

print(newStr.count("i"))


print(newStr.casefold())

print(newStr.find("i"))

print(newStr.index("with"))

