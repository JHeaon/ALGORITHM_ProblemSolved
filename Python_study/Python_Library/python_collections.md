# collections

## 📖 collections 라이브러리 </p>
여러 자료구조를 모아둔 라이브러리이다.


## ✏️ deque 함수
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

<br>


## ✏️ Counter 함수
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

## ✏️ defaultdict 함수
```
from collections import defaultdict

text = "Life is too short, You need python."

d = defaultdict(int)
for c in text:
    d[c] += 1

print(dict(d))
===================
{'L': 1, 'i': 2, 'f': 1, 'e': 3, ' ': 6, 's': 2, 't': 3, 'o': 5, 'h': 2, 'r': 1, ',': 1, 'Y': 1, 'u': 1, 'n': 2, 'd': 1, 'p': 1, 'y': 1, '.': 1}
```
딕셔너리로 이와 같은 집계용 코드를 작성할 때는 항상 초깃값에 신경 써야 한다. 하지만, collections의 defaultdict를 사용하면 이러한 번거로움을 피할 수 있다. 미리 초기화 가능하다.

```
defaultdict(string)
defaultdict(int)
defaultdict(float)
```
등등 여러가지가 타입형으로 지정 가능하다.


