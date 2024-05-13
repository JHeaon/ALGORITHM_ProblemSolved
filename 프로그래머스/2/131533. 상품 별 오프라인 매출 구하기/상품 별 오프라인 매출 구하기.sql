SELECT product_code, sum(price * sales_amount) SALES
from  product a inner join offline_sale b on a.product_id = b.product_id
group by product_code
order by 2 desc, 1
