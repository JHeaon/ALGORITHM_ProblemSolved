a, b = map(int, input().split())
a, b = min(a, b), max(a, b)
print((b+1)*b//2 - (a+1)*a//2 + a)
