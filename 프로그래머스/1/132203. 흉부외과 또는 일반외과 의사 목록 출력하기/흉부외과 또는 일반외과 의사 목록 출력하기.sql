select dr_name, dr_id, mcdp_cd, substr(hire_ymd, 1, 10) hire_ymd
from doctor
where mcdp_cd IN ("CS", "GS")
order by hire_ymd desc, dr_name