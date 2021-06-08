if __name__ == '__main__':
    table = {'black': (0, 1), 'brown': (1, 10), 'red': (2, 100), 'orange': (3, 1000), 'yellow': (4, 10000),
             'green': (5, 100000), 'blue': (6, 1000000), 'violet': (7, 10000000), 'grey': (8, 100000000),
             'white': (9, 1000000000)}
    resist1 = input()
    resist2 = input()
    mul = input()
    result = int(str(table.get(resist1)[0]) + str(table.get(resist2)[0])) * table.get(mul)[1]
    print(result)
