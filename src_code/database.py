import pandas as pd
import csv
import json
from mysql import connector

class Db:
    def mysql_connection(host,dbase,user,password,port):
        connection=connector.connect(host=host,
                                        database=dbase,
                                        user=user,
                                        password=password,
                                        port=port)
        cursor=connection.cursor()
        return connection,cursor
    
    def india_covid_s3_to_stg(connection,cursor,filename):
        f_e=pd.read_csv(filename)
        df.drop_duplicates(inplace=True)
        data=json.loads(f_e.to_json(orient='records'))
        cursor.execute("truncate table staging_schema.stg_india_covid;")
        connection.commit()
        print("truncate staging")
        for d in data:
            cursor.execute("insert into staging_schema.stg_india_covid values (%s,%s,%s,%s,%s)",list(d.values()))
        connection.commit()
        print("Db Filename is done:", filename)
        return "module is done"
        
    def US_covid_s3_to_stg(connection,cursor,filename):
        df=pd.read_csv(filename)
        data=json.loads(df.to_json(orient='records'))
        cursor.execute("truncate table staging_schema.stg_US_covid;")
        connection.commit()
        for d in data:
            cursor.execute("insert into staging_schema.stg_US_covid values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",list(d.values()))
        connection.commit()
        print("Db Filename is done:", filename)
        return "module is done"
        
    def stored_procedure(connection,cursor,sp_name):
        cursor.execute(f"call {sp_name}")
        connection.commit()







