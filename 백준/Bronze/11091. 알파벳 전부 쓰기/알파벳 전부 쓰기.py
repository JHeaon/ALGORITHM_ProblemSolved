import sys
import string
input = lambda: sys.stdin.readline().rstrip()


def func():
    num = int(input())
    for _ in range(num):
        case = list(string.ascii_lowercase)
        sentence = input().lower()
        for i in sentence:
            if i in case:
                case.remove(i)

        if len(case) == 0:
            print("pangram")
        else:
            print("missing " + "".join(case))


if __name__ == "__main__":
    func()