--- Creating stg tables for both api data ---
--- For India Covid cases(staging table) ---
create table staging_schema.stg_india_covid (
  StateCode varchar(20),
  Record_Date varchar(20), 
  Confirmed varchar(20), 
  Recovered varchar(20),
  Deceased varchar(20)
);
--- For USA covid cases(staging table) ---
create table staging_schema.stg_US_covid (
    Record_Date varchar(20),
    states varchar(20),
    positive varchar(20),
    negative varchar(20),
    pending varchar(20),
    hospitalizedCurrently varchar(20),
    hospitalizedCumulative varchar(20),
    inIcuCurrently varchar(20),
    inIcuCumulative varchar(20),
    onVentilatorCurrently varchar(20),
    onVentilatorCumulative varchar(20),
    dateChecked varchar(20),
    death varchar(20),
    hospitalized varchar(20),
    totalTestResults varchar(20),
    lastModified varchar(20),
    recovered varchar(20),
    total varchar(20),
    posNeg varchar(20),
    deathIncrease varchar(20),
    hospitalizedIncrease varchar(20),
    negativeIncrease varchar(20),
    positiveIncrease varchar(20),
    totalTestResultsIncrease varchar(20),
    given_hash varchar(20)
);
--- For India Covid cases(BIDatamart table) ---
create table BIDatamart.india_covid (
  StateCode varchar(10),
  Record_Date date, 
  Confirmed int(20), 
  Recovered int(20),
  Deceased int(20)
);
--- For USA Covid cases(BIDatamart table) ---
create table BIDatamart.US_covid (
    Record_Date date(20),
    states int(20),
    positive int(20),
    negative int(20),
    pending int(20),
    hospitalizedCurrently int(20),
    hospitalizedCumulative int(20),
    inIcuCurrently int(20),
    inIcuCumulative varchar(20),
    onVentilatorCurrently int(20),
    onVentilatorCumulative int(20),
    dateChecked varchar(20),
    death int(20),
    hospitalized int(20),
    totalTestResults int(20),
    lastModified varchar(20),
    recovered int(20),
    total int(20),
    posNeg int(20),
    deathIncrease int(20),
    hospitalizedIncrease int(20),
    negativeIncrease int(20),
    positiveIncrease int(20),
    totalTestResultsIncrease int(20),
    given_hash varchar(20)
);