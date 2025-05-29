class age:
    age1 = int(input("how many people are less than 20: "))
    age2 = int(input("how many people are between 20 and 39: "))
    age3 = int(input("how many people are between 40 and 59: "))
    age4 = int(input("how many people are between 60 and 79: "))
    age5 = int(input("how many people are greater than 80: "))
    total = age1 + age2 + age3 + age4 + age5
    page1 = (age1/total) * 100
    page2 = (age2/total) * 100
    page3 = (age3/total) * 100
    page4 = (age4/total) * 100
    page5 = (age5/total) * 100
    print (str(page1) + "% " + str(page2) + "% " + str(page3) + "% " + str(page4) + "% " + str(page5) + "%")