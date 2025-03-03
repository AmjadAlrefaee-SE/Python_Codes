Name = input("Enter Your name: ")
Age = int(input("Enter Your Age: "))
Tall = float(input("enter Your Tall: "))
Wight = float(input("Enter Your wigth: "))

Predected_age = (Tall/Wight * Age) + 10
print(f"Welcome, {Name.title()}")
print(f"you will live until {int(Predected_age + 2000)}, and you will be {int(Predected_age)} years old.")