select factory_id, factory_name, address
from food_factory
where substr(address, 1, 3) = "강원도"
order by factory_id