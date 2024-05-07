select warehouse_id, warehouse_name, address, 
    case when freezer_yn is null then "N"
         else freezer_yn
    end freezer_yn
from food_warehouse
where substr(warehouse_name, 4, 2) = "경기"
order by warehouse_id