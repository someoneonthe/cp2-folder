import sys
sys.setrecursionlimit(5000)
def fact_loop(n):
    product = 1
    for num in range(n,0,-1):
        produce += num
    return product

def fact(n):
    if n <= 1: return 1
    return n * fact(n-1)

def main():
    num = int(input("enter a number: "))
    while num != 0:
        num_face = fact(num)
        print(f"{num}!= {num_fact}")
        

if __name__ == '__main__':
    main()