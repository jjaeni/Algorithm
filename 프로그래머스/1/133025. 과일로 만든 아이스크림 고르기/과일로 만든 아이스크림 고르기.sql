-- 코드를 입력하세요
select fh.flavor
from first_half fh
join icecream_info I
on fh.flavor = I.flavor
where total_order > 3000 and ingredient_type = 'fruit_based'