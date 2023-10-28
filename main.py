def bin_search(l: list, x: int):
    left = -1
    right = len(l) - 1
    med = (left + right) // 2
    while left + 1 < right:
        if (l[med] > x):
            right = med
            med = (left + right) // 2
        elif (l[med] < x):
            left = med
            med = (left + right) // 2 + 1
        elif (l[med] == x):
            return "YES"
    return "NO"


if __name__ == '__main__':
    n, k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    for x in b:
        print(bin_search(a, x))
