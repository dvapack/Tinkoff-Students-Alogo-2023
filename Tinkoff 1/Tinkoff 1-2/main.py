def bin_search(l: list, x: int):
    left = 0
    right = len(l)
    while left + 1 < right:
        med = (left + right) // 2
        if (l[med] > x):
            right = med
        else:
            left = med
    if (right != len(l)):
        if (abs(x - l[left]) <= abs(l[right] - x)):
             return l[left]
        else:
             return l[right]
    return l[left]



if __name__ == '__main__':
    n, k = [int(s) for s in input().split()]
    arr = [int(s) for s in input().split()]
    zap = [int(s) for s in input().split()]
    for x in zap:
        print(bin_search(arr, x))


