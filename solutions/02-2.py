import pandas as pd

def read_weather_data(url):
    data = pd.read_csv(url, index_col=['CST'], parse_dates=['CST'])
    data.columns = data.columns.str.strip()
    for event in ['Thunderstorm', 'Fog', 'Rain']:
        data[event] = data[' Events'].str.contains(event)

    return data