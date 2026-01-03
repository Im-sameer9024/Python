a = "Hello Guys This is a simple python file"

print(a.upper())

print(a.lower())

print(a.split(" "))

print(a.casefold())
print(a.replace("l","a"))
print(a.index("l"))

price = 30 
color = "Brown"

txt = " I have ordered a {} cup of chai for ${}."

print(txt.format(color, price))  # I have ordered a Brown cup of chai for $30.


tea_varities = ["Masala Chai", "Ginger Chai", "Lemon Chai", "Cardamom Chai"]


print(", ".join(tea_varities))  # Masala ChaiGinger ChaiLemon ChaiCardamom Chai


tea_types = ["Masala Chai","Ginger Chai","Lemon Chai"]


tea_types[1:1] = ["Cardamom Chai","Tulsi Chai"]

print("".join(tea_types[1:3]))