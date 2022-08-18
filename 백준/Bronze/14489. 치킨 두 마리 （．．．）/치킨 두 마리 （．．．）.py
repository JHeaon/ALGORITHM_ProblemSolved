import sys
input = lambda: sys.stdin.readline().rstrip()


def func():
    a, b = map(int, input().split())
    value = int(input())

    if a + b >= 2 * value:
        return (a + b) - 2 * value
    else:
        return a + b


if __name__ == "__main__":
    print(func())