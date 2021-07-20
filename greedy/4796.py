if __name__ == '__main__':
    case = 0
    while True:
        l, p, v = map(int, input().split())
        if l+p+v == 0:
            break
        case += 1

        result = (v//p)*l
        result += min((v%p), l)

        print("Case %d: %d" % (case, result))
