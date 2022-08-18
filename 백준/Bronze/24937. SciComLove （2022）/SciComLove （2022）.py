import sys
import string
input = lambda: sys.stdin.readline().rstrip()


def func():
    sentence = "SciComLove"
    num = int(input()) % 10
    for _ in range(num):
        ch = sentence[0]
        sentence = sentence[1:] + sentence[0]
    print(sentence)


if __name__ == "__main__":
    func()
