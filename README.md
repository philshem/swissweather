swissweather
============

Historical monthly averages (1864-present) of temperature and precipitation at weather stations across Switzerland. All data is from MeteoSwiss and their license applies to its usage.

Data source: http://www.meteoswiss.admin.ch/web/en/climate/climate_today/homogeneous_data.html
Data license: http://www.meteoswiss.admin.ch/web/en/legal.html

Station code : Station name
BER : Bern / Zollikofen
BAS : Basel / Binningen
CHM : Chaumont
CHD : Château-d'Oex
GSB : Col du Grand St-Bernard
DAV : Davos
ENG : Engelberg
GVE : Genève-Cointrin
LUG : Lugano
PAY : Payerne
SIA : Segl-Maria
SIO : Sion
SAE : Säntis
SMA : Zürich / Fluntern

Usage: 
+ get_meteoswiss.py downloads .txt files from meteoswiss.ch and combines/converts data to a JSON file (meteoswiss.json) and a python module (meteoswiss.py)
+ plot_zurich_temps.py reads meteoswiss.py and plots the average June temperature in Zürich.
