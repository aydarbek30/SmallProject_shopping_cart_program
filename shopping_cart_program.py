#Shopping cart program

foods = []
prices = []
total = 0

while True:
    food = input("Enter your food(or press q to quit): ")
    if food.lower() == "q":
        break
    price = float(input("Enter price of food: "))
    foods.append(food)
    prices.append(price)

print("____SHOPPING CART____")

for food in foods:
    print(food)

for price in prices:
    total += price

print(f"Your total price is: {total:.2f}$")


