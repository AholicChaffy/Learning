print("Holiday")

name = input("Type ur name: ")
key = input("Type the key of the area: ")

if key == "1":
    WorkingYears = input("Type your Working years: ")
    if WorkingYears == "1":
        print(f"Hi {name} you have 6 days")
    elif WorkingYears >= "2" and WorkingYears <="6":
        print(f"Hi {name} you have 14 days")
    elif WorkingYears > "7":
        print(f"Hi {name} you have 20 days")
elif key == "2":
    WorkingYears = input("Type your Working years: ")
    if WorkingYears == "1":
        print(f"Hi {name} you have 7 days")
    elif WorkingYears >= "2" and WorkingYears <="6":
        print(f"Hi {name} you have 15 days")
    elif WorkingYears > "7":
        print(f"Hi {name} you have 22 days")
elif key == "3":
    WorkingYears = input("Type your Working years: ")
    if WorkingYears == "1":
        print(f"Hi {name} you have 10 days")
    elif WorkingYears >= "2" and WorkingYears <="6":
        print(f"Hi {name} you have 20 days")
    elif WorkingYears > "7":
        print(f"Hi {name} you have 30 days")
