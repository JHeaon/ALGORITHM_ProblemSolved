select a.product_id, a.product_name, a.price * sum(b.amount) TOTAL_SALES
from food_product a inner join food_order b on a.product_id = b.product_id
where b.produce_date like "%2022-05%"
group by a.product_id
order by 3 desc , 1
