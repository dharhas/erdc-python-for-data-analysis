"download temperature for ten stations from wunderground and anonymize the cities"
import pandas as pd

url = 'https://www.wunderground.com/history/airport/{}/{}/1/1/CustomHistory.html?dayend=31&monthend=12&yearend={}&req_city=&req_state=&req_statename=&reqdb.zip=&reqdb.magic=&reqdb.wmo=&format=1'
for year in range(2010, 2016):
    data = []
    for station in ['KCLT', 'KCQT', 'KHOU', 'KIND', 'KJAX',
                    'KMDW', 'KNYC', 'KPHL', 'KPHX', 'KSEA']:
        station_data = pd.read_csv(url.format(station, year, year), index_col=[0], usecols=[0, 2], parse_dates=True)
        station_data = station_data.resample('W').mean()
        data.append(station_data)

    data = pd.concat(data, axis=1).T
    #remove 53rd week
    data.iloc[:,:-1].to_csv('city_temperatures_{}.csv'.format(year), header=False, index=False, float_format='%.0f')