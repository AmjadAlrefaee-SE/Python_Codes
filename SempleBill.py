print("Sehha & Hana" + "\n" + "Restaurant")
FoodName1 = "Pizza"
FoodName2 = "Cola"
FoodName3 = "water"
pizza = 1
cola = 2
water =2
PizzaPrice = 20
ColaPrice = 5
waterPrice = 1.5
Total = (pizza * PizzaPrice) + (cola * ColaPrice)+(water * waterPrice)
Tax = Total * 0.15
print(f"1: {FoodName1} = {pizza} * {PizzaPrice} = {pizza * PizzaPrice}$")
print(f"2: {FoodName2} = {cola} * {ColaPrice} = {cola * ColaPrice}$")
print(f"3: {FoodName3} = {water} * {waterPrice} = {water * waterPrice}$")
print("------------------")
print(f"Total = {Total}$ \nTax = {Tax}$")
print("------------------")
print(f"Total Cost = {Total + Tax}$")
print("------Thank You-----")