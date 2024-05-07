SELECT animal_type, name, sex_upon_intake
replace(name, null, "no name") name
from animal_ins
order by animal_id