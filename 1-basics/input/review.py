print("""Hello
price: £1.50
Fruit options: 
Apple
Banana
Pear
""")

print("What fruit are you trying to purchase?")
fruit = input()

print("How many would you like to buy?")
amount = float(input())

price = float(amount * 1.50)

print("please enter £",price)