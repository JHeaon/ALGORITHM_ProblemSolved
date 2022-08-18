import sys
import itertools
input = lambda: sys.stdin.readline().rstrip()


def func():
    case = list(input())
    for i in range(len(case)):
        if ord(case[i]) - 3 < 65:
            case[i] = chr(ord(case[i]) + 23)
        else:
            case[i] = chr(ord(case[i]) - 3)
    print("".join(case))


if __name__ == "__main__":
    func()