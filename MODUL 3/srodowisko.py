# ZADANIE 1 #

shop_dict = {
    "warzywniak": ["marchew", "seler", "rukola"],
    "piekarnia": ["bułka", "chleb", "pączek"]
}

quantity = 0

for shop, food in shop_dict.items():
    shop = shop.capitalize()
    foods = ", ".join([food.capitalize() for food in food])
    print(f"Idę do {shop} i kupuję tam {foods}.")
    quantity += len(food)

print(f"W sumie kupuję {quantity} produktów.")

### ZADANIE 2 ###

for i in range(101):
    if i % 5 == 0:
        print(i)
print()
for i in range(101):
    if i % 5 == 0:
        print(i ** 3)
        
