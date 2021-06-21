if __name__ == '__main__':
    n = int(input())
    customer = list(map(int, input().split()))
    refused = n - len(list(set(customer)))
    print(refused)
