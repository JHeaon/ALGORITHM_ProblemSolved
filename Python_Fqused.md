# 파이썬 자주 쓰는 모듈과 기술

## 📌 내장 함수 관련
### - n진법 관련 함수
```
만약 들어온 수가 N이고 M진법으로 만들고 싶다면,
answer = ""
while n > 0:
    n, re = divmod(n, m)
    answer += str(re)

# m진법 수를 뒤집은 수가 나오기에 뒤집어줘야함
answer = answer[::-1]

# 만약 n 진법인 수의 str형태가 존재한다면, 
answer = int(str, n)
으로 10진법의 수로 풀어줄수 있다.
```
일반적으로 n진법의 수를 구하는 방법이다. 밑의 int(str, n)을 통해 n진법인 수의 str형태를 10진법 int형으로 바꿔 표현 할 수 있다.

```
a = 200
# 접두어 제외
b = format(a, 'b')
print(f"2진수 : {b}")

c = format(a, 'o')
print(f"8진수 : {c}")

d = format(a, 'x')
print(f"16진수 : {d}")

[결과]
2진수 : 11001000
8진수 : 310
16진수 : c8
```
하지만 일반적으로 우리가 자주 구하는 2, 8, 16 진수일 경우 다음과 같이 변환하여 사용하는 것이 시간복잡도상 편하게 사용할 수 있다.

### - eval 함수
```
s = "3 + 2"
print(eval(s)) # 5
```
eval 함수는 문자열로 되어 있는 수식을 계산해주는 함수이다.

### - divmod 함수
```
a = 12
b = 2 
print(*divmod(a, b))
# 6 0
```
divmod 를 통해 몫과 나머지를 한번에 구할수 있으며, *이라는 언팩킹을 통해 원래 나올 결과인 (6, 0)을 괄호 없이 그냥 6, 0 으로 나타 낼수 있다.

### - ljust, center, rjust 함수
```
s = "가나다라"
n = 7
s.ljust(n)  #좌측 정렬
s.center(n) #가운데 정렬
s.rjust(n)  #우측 정렬
```
ljust, center, rjust 함수는 n만큼의 정렬을 시행한다.


### - 아주 큰수 inf
```
min_val = float('inf')
min_val > 10000000000
```
inf 를 이용하면 파이썬에서 아주 큰수라고 지정할수 있다.

### - enumerate 함수
```
>>> for i, name in enumerate(['body', 'foo', 'bar']):
...     print(i, name)
...
0 body
1 foo
2 bar
```
인덱스와 함께 반환을 하고 싶다면 enumerate 함수를 사용한다.



## 📌 list 관련
### - filter 내장 함수
```
filter(조건 함수, 순회 가능한 데이터)
```
데이터를 반환함으로 list(filter(조건함수, 순회가능 데이터)) 를 활용 하는 것이 좋다.

### - 리스트 사전화
```
list1 = ['aaa','bbb','ccc','ddd']
list2 = [11,22,33,44]

dict_list= dict(zip(list1,list2))

print(dict_list)
```
두개의 리스트를 zip으로 받아서 dict화 시킬수 있다.


### - upper, lower 함수
```
    str = "Hello world"
    up = str.upper() # HELLO WORLD
    low = str.lower() # hello world
    print(str) # Hello world
```
대문자, 소문자로 바꿔주는 함수이다. 리턴값으로 대문자, 소문자로 바꾼 값을 리턴해준다.

### - ord, chr 함수
```
print(ord('a')) # 97
print(chr(ord('a'))) # a
```
문자 아스키코드에 의거하여 문자를 숫자로 숫자를 문자로 바꿔주는 함수이다.

### - split() 함수
```
    str = "Hello world"
    hello = str.split() # hello = ["Hello", "world"]`
```
split() 안에있는 문자 기준으로 잘라서 리스트를 반환해 준다. 

### - sort() 함수
리스트 안의 요소가 많을때 비교
```
case = [[1, 2],[3, 4],[5, 6]] 
case.sort(key = lambda x:(x[0], x[1]))
# x[0] 기준으로 정렬하되, 서로 같으면 x[1] 기준으로 정렬한다.
```
리스트안에 비교 해야할 내용들이 다양할 경우에 key 값을 이용하여 비교해서 반환 시킬 수 있다. key = "함수" 가 들어가야한다. 2차원 리스트에서 sort 함수를 쓰면 기본값으로 y값 까지 알아서 정렬해준다라는 점도 알고 있자!

### - del, pop(), remove() 함수
```
user_1 = ['Jason' , 'Smith', 'Kevin']
del user_1[1]    # 'Smith' 삭제
print(user_1)

user_1 = ['Jason' , 'Smith', 'Kevin']
user_1.pop(1) # 'Smith' 삭제
print(user_1)

user_1 = ['Jason' , 'Smith', 'Kevin', 'Smith']
user_1.remove('Smith') # 'Smith' 삭제
print(user_1)
```
요소 삭제로는 del, pop, remove 함수가 존재하는데 del, pop 함수는 해당 인덱스에 있는 요소를 삭제하는 반면에 remove 함수는 특정값을 삭제하는데 사용된다.  


### - 2차원 함수를 1차원 함수로 바꾸는 방법
```
my_list = [[1, 2], [3, 4], [5, 6]]

# 방법 1 - sum 함수
answer = sum(my_list, [])

# 방법 2 - itertools.chain
import itertools
list(itertools.chain.from_iterable(my_list))

# 방법 3 - itertools와 unpacking
import itertools
list(itertools.chain(*my_list))

# 방법 4 - list comprehension 이용
[element for array in my_list for element in array]

# 방법 5 - reduce 함수 이용 1
from functools import reduce
list(reduce(lambda x, y: x+y, my_list))

# 방법 6 - reduce 함수 이용 2
from functools import reduce
import operator
list(reduce(operator.add, my_list))
```

## 📌 Math 라이브러리
### - 절대값 
```
    절대값 = abs(값)
```
abs()안의 값을 내용을 절대값해서 반환해준다.

## 📌 입력
### - input() vs sys.stdin.readline()
```
import sys
value = sys.stdin.readline()
```
한 두줄 입력 받는 문제들이라면, input()을 통해서 넣어도 괜찮으나 여러줄을 입력 받아야 할 경우에는 시간초과가 일어 날 수 있기 때문에 sys.stdin.readline() 을 사용하는 것이 좋다. 


## 📌 itertools 라이브러리
### permutations 함수
```
import itertools

arr = ['A', 'B', 'C']
nPr = itertools.permutations(arr, 2)
print(list(nPr))

결과 : [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]
# permutations(반복 가능한 객체, r)
```
순열을 구할때 사용한다. 
### combinations 함수
```
import itertools

arr = ['A', 'B', 'C']
nCr = itertools.combinations(arr, 2)
print(list(nCr))

결과 : [('A', 'B'), ('A', 'C'), ('B', 'C')]
# combinations(반복 가능한 객체, r)

```
조합을 구할때 사용한다. 

### product 함수
```
import itertools

iterable1 = 'ABCD'
iterable2 = 'xy'
iterable3 = '1234'
print(list(itertools.product(iterable1, iterable2, iterable3)))
# 두 스트링 'ABCD', 'xy' 의 곱집합은 Ax Ay Bx By Cx Cy Dx Dy 입니다.

만약 리스트에서 n개를 뽑아서 중복순열을 구한다고 한다면, 

k = list(product(case, repeat=2))
repeat 이라는 것을 통해서 한다.
# product(반복 가능한 객체, repeat=1)
```
중복 순열을 구할때 사용되는 함수이다.

### combinations_with_replacemnet 함수
```
from itertools import combinations_with_replacement

for cwr in combinations_with_replacement([1,2,3,4], 2):
    print(cwr, end=" ")
# combinations_with_replacement(반복 가능한 객체, r)
```
중복 조합을 만들때 사용한다.

## 📌 collections 라이브러리
### deque 함수
```
from collections import deque
deq = deque()
```
* deque.append(item): item을 데크의 오른쪽 끝에 삽입한다.
* deque.appendleft(item): item을 데크의 왼쪽 끝에 삽입한다.
* deque.pop(): 데크의 오른쪽 끝 엘리먼트를 가져오는 동시에 데크에서 삭제한다.
* deque.popleft(): 데크의 왼쪽 끝 엘리먼트를 가져오는 동시에 데크에서 삭제한다.
* deque.extend(array): 주어진 배열(array)을 순환하면서 데크의 오른쪽에 추가한다.
* deque.extendleft(array): 주어진 배열(array)을 순환하면서 데크의 왼쪽에 추가한다.
* deque.remove(item): item을 데크에서 찾아 삭제한다.
* deque.rotate(num): 데크를 num만큼 회전한다(양수면 오른쪽, 음수면 왼쪽).

### Counter 함수
```
from collections import Counter

temp_list = Counter(list)
```
Counter 클래스를 사용할 경우 해당 리스트에 있는 원소들이 몇번 반복되었는지에 대해서 dict 형태로 반환해준다. 예를 들어서 아래 처럼 사용할 경우 다음과 같다.
```
colors = Counter(['blue', 'green', 'red', 'blue','red','blue'])
print(colors) => Counter({'blue': 3, 'red': 2, 'green': 1})
```
여기서 자주 사용하는 함수는 most_common() 이며, most_common()에서 값을 넘겨주면 리스트 형태로 큰 값에서 내림차순으로 반환한다.
```
c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(a=1, b=2, c=3, d=4)
c.subtract(d)
c
Counter({'a': 3, 'b': 0, 'c': -3, 'd': -6})
```
두 번째로는 subtract()함수인데 Counter객체로 만들어진 c, d를 subtract하면 원소끼리의 차를 반환하게 된다.

## 📌 datatime 라이브러리
### now 함수
```
import datetime

d = datetime.datetime.now()
print (d)
# 2021-04-18 16:50:43.895283
```
datetime 객체는 년,월,일,시,분,초 반환이 가능 요일 같은 경우에는 월~일까지 0 ~ 6까지 숫자로 반환해서 나타내준다
```
d = datetime.datetime.now()
print (d.year,'년 ', d.month,'월 ', d.day,' 일')
print (d.hour,'시 ',d.minute,'분 ',d.second,'초')
print(d.weekday())

#
2021 년  4 월  18  일
16 시  58 분  38 초
# 요일 맞는 숫자 반환
```

현재 시간을 now라는 메소드로 구할수 있으나, 직접 지정한 날짜를 datatime 객체를 통해서 가져올 수 있다.

```
wuhan_covid19 = datetime.datetime(2019,12,12)
print (wuhan_covid19)
# 2019-12-12 00:00:00
```

## string 라이브러리
### 데이터를 상수로 정의해 놓은것
```
import string 

string.ascii_lowercase # 소문자 abcdefghijklmnopqrstuvwxyz
string.ascii_uppercase # 대문자 ABCDEFGHIJKLMNOPQRSTUVWXYZ
string.ascii_letters # 대소문자 모두 abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
string.digits # 숫자 0123456789
```
파이썬에는 이렇게 데이터를 라이브러리화 해서 저장해놓았다.

## bisect 라이브러리
### 이진탐색 bisect 함수
```
import bisect
mylist = [1, 2, 3, 7, 9, 11, 33]
print(bisect.bisect(mylist, 3))
```
오름차순으로 정렬된 리스트에서 특정한 값의 위치를 찾는 알고리즘이다.