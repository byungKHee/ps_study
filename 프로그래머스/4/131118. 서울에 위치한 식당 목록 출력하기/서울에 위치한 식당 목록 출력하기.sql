-- 코드를 입력하세요
SELECT I.REST_ID, I.REST_NAME, I.FOOD_TYPE, I.FAVORITES, I.ADDRESS, R.score as SCORE
from
    REST_INFO as I
join (select REST_ID, ROUND(AVG(REVIEW_SCORE), 2) as score from REST_REVIEW group by REST_ID) as R
    on I.REST_ID = R.REST_ID
where I.ADDRESS like '서울%'
order by R.score desc, I.FAVORITES desc