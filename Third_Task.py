Convert_From = input("Exchange From (USD, EUR, SAR): ").upper()
Quantity = float(input("How Much? "))
Convert_to = input("Exchange To (USD, EUR, SAR): ").upper()

#1 USD = 3.75 SAR
# 1 USD = 0.66 EUR
USD = 1
SAR = 3.75
EUR = 0.99
Exchange_Rate = 0
if Convert_From == "USD" and Convert_to =="SAR":
    Exchange_Rate = Quantity * SAR
    print(f"You Will Give {Quantity} USD, and you will take {Exchange_Rate} SAR")
elif Convert_From == "SAR" and Convert_to == "USD":
    Exchange_Rate = Quantity / SAR
    print(f"You Will Give {Quantity} SAR, and you will take {Exchange_Rate} USD")
elif Convert_From == "USD" and Convert_to =="EUR":
    Exchange_Rate = Quantity * EUR
    print(f"You Will Give {Quantity} USD, and you will take {Exchange_Rate} EUR")
elif Convert_From == "EUR" and Convert_to =="USD":
    Exchange_Rate = Quantity / EUR
    print(f"You Will Give {Quantity} EUR, and you will take {Exchange_Rate} USD")
elif Convert_From == "EUR" and Convert_to =="SAR":
    Exchange_Rate = Quantity / EUR * SAR
    print(f"You Will Give {Quantity} EUR, and you will take {Exchange_Rate} SAR")
elif Convert_From == "SAR" and Convert_to =="EUR":
    Exchange_Rate = Quantity /SAR * EUR
    print(f"You Will Give {Quantity} SAR, and you will take {Exchange_Rate} EUR")
elif Convert_From == Convert_to:
    Exchange_Rate = Quantity
    print(f"The Currency is equal and the amount = {Quantity}")
else:
    print("Invalid Wrong, please Try Again and select USD or EUR or SAR")