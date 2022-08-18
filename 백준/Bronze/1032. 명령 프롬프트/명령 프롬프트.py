import sys
input = lambda: sys.stdin.readline().rstrip()


def func():
    num = int(input())

    if num == 1:
        sentence = input()
        print(sentence)

    else:
        str_index = []
        sentence = input()
        for _ in range(num - 1):
            case = input()
            for i in range(len(case)):
                if case[i] != sentence[i]:
                    str_index.append(i)

        sentence = list(sentence)
        for i in str_index:
            sentence[i] = "?"

        print("".join(sentence))


if __name__ == "__main__":
    func()
    