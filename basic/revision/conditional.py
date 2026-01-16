
score = int(input("Enter your score: "))


if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
elif score >= 50:
    print("Grade: E")   
else:
    print("Grade: F")



day = input("Enter the day of the week: ").lower()


match day:
    case "monday":
        print("It's Monday, the start of the work week!")
    case "tuesday":
        print("It's Tuesday, the second day of the work week!")
    case "wednesday":
        print("It's Wednesday, we're halfway through the week!")
    case "thursday":
        print("It's Thursday, almost the end of the week!")
    case "friday":
        print("It's Friday, the end of the work week!")
    case "saturday":
        print("It's Saturday, the weekend is here!")
    case "sunday":
        print("It's Sunday, a day to rest and recharge!")
    case _:
        print("Invalid day entered.")