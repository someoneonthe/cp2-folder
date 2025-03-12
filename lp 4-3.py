eggs = int(input("number of dozen eggs:"))
price = 0.0
if 0 < eggs < 4:
    price = 0.5
elif 3 < eggs < 6:
    price = 0.45
elif 5 < eggs < 11:
    price = 0.4
elif eggs > 10:
    price = 0.35
else:
    print("invalid")
    quit()
print ("price per dozen is $" + str(price))
print ("total is $" + str(price * eggs))