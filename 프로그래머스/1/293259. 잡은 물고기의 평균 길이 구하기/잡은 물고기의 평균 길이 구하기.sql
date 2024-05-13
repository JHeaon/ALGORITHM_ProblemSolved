select round(avg(length), 2) average_length
from (
    select id, 
           fish_type, 
           if(length is null, 10, length) length,
           time
    from fish_info
) a

    
    


