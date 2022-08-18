if __name__ == "__main__":
    a, b = map(int, input().split())
    answer = []
    for _ in range(a):
        line = input()
        answer.append(line[::-1])

    for i in answer:
        print(i)