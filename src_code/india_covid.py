import s3fs
import common_function
import pandas as pd

class Indian:
    def fetch_and_store_data():
        state_data = []
        url = f"https://data.covid19india.org/v4/min/timeseries.min.json"
        data_json = common_function.api_to_json(url)

        # Dictionary to map state codes to state names
        state_code_to_name = {
            "AN": "Andaman and Nicobar Islands",
            "AP": "Andhra Pradesh",
            "AR": "Arunachal Pradesh",
            "AS": "Assam",
            "BR": "Bihar",
            "CH": "Chandigarh",
            "CT": "Chhattisgarh",
            "DL": "Delhi",
            "DN": "Dadra and Nagar Haveli and Daman and Diu",
            "GA": "Goa",
            "GJ": "Gujarat",
            "HP": "Himachal Pradesh",
            "HR": "Haryana",
            "JH": "Jharkhand",
            "JK": "Jammu and Kashmir",
            "KA": "Karnataka",
            "KL": "Kerala",
            "LA": "Ladakh",
            "LD": "Lakshadweep",
            "MH": "Maharashtra",
            "ML": "Meghalaya",
            "MN": "Manipur",
            "MP": "Madhya Pradesh",
            "MZ": "Mizoram",
            "NL": "Nagaland",
            "OR": "Odisha",
            "PB": "Punjab",
            "PY": "Puducherry",
            "RJ": "Rajasthan",
            "SK": "Sikkim",
            "TG": "Telangana",
            "TN": "Tamil Nadu",
            "TR": "Tripura",
            "TT": "Total Tested",
            "UN": "Unknown",
            "UP": "Uttar Pradesh",
            "UT": "Uttarakhand",
            "WB": "West Bengal"
        }

        for state_code, state_info in data_json.items():
            for date, stats in state_info["dates"].items():
                # Get the state name from the state_code_to_name dictionary
                state_name = state_code_to_name.get(state_code, "Unknown")

                row = {
                    "StateName": state_name,  # Use StateName instead of StateCode
                    "Record_Date": date,
                    "Confirmed": stats.get("total", {}).get("confirmed", 0),
                    "Recovered": stats.get("total", {}).get("recovered", 0),
                    "Deceased": stats.get("total", {}).get("deceased", 0),
                }
                state_data.append(row)
        df = pd.DataFrame(state_data)
        filename = "s3://projectdev1/india_covid_data.csv"
        df.to_csv(filename, index=False)
        print("Filename is done:", filename)
        return filename






    




    