import sys
import math
input = lambda: sys.stdin.readline().rstrip()


def func():
    num = int(input())
    num = math.factorial(num)
    cnt = 0

    for i in str(num)[::-1]:
        if i == "0":
            cnt += 1
        else:
            break

    print(cnt)


if __name__ == "__main__":
    func()
