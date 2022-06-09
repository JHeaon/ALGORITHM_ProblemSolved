# Python basic

## 📖 python
파이썬은 쉽게 사용가능한 인터프리터 언어이다.

<br>

##  <p align = "center">✏️ 입, 출력 </p>

## 입력 : input() vs sys.stdin.readline()
```
import sys
value = sys.stdin.readline()
```
한 두줄 입력 받는 문제들이라면, input()을 통해서 넣어도 괜찮으나 여러줄을 입력 받아야 할 경우에는 시간초과가 일어 날 수 있기 때문에 sys.stdin.readline() 을 사용하는 것이 좋다. 

## 출력 : print()와 \ 백슬래쉬
```
print("""\
안녕하세요
정해원입니다.
잘부탁해요
\""")
```
백슬래쉬 없을경우 """ 구간에 공백이 생겨버려서 한칸 뛰우고 text 한칸 뛰우기로 보인다 이를 방지하기 위해서 \ 백슬래쉬를 붙이게되면 자연스럽게 나타나게 된다.

```
s = "aaaaaaa" \
+ "bbbbbbbb"
```
\ 쓰면 다음줄로 넘어갑니다. 

## ⊙ if 문과 리스트, 문자열
 ```
is_ok = [1,2,3,4]
if is_ok:
  print("ok")
else:
  print("no")
========
ok
```
리스트나 문자열 같은 경우에 값이 들어있으면 1, 없으면 0을 반환하는데 이를 이용하여 if문에 사용할 수 있다. 굳이 len(list) > 0 이라고 비교할 필요가 없다

## ⊙ is 와 none
 ```
is_empty = None

if is_empty is None:
    print("none")
======
none
 ```
 is 는 ~ 와 같다 라고 할때 많이 사용하는데 그중에서도 값이 none인가에 대한 판별을 가리는데 많이 사용한다. 


<br><br><br>

##  <p align = "center">✏️ 파이선 내장 함수 </p>

## ⊙ - n진법 관련 함수
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

<br>

## ⊙ - eval 함수
```
s = "3 + 2"
print(eval(s)) # 5
```
eval 함수는 문자열로 되어 있는 수식을 계산해주는 함수이다.

<br>

## ⊙ - divmod 함수
```
a = 12
b = 2 
print(*divmod(a, b))
# 6 0
```
divmod 를 통해 몫과 나머지를 한번에 구할수 있으며, *이라는 언팩킹을 통해 원래 나올 결과인 (6, 0)을 괄호 없이 그냥 6, 0 으로 나타 낼수 있다.

<br>

## ⊙ - ljust, center, rjust 함수
```
s = "가나다라"
n = 7
s.ljust(n)  #좌측 정렬
s.center(n) #가운데 정렬
s.rjust(n)  #우측 정렬
```
ljust, center, rjust 함수는 n만큼의 정렬을 시행한다.

<br>

## ⊙ - 아주 큰수 inf
```
min_val = float('inf')
min_val > 10000000000
```
inf 를 이용하면 파이썬에서 아주 큰수라고 지정할수 있다.

<br>

## ⊙ - 문자열, 문자 바꾸기
```
>>> 'Hello, world!'.replace('world', 'Python')
'Hello, Python!'
>>> s = 'Hello, world!'
>>> s = s.replace('world!', 'Python')
>>> s
'Hello, Python'
```
replace('바꿀 문자열', '새 문자열')

<br>

## ⊙ - filter 내장 함수
```
filter(조건 함수, 순회 가능한 데이터)
```
데이터를 반환함으로 list(filter(조건함수, 순회가능 데이터)) 를 활용 하는 것이 좋다.

<br>

## ⊙ - 리스트 사전화
```
list1 = ['aaa','bbb','ccc','ddd']
list2 = [11,22,33,44]

dict_list= dict(zip(list1,list2))

print(dict_list)
```
두개의 리스트를 zip으로 받아서 dict화 시킬수 있다.

<br>


## ⊙ - upper, lower 함수
```
    str = "Hello world"
    up = str.upper() # HELLO WORLD
    low = str.lower() # hello world
    print(str) # Hello world
```
대문자, 소문자로 바꿔주는 함수이다. 리턴값으로 대문자, 소문자로 바꾼 값을 리턴해준다.

<br>

## ⊙ swapcase() 함수
```
a = input()
print(a.swapcase())
```
대소문자 바꿔서 리턴해주는 함수이다.

<br>

## ⊙ capitalize(), title() 함수
```
A='abcd'
print(A.upper()) #ABCD
print(A.capitalize()) #Abcd
print(A.title()) #Abcd

B='a2b3c4'
print(B.upper()) #A2B3C4
print(B.capitalize()) #A2b3c4
print(B.title()) #A2B3C4

C="abc-def efg"
print(C.upper()) #ABC-DEF EFG
print(C.capitalize()) #Abc-def efg
print(C.title()) #Abc-Def Efg
```
capitalize는 첫 문장만, title은 공백을 포함한 특수문자 다음 글자를 대문자로
변경해준다.

<br>

## ⊙ - ord, chr 함수
```
print(ord('a')) # 97
print(chr(ord('a'))) # a
```
문자 아스키코드에 의거하여 문자를 숫자로 숫자를 문자로 바꿔주는 함수이다.

<br>

## ⊙ - split() 함수
```
    str = "Hello world"
    hello = str.split() # hello = ["Hello", "world"]`
```
split() 안에있는 문자 기준으로 잘라서 리스트를 반환해 준다. 

<br>

## ⊙ - sort() 함수
리스트 안의 요소가 많을때 비교
```
case = [[1, 2],[3, 4],[5, 6]] 
case.sort(key = lambda x:(x[0], x[1]))
# x[0] 기준으로 정렬하되, 서로 같으면 x[1] 기준으로 정렬한다.
```
리스트안에 비교 해야할 내용들이 다양할 경우에 key 값을 이용하여 비교해서 반환 시킬 수 있다. key = "함수" 가 들어가야한다. 2차원 리스트에서 sort 함수를 쓰면 기본값으로 y값 까지 알아서 정렬해준다라는 점도 알고 있자!

<br>

## ⊙ - del, pop(), remove() 함수
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

<br>


## ⊙ - 2차원 함수를 1차원 함수로 바꾸는 방법
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

<br>

## ⊙ - count 함수
```
list.count(str)
```
list안에 있는 str의 갯수를 리턴해준다.

<br>

## ⊙ - find vs index 함수
```
list.find(str)
list.index(str)
```
list안에 있는 str의 인덱스를 리턴해주는데 만약 index함수를 사용할 경우에 해당 str이 없으면 에러를 일으키고, find 함수는 해당 함수에 해당하는 값이 없다면 -1을 반환한다.

<br>


## ⊙ - enumerate 함수
```
>>> for i, name in enumerate(['body', 'foo', 'bar']):
...     print(i, name)
...
0 body
1 foo
2 bar
```
인덱스와 함께 반환을 하고 싶다면 enumerate 함수를 사용한다.

<br>


## ⊙ - 절대값 
```
    절대값 = abs(값)
```
abs()안의 값을 내용을 절대값해서 반환해준다.

<br><br><br>

 
 

 ##  <p align = "center">✏️  bisect 라이브러리 </p>


## ⊙ 이진탐색 bisect 함수
```
import bisect
mylist = [1, 2, 3, 7, 9, 11, 33]
print(bisect.bisect(mylist, 3))
```
오름차순으로 정렬된 리스트에서 특정한 값의 위치를 찾는 알고리즘이다.

<br><br><br>

