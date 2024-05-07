select substr(product_code, 1, 2) category,
       count(*) products
from product
group by substr(product_code, 1, 2)
order by product_code