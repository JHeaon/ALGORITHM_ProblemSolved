import sys
input = lambda: sys.stdin.readline().rstrip()


def func():
    money = int(input())
    num = int(input())
    for _ in range(num):
        a, b = map(int, input().split())
        money -= a * b

    print("Yes" if money == 0 else "No")


if __name__ == "__main__":
    func()