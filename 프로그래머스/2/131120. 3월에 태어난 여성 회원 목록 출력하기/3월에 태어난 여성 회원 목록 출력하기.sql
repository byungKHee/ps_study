-- 코드를 입력하세요
SELECT MEMBER_ID,
    MEMBER_NAME,
    GENDER, 
    DATE_FORMAT(DATE_OF_BIRTH, '%Y-%m-%d') as DATE_OF_BIRTH
from MEMBER_PROFILE
where GENDER = 'W'
    and DATE_FORMAT(DATE_OF_BIRTH, '%m') = '03'
    and TLNO is not NULL
order by MEMBER_ID