import sys
input = lambda : sys.stdin.readline()


def func():
    num = int(input())
    for i in range(num):
        case = input().strip()
        print("yes" if 6 <= len(case) <= 9 else "no")


if __name__ == "__main__":
    func()