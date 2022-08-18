import sys
input = lambda: sys.stdin.readline().rstrip()


def func():
    answer = []
    max_num = [0, 0, 0]

    for i in range(1, 10):
        temp = list(map(int, input().split()))
        answer.append(temp)
        if max(temp) >= max_num[0]:
            max_num = [max(temp), i, temp.index(max(temp)) + 1]

    print(max_num[0])
    print(max_num[1], max_num[2])

if __name__ == "__main__":
    func()