# -*- coding: utf-8 -*-

from meteoswiss import meteoswiss

yearlist = []
templist = []
for station in meteoswiss:
	print(station, ':', meteoswiss[station]['station_name'])
	if station == 'SMA': # only Zurich temps
		temps = meteoswiss[station]['temp']
		for key,value in temps.items():
			month = key.split('-')[-1]
			if month == '06': # only June
				yearlist.append(key.split('-')[0])
				templist.append(value)

import matplotlib.pyplot as plt
plt.plot(yearlist,templist,'ro')
plt.xlabel('Year')
plt.ylabel('Temperature (C)')
plt.title('Average June Temperature in Zurich')
#plt.grid(True)
plt.show()