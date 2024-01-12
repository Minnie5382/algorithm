# SELECT MCDP_CD as '진료과코드', COUNT(*) as '5월예약건수'
# FROM APPOINTMENT
# WHERE YEAR(APNT_YMD) = 2022 and MONTH(APNT_YMD) = 5
# GROUP BY MCDP_CD
# ORDER BY '5월예약건수' asc, '진료과코드' desc;

SELECT
    MCDP_CD as "진료과코드"
    , count(APNT_NO) as "5월예약건수"
from APPOINTMENT
where APNT_YMD like "2022-05-%"
group by MCDP_CD
order by 2 asc, 1 asc


