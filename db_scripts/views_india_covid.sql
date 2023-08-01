create view BIDatamart.vw_statewise_cases as (
select
    StateCode as StateCode,
    SUM(Confirmed) as total_confirmed,
    SUM(Recovered) as total_recovered,
    SUM(Deceased) as total_deceased
from
    BIDatamart.india_covid
group by
    india_covid.StateCode
)