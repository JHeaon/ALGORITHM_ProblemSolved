import sys
def input(): return sys.stdin.readline().rstrip()


def func():
    K, N = map(int, input().split())

    if N == 1:
        print(-1)
        exit()
    else:
        result = (N*K // (N-1))
        if (N*K) % (N-1):
            print(result + 1)
        else:
            print(result)
 


if __name__ == "__main__":
    func()