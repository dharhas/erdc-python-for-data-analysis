from bokeh.charts import TimeSeries, show, output_file

def read_weather_data(url):
    data = pd.read_csv(url, parse_dates=['CST'])
    data.columns = data.columns.str.strip()

    return data

vicksburg_data = read_weather_data(vicksburg_url)
austin_data = read_weather_data(austin_url)

data = dict(
    VICKSBURG = vicksburg_data['Mean TemperatureF'],
    AUSTIN = austin_data['Mean TemperatureF'],
    Date=vicksburg_data['CST'],
)

tsline = TimeSeries(data,
    x='Date', y=['VICKSBURG', 'AUSTIN'],
    color=['VICKSBURG', 'AUSTIN'], dash=['VICKSBURG', 'AUSTIN'],
    title="2015", ylabel='Mean TemperatureF', legend=True)

output_file("timeseries.html")
show(tsline)