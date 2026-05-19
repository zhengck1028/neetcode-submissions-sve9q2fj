-- Write your query below
select name 
from customers as a 
left join orders as b on a.id = b.customer_id
where b.id is null