# -*- coding: utf-8 -*-
import requests
from collections import defaultdict
import json

stationlist = ['BER','BAS','CHM','CHD','GSB', \
				'DAV','ENG','GVE','LUG','PAY', \
				'SIA','SIO','SAE','SMA']

#stationlist = ['SMA'] # debugging

urlbase = 'http://www.meteoswiss.admin.ch/files/kd/homogreihen/homog_mo_'

data = defaultdict(dict)

for station_code in stationlist:
	url = urlbase + station_code +'.txt'
	resp = requests.get(url=url)

	tosave = 'homog_mo_'+station_code+'.txt'

	#print resp.status_code
	#print resp.headers
	#print resp.encoding

	temp = resp.text
	temp = temp.encode('utf-8').split('\r\n')
	temp = [x.strip() for x in temp]
	station_name = temp[5].split(':')[-1].strip()
	print station_code, ':', station_name

	data[station_code].update({ 'source_url' : url }) # source URL
	data[station_code].update({ 'station_name' : station_name }) # full name of station

	data[station_code].update({ temp[6].split(':')[0].strip() : temp[6].split(':')[-1].strip() }) # altitude
	data[station_code].update({ temp[7].split(':')[0].strip() : temp[7].split(':')[-1].strip() }) # coordinates
	
	data[station_code].update({ temp[18].split(':')[0].strip() +' - '+ temp[17]: temp[18].split(':')[-1].strip() }) # temp units
	data[station_code].update({ temp[19].split(':')[0].strip() +' - '+ temp[17]: temp[19].split(':')[-1].strip() }) # precip units

	data[station_code].update({ temp[23].split(':')[0].strip() : temp[23].split(':')[-1].strip() }) # data source
	data[station_code].update({ temp[24].split(':')[0].strip() : temp[24].split(':')[-1].strip() }) # creation date

	header = temp[27].split()
	header = [x.strip() for x in header]
	#print header

	data[station_code]['temp'] = {}
	data[station_code]['precip'] = {}

	for i in xrange(28,len(temp)):
		row = temp[i].split()
		row = [x.strip() for x in row]
		for j in xrange(len(row)):
			datekey = '-'.join((row[0],row[1].zfill(2))) # padded month (i.e. 2014-04)
			data[station_code]['temp'][datekey] = row[2]
			data[station_code]['precip'][datekey] = row[3]

with open('meteoswiss.json','wb') as outfile:
	json.dump(data,outfile,indent=4,encoding='utf-8',ensure_ascii=False)

with open('meteoswiss.py','wb') as outfile:
	outfile.write('# -*- coding: UTF-8 -*-\n')
	outfile.write('meteoswiss = '+json.dumps(data,encoding='utf-8', ensure_ascii=False)+'\n')
	#json.dump(data,out,indent=4,encoding='utf-8',ensure_ascii=False)