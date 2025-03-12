from voidfunctions import *

def calcArea(len,wid) -> int:
    return len * wid

def calcPerim(len: int, wid: int) -> int:
    return 2* len + wid * 2

def areaPerim(len,wid):
    area = calcArea(len,wid)
    perim = calcPerim(len,wid)
    return area, perim

def main():
    voidfunctions.doThing
    length = int(input("Enter length"))
    width = int(input("Enter width: "))
    a,p = areaPerim(length, width)
    print()
    pass

def main():
    voidfuctions.doThing()
    length = int(input("Enter length: "))
    width = int(input("enter width: "))
    a,p = areaPerim(length, width)
    print(f"Area: {a}\nPerimeter: {n}")
    pass

if __name__ == "__main__":
    main()