n = int(input())
c = int(input())
wList = list(map(int, input().split()))
vList = list(map(int, input().split()))


def m(i, j):
    if i >= n or j <= 0:
        return 0
    return max(m(i + 1, j), m(i + 1, j - wList[i]) + vList[i])

print()
print(m(0, c))
