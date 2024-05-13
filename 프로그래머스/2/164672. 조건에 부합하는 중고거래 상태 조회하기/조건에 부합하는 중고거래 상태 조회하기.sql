SELECT board_id, writer_id, title, price,
       case when status="DONE" then "거래완료"
            when status="RESERVED" then "예약중"
            when status="SALE" then "판매중"
       end STATUS
from used_goods_board
where created_date like "%2022-10-05%"
order by board_id desc