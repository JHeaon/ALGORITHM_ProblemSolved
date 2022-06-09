# pandas

## 📖 pandas 란?

pandas 는 numpy를 포함한 여러 데이터들을 쉽고 빠르게 가져온다는 점에서 좋은 프레임워크라고 할 수 있다.

pandas 에서는 기본적으로 정의되는 자료구조, Series와 DataFrame 을 사용한다.

<br>


##  pandas의 기본사항
```
# row(행) / column(열)
일반적으로 데이터표를 보면 row와 column으로 나누어져있다. column은 데이터의 특징을 담고 있으며, row는 각 사람을 의미한다.


```

<br>



## pandas 의사용방법
```
import pandas as pd

dt = ([["정해원", 50, 66], ["홍준기", 20, 36], ["김기렬", 10, 18]])
my_df = pd.DataFrame(dt, columns =['name', 'english', 'age'], index = ['a', 'b', 'c', 'd'])

my_df 
# 행에는 name, english, age 열에는 a, b, c, d로 정리된 표가 나온다.
```
일반적으로 pd.DataFrame()안에 2차원 배열만 집어 넣게 되면은 행과 열에는 아무것도 없이 index만 뜨기 때문에 column과 index 를 이용하여 행과 열을 지정하여 채워 넣을 수 있다.


<br>



### DataFrame 만들기 
```
import numpy as np
import pandas as pd

two_dimensional_list = [['dongwook', 50, 86], ['sineui', 89, 31], ['ikjoong', 68, 91], ['yoonsoo', 88, 75]]
two_dimensional_array = np.array(two_dimensional_list)
list_of_series = [
    pd.Series(['dongwook', 50, 86]), 
    pd.Series(['sineui', 89, 31]), 
    pd.Series(['ikjoong', 68, 91]), 
    pd.Series(['yoonsoo', 88, 75])
]

# 아래 셋은 모두 동일합니다
df1 = pd.DataFrame(two_dimensional_list)
df2 = pd.DataFrame(two_dimensional_array)
df3 = pd.DataFrame(list_of_series)

print(df1)
```


<br>

### dict를 이용한 DataFrame 만들기
```
import numpy as np
import pandas as pd

names = ['dongwook', 'sineui', 'ikjoong', 'yoonsoo']
english_scores = [50, 89, 68, 88]
math_scores = [86, 31, 91, 75]

dict1 = {
    'name': names, 
    'english_score': english_scores, 
    'math_score': math_scores
}

dict2 = {
    'name': np.array(names), 
    'english_score': np.array(english_scores), 
    'math_score': np.array(math_scores)
}

dict3 = {
    'name': pd.Series(names), 
    'english_score': pd.Series(english_scores), 
    'math_score': pd.Series(math_scores)
}


# 아래 셋은 모두 동일합니다
df1 = pd.DataFrame(dict1)
df2 = pd.DataFrame(dict2)
df3 = pd.DataFrame(dict3)

print(df1)
```

<br>

### pandas를 이용하여 csv 엑셀 파일 읽기
```
import pandas as pd

iphone_df = pd.read_csv("아이폰csv의 상대주소")
iphone_df
# 아이폰 csv가 화면에 나온다. 
```
- pandas는 위에 있는 첫줄을 헤더라고 판단하고 column 값에 넣는데 이를 방지하기 위해서 iphone_df = pd.read_case("아이폰csv의 상대주소", header = None) 을 하면 column 부분이 인덱스로 찬다.

- index_col = n 을 통해서 n column에 해당하는 부분이 맨 왼쪽의 메인이 된다.

<br>

### pandas에서 데이터를 가져오기
```
iphone.loc['iphone 7', '메모리']
```
데이터 프레임명.loc['행' '열'] 을 통해서 데이터를 가져올 수 있다. 만약 인덱스와 해당 column에 있는 모든 내용을 가지고 오고 싶다면 
```
iphone.loc[:, '메모리']
또는
iphone['메모리']
```
처럼 사용하면 된다.
여기서 2개 이상의 열값을 추출하고 싶다고 하면

```
iphone[['제조일자', '메모리']]
혹은
iphone.loc[:,['제조일자', '메모리']]
```
를 사용하면 됩니다. 여기서 중요해야할 점은 여러 데이터를 추출할경우 리스트 안에 리스트를 사용해야 한다는 점을 잊지 말자!

만약에 어느 특정한 어느 부분에서의 슬라이싱을 하고 싶다면 df.loc(출발행:끝행 , 출발열:끝열) 을 사용하면 된다. 

### pandas 조건을 넣어서 찾기
```
iphone_df.loc[iphone_df['디스플레이'] > 5]
```
처럼 loc 안에 조건을 넣어서 행과 열을 구할 수 있다.
여기서 조금 짚고 넘어가야할 점이있다면 
조건을 써두고 그 조건을 넣어서 처리해야 오류가 안난다는점이다. 밑의 예로는
```
조건1 = 해원이 == 바보
조건2 = 김기렬 == 머함
iphone_df.loc[조건1 & 조건2, 뽑고자 하는 열]
```
처럼 하는 형식을 게속 연습하자!

### pandas 정수형으로 데이터 찾기
```
iphone.iloc[[1,3],[2,4]]
```
iloc을 통해서 인덱스를 통해서 슬라이싱을 통핵서 찾을 수 있다. 

### DataFrame에 값 쓰기
```
iphone_df.loc['iphone 8', '출시 버전'] = '넣고싶은 값'
```
loc 에 나오는 값에 따라서 인수에 맞게 넣어주면 그 값에 따라 수정된다. 

### DataFrame에 행과 열을 추가 / 삭제
```
iphone_df["넣고자 하는 열"] = 값
iphone_df.loc["넣고자하는 행"] = 값
```
단 여기서 넣고자 하는 열과 행이 겹치는 이름은 없어야 한다. 여기서 만약 만들어진 행과 열을 삭제하고 싶다면

```
iphone_df.drop("삭제하고자 하는 이름", axis='index' 또는 'column', inplace=True 또는 False)
```
drop을 통해서 삭제가 가능하고 뒤에 있는 axis를 통해 행을 삭제 하고 싶은지 열을 삭제 하고 싶은지 지정할 수 있으며, inplace을 통해 현재 데이터 프레임을 수정하고 싶은지, 아니면 수정한 값을 변수에 담을지를 정할 수 있다. 

### DataFrame의 행과 열 이름 수정
```
iphone_df.rename(column={'메모리' : 'Memory'}, inplace = True)
# 물론 column 값을 index로 변경 가능하다.
```

### DataFrame 에서의 열을 인덱스로 바꾸기
```
liverpool.df.set_index("열이름", inplace = True)
# 하지만 기존의 인덱스가 날아가기 때문에 이를 따로 저장해두어야 한다.
```
### DataFrame 에서 열의 종류가 얼마나 담겼는지 확인하기
```
course_counts = df.loc[allowed, "course name"].value_counts()
# value_counts() 를 사용합니다. 
```

