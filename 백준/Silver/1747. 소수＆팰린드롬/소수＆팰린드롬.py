import sys
import math
input = lambda: sys.stdin.readline().rstrip()


def prime(num):
    end = int(math.sqrt(num))
    for i in range(2, end + 1):
        if num % i == 0:
            return False
    return True


def func():
    num = int(input())
    if num == 1:
        num = 2

    while True:
        
        if str(num) == str(num)[::-1] and prime(num):
            print(num)
            break
        else:
            num += 1


if __name__ == "__main__":
    func()