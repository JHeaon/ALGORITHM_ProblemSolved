import sys
input = lambda: sys.stdin.readline().rstrip()


def func():
    a, b = map(int, input().split())
    answer = a - (a * (b/100))
    if answer >= 100:
        return 0
    else:
        return 1


if __name__ == "__main__":
    print(func())