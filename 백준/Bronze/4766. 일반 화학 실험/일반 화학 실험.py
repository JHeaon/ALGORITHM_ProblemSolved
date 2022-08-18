import sys
input = lambda: sys.stdin.readline().rstrip()


def func():
    num1 = float(input())

    while True:
        num2 = float(input())
        if num2 == 999:
            break
        else:
            gap = num2 - num1
            print(f"{gap:.2f}")
            num1 = num2



if __name__ == "__main__":
    func()
