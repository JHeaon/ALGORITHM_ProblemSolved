import sys
import math
input = lambda: sys.stdin.readline().rstrip()


def func():
    num = int(input())
    print(str(math.factorial(num))[-1])


if __name__ == "__main__":
    func()