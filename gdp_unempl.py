"""Using GDP and employment data from the web.
In economics, the gross domestic product (GDP) is a measure of how much a country has produced.
Economists use this number to gauge how well the economy is doing in a country.
The unemployment rate is another measure.  However, the unemployment rate is called a
lagging economic indicator because the rate typically does not go down until the economy
starts to pick up again.
"""
import datetime

import requests
import matplotlib.pyplot as plt
from matplotlib.dates import YearLocator

COUNTRY = 'usa'
UNEMPLOYMENT_URI = 'http://api.worldbank.org/countries/%s/indicators/SL.UEM.TOTL.ZS?format=json&date=1991:2014'
GDP_URI = 'http://api.worldbank.org/countries/%s/indicators/NY.GDP.MKTP.KD.ZG?format=json&date=1991:2014'


years = YearLocator()   # every year

gdp = requests.get(GDP_URI % COUNTRY)
payload = gdp.json()[1]  # fetch payload
dates_range = [datetime.datetime(int(i['date']), 1, 1) for i in payload]
data = [i['value'] for i in payload]  # gather values

unemployment = requests.get(UNEMPLOYMENT_URI % COUNTRY)
payload = unemployment.json()[1]  # fetch payload
unemployment = [i['value'] for i in payload]  # gather values

fig, ax = plt.subplots()
ax.plot(dates_range, data, 'b-')
ax.set_xlabel('Year')

# Make the y-axis label and tick labels match the line color.
ax.set_ylabel('Change in GDP', color='b')
for tl in ax.get_yticklabels():
    tl.set_color('b')

ax2 = ax.twinx()
ax2.plot(dates_range, unemployment, 'r')

# Same as above
ax2.set_ylabel('Unemployment rate', color='r')
for tl in ax2.get_yticklabels():
    tl.set_color('r')

ax.xaxis.set_major_locator(years)
ax.autoscale_view()
ax.grid(True)

fig.autofmt_xdate(rotation='vertical')
plt.title('GDP vs Unemployment')
plt.show()
