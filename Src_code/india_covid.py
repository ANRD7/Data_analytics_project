import s3fs
import common_function
import pandas as pd

class Indian:
    def fetch_and_store_data():
        state_data = []
        url = f"https://data.covid19india.org/v4/min/timeseries.min.json"
        data_json=common_function.api_to_json(url)
        for state_code, state_info in data_json.items():
            for date, stats in state_info["dates"].items():
                row = {
                    "StateCode": state_code,
                    "Record_Date": date,
                    "Confirmed": stats.get("total", {}).get("confirmed", 0),
                    "Recovered": stats.get("total", {}).get("recovered", 0),
                    "Deceased": stats.get("total", {}).get("deceased", 0),
                }
                state_data.append(row)
        df = pd.DataFrame(state_data)
        filename="s3://projectdev1/india_covid_data.csv"
        df.to_csv(filename,index=False)
        print("Filename is done:", filename)
        return filename




    