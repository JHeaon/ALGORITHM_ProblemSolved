select count(*) FISH_COUNT, b.fish_name
from fish_info a inner join fish_name_info b on a.fish_type = b.fish_type
group by b.fish_name
order by 1 desc
