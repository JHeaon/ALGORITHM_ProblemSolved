import sys
input = lambda : sys.stdin.readline()

def func():
    num = int(input()) // 4
    print("long " * num + "int")


if __name__ == "__main__":
    func()
    