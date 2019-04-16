import requests, json, datetime

def getPSI():
    time_now = datetime.datetime.now()
    time_now = time_now.strftime('%Y-%m-%dT%H:%M:%S')

    url = 'https://api.data.gov.sg/v1/environment/psi'
    params = {'date_time':time_now}
    response = requests.get(url,params=params)
    response = response.json()

getPSI()