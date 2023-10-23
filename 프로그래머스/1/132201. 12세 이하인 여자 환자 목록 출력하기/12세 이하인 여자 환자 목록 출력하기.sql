SELECT PT_NAME, PT_NO, GEND_CD, AGE, ifnull(TLNO, 'NONE')
from PATIENT
where GEND_CD = 'W' and AGE < 13
order by AGE desc, PT_NAME