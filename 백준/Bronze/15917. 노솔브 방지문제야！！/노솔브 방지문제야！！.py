import sys
input = lambda: sys.stdin.readline().rstrip()


def func():
    answer = [2 ** i for i in range(32)]
    num = int(input())
    
    for _ in range(num):
        case = int(input())
        print(1 if case in answer else 0)


if __name__ == "__main__":
    func()