import sys
input = lambda: sys.stdin.readline().rstrip()


def func():
    case1 = list(map(int, input().split()))
    case2 = list(map(int, input().split()))

    distance1 = ((case2[0] - case1[0]) ** 2 + (case2[1] - case1[1]) ** 2) ** 0.5
    distance2 = case1[2] + case2[2]

    if distance1 < distance2:
        print('YES')
    else:
        print('NO')


if __name__ == "__main__":
    func()
