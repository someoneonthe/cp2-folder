num = int(input("how many will you by: "))
if num < 100:
    price = num * 5.95
elif num > 99 and num < 200:
    price = num * 5.75
elif num > 199 and num < 300:
    price = num * 5.40
else:
    price = num * 5.15
print("price not including tax: " + str(price))