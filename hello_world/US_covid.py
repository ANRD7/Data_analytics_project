import s3fs
import common_function
import pandas as pd

class American:
    def process_data(event,changedate):
        changedate = event['changedate']
        url = f"https://api.covidtracking.com/v1/us/{changedate}.json"
        data_json=common_function.api_to_json(url)
        row = {}
        for key, value in data_json.items():
            row[key] = value

        df = pd.DataFrame([row])
        df.rename(columns={"date": "Record_date"}, inplace=True)
        filename="s3://projectdev1/US_covid.csv"
        df.to_csv(filename,index=False)
        print("Filename is done:", filename)
        return filename
    
