tea_verities = ["Green Tea", "Black Tea", "Oolong Tea", "White Tea", "Herbal Tea"]

string_tea = ", ".join(tea_verities) # use to make the list into a string
print("Available tea varieties: " + string_tea)


teas = ["Green Tea", "Black Tea", "Oolong Tea", "White Tea", "Herbal Tea"]

for tea in teas:
    if "Black Tea" in tea:
        print(tea + " is available.")
    elif "Chamomile" in tea:
        print(tea + " is available.")
    else:
        print(tea + " is not available.")
        
        
        
for i in range(1,11):
    print(i)
    

