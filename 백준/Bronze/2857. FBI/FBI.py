import sys
input = lambda: sys.stdin.readline().rstrip()


def func():
    case = []
    for i in range(1, 6):
        name = input()
        if "FBI" in name:
            case.append(str(i))

    if len(case) == 0:
        print("HE GOT AWAY!")
    else:
        print(" ".join(case))


if __name__ == "__main__":
    func()