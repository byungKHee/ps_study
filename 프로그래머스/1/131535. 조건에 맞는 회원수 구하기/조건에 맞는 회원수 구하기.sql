-- 코드를 입력하세요
SELECT count(USER_ID)
FROM USER_INFO
WHERE JOINED between '2021-01-01' and '2021-12-31'
    and AGE between 20 and 29;
