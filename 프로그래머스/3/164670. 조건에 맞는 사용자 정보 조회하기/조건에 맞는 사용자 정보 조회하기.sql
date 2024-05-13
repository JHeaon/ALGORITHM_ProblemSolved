SELECT user_id, 
       nickname,
       concat(b.city, " ", STREET_ADDRESS1," ", STREET_ADDRESS2) 전체주소,
       concat(substr(TLNO, 1, 3), "-", substr(TLNO, 4, 4), "-", substr(TLNO, 8, 4)) '전화번호'
from USED_GOODS_BOARD a inner join USED_GOODS_USER b on a.writer_id = b.user_id
group by user_id
having count(user_id) >= 3
order by user_id desc