swissweather
============

Historical monthly averages (1864-present) of temperature and precipitation at weather stations across Switzerland. All data is from [MeteoSwiss](http://www.meteoswiss.admin.ch/web/en.html) and [their license](http://www.meteoswiss.admin.ch/web/en/legal.html) applies to its usage. I have only combined and transformed the data so it is more code-friendly.

 + [Data source](http://www.meteoswiss.admin.ch/web/en/climate/climate_today/homogeneous_data.html)
 + [Measurement details](http://www.meteoswiss.admin.ch/web/de/klima/klima_heute/homogene_reihen.Par.0054.DownloadFile.tmp/vergleichoriginalhomogen.pdf) (PDF, German)


Station code  | Station name
:---------------:| ---------------
BER | Bern / Zollikofen
BAS | Basel / Binningen
CHM | Chaumont
CHD | Château-d'Oex
GSB | Col du Grand St-Bernard
DAV | Davos
ENG | Engelberg
GVE | Genève-Cointrin
LUG | Lugano
PAY | Payerne
SIA | Segl-Maria
SIO | Sion
SAE | Säntis
SMA | Zürich / Fluntern

#### Usage: 

+ **get_meteoswiss.py** gets multiple .txt files from [meteoswiss.ch](http://www.meteoswiss.admin.ch/files/kd/homogreihen/homog_mo_SMA.txt) and transforms data:
 + JSON file: [meteoswiss.json](https://raw.githubusercontent.com/philshem/swissweather/master/meteoswiss.json)
 + python module: [meteoswiss.py](https://raw.githubusercontent.com/philshem/swissweather/master/meteoswiss.py).

+ **plot_zurich_temps.py** is an example code:
 + loads data from meteoswiss.py
 + selects only Zürich (SMA) as the weather station
 + selects only average June temperatures
 + makes a plot of historical June temperatures in Zürich

```python
from meteoswiss import meteoswiss

yearlist = []
templist = []
for station in meteoswiss:
	print station, ':', meteoswiss[station]['station_name']
	if station == 'SMA': # only Zurich temps
		temps = meteoswiss[station]['temp']
		for key,value in temps.iteritems():
			month = key.split('-')[-1]
			if month == '06': # only June
				yearlist.append(key.split('-')[0])
				templist.append(value)

import matplotlib.pyplot as plt
plt.plot(yearlist,templist,'ro')
plt.xlabel('Year')
plt.ylabel('Temperature (C)')
plt.title('Average June Temperature in Zurich')
plt.grid(True)
plt.show()
```

![Average June Temperature in Zurich](https://raw.githubusercontent.com/philshem/swissweather/master/figure_1.png)

