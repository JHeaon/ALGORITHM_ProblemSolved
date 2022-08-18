import sys
import itertools
input = lambda: sys.stdin.readline().rstrip()


def func():
    case = []

    for _ in range(9):
        case.append(int(input()))

    for i in itertools.combinations(case, 7):
        if sum(i) == 100:
            case = i
            break

    for i in case:
        print(i)


if __name__ == "__main__":
    func()