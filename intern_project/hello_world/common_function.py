import requests
from datetime import date,timedelta

def api_to_json(url):
    response=requests.get(url)
    data_json=response.json()
    return data_json

def changedates(event):
    if event['changedate']=="":
        changedate=date.today() - timedelta(days=365 * 2)
    else:
        changedate=event['changedate']
    return changedate

