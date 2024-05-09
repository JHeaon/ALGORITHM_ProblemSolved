select book.book_id, author.author_name, date_format(PUBLISHED_DATE,'%Y-%m-%d') published_date
from book inner join author on book.author_id = author.author_id
where book.category like "%경제%"
order by book.published_date