n = int(input())

while True:
  if n == 1: 
    print(1)
    break
  if n % 2 == 0:
    n //= 2
  else:
    print(0)
    break