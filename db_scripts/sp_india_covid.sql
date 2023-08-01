-- truncate and moving data from staging_schema.stg_india_covid to BIDatamart.india_covid ---
create procedure BIDatamart.sp_india_covid()
begin
	truncate table BIDatamart.india_covid;
	insert into BIDatamart.india_covid
	  (	 StateCode,
    	 Record_Date,
    	 Confirmed,
    	 Recovered,
    	 Deceased
	  )
	select StateCode,
    	 Record_Date,
    	 Confirmed,
    	 Recovered,
    	 Deceased
    from staging_schema.stg_india_covid;
end;