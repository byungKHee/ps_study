-- 코드를 입력하세요
SELECT F.FLAVOR
from FIRST_HALF as F
join ICECREAM_INFO as I
    on F.FLAVOR = I.FLAVOR
where TOTAL_ORDER > 3000
    and I.INGREDIENT_TYPE = 'fruit_based'
order by TOTAL_ORDER desc