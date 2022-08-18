import sys
import math
input = lambda: sys.stdin.readline().rstrip()


def func():
    N, W, H = map(int, input().split())
    for _ in range(N):
        num = int(input())
        if num <= math.sqrt(W ** 2 + H ** 2):
            print("DA")
        else:
            print("NE")


if __name__ == "__main__":
    func()
