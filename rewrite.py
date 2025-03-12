def main():
    with open("cool.txt", 'w') as f:
        f.write('cool')
        f.write('beans')
    
    with open("cool.txt", 'a') as file:
        file.write('\nwowsers')
    
    with open("cool.txt", 'r') as f:
        for line in f:
            print(line, end='')
    pass

if __name__ == "__main__":
    main()