# 파이썬 자주 쓰는 모듈과 기술

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