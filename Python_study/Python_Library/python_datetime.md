# datetime

##  📖 datetime 라이브러리 
시간에 대한 라이브러리이다.

## ✏️ 사용방법
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

 <br><br><br>
 