select a.flavor
from first_half a inner join icecream_info b on a.flavor = b.flavor
where total_order >= 3000 and INGREDIENT_TYPE = "fruit_based"
order by total_order desc