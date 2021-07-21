if __name__ == '__main__':
    n, m = map(int, input().split())
    brand = []
    for _ in range(m):
        package, breakup = map(int, input().split())
        brand.append([package, breakup])
    package_cnt = n // 6

    package_price, breakup_price = 1001, 1001
    for i in range(m):
        package_price = min(package_price, brand[i][0])
        breakup_price = min(breakup_price, brand[i][1])

    result = min(package_price * package_cnt, breakup_price * (6 * package_cnt))\
             + min(package_price, breakup_price * (n - package_cnt * 6))
    print(result)
