import sys
input = lambda: sys.stdin.readline().rstrip()


def func():
    num = int(input())
    for _ in range(num):
        case = int(input())
        print("even" if case % 2 == 0 else "odd")


if __name__ == "__main__":
    func()
