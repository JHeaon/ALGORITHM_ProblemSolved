import sys
input = lambda: sys.stdin.readline().rstrip()


def func():
    mtx1 = []
    mtx2 = []
    answer = []

    n, m = map(int, input().split())

    for _ in range(n):
        temp = list(map(int, input().split()))
        mtx1.append(temp)

    for _ in range(n):
        temp = list(map(int, input().split()))
        mtx2.append(temp)

    for m1, m2 in zip(mtx1, mtx2):
        temp = []
        for a, b in zip(m1, m2):
            temp.append(a + b)
        answer.append(temp)

    for i in answer:
        for j in i:
            print(j, end=" ")
        print("")


if __name__ == "__main__":
    func()