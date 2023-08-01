import common_function
import US_covid
import india_covid
import database
import creds

def lambda_handler(event, context):
    if event['modulename']=="US_covid":
        USA_cases=US_covid.American
        changedate=common_function.changedates(event)
        file_name=USA_cases.process_data(event,changedate)
        host,dbase,user,password,port=creds.mysql_creds()
        db_obj=database.Db
        connection,cursor=db_obj.mysql_connection(host,dbase,user,password,port)
        db_obj.US_covid_s3_to_stg(connection,cursor,file_name)
        db_obj.stored_procedure(connection,cursor,"BIDatamart.sp_US_covid()")
        return f"{event['modulename']} module is successfully completed"
    
    elif event['modulename']=="india_covid":
        india_cases=india_covid.Indian
        file_name_1=india_cases.fetch_and_store_data()
        host,dbase,user,password,port=creds.mysql_creds()
        db_obj=database.Db
        connection,cursor=db_obj.mysql_connection(host,dbase,user,password,port)
        db_obj.india_covid_s3_to_stg(connection,cursor,file_name_1)
        db_obj.stored_procedure(connection,cursor,"BIDatamart.sp_india_covid()")
        return f"{event['modulename']} module is successfully completed"
    else:
        return f"{event['modulename']} module is not successfully completed"




