-- 코드를 입력하세요
SELECT *
from FOOD_PRODUCT
where PRICE in (
    select MAX(PRICE) from FOOD_PRODUCT
)