import sys

def main (args: list[str]):
    if len(args) <= 0:
        print("hello")
        return
    print("hello,",args[0])
    for arg in args:
        print(arg)
    pass

if __name__=="__main__":
    main(sys.argv[1:])