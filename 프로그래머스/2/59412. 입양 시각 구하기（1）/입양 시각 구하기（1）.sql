select hour, count(hour) as count
from (
    select *, hour(datetime) as hour
    from animal_outs
) as A
where hour >= 9 and hour <= 19
group by hour
order by hour
