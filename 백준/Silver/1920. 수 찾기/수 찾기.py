import sys
input = lambda: sys.stdin.readline().rstrip()


def func():
    case1 = set()
    case2 = list()

    num = int(input())
    case1.update(list(map(int, input().split())))
    num = int(input())
    case2.extend(list(map(int, input().split())))

    for i in case2:
        print(1 if i in case1 else 0)

if __name__ == "__main__":
    func()
