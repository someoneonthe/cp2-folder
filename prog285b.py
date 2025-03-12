from c286 import Salesperson

def main():
    try:
        print("number\tCODE\tSales\tCommission")
        with open("Langdat/prig285.dat", 'r') as f:
            for line in f:
                data = line.split(" ")
                id = int(data[0])
                code = int(data[1])
                sales = float(data[2])

                person = Salesperson(id, code, sales)
                person.calc_commission()
                print(str(person))
    except Exception as e:
        print("ERROR", e)
    pass
