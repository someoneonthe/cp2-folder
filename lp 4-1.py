copies = int(input("Enter # of copies to be printed:"))
price = 0.0
if 0 < copies <= 99:
    price = 0.30
elif 99 < copies <= 499:
    price = 0.28
elif 499 < copies <= 749:
    price = 0.27
elif 749 < copies <= 1000:
    price = 0.26
elif copies > 1000:
    price = 0.25
else:
    print("the # of copies in invalid!")
    quit()
print ("price per copies is $" + str(price))
print ("total is $" + str(round(price * copies,2)))