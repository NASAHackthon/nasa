#! python3
# dataCollector.py - collect moonquake data and convert it into json file
# data will includes informations like name, latitude, longtitude, depth, type, time

import json, csv

data_list = []

# process data in lognonne_2003_catalog.csv
# replace with file's path in your computor
m = 0
sh = 0
file = open("C:\\Users\Cooki\\Desktop\\nasa_hacker\\dataCollector\\lognonne_2003_catalog.csv")
reader = csv.reader(file)
for row in reader:
    data = {}
    # skip first line
    if (reader.line_num != 1):
        # determine type and name
        if (row[0] == 'M'):
            m += 1
            name = 'M' + str(m)
            typ = 'Meteoroid Impact'
        elif (row[0] == 'SH'):
            sh += 1
            name = 'SM' + str(sh)
            typ = 'Shallow Moonquake'
        elif (row[0][0] == 'A'):
            name = row[0]
            typ = 'Deep Moonquake'
        else:
            name = row[0]
            typ = 'Artificial Impact'
        data['name'] = name
        data['type'] = typ
        # determine depth
        if (row[3]):
            dep = int(row[3])
        else:
            dep = 0
        data['depth'] = dep
        # determine latitude and longtitude
        lat = float(row[1])
        data['latitude'] = lat
        long = float(row[2])
        data['longtitude'] = long
        # determine time
        time = {}
        year = int('19' + row[8][:2])
        time['Year'] = year
        month = int(row[8][2:4])
        time['month'] = month
        date = int(row[8][4:6])
        time['date'] = date
        hour = int(row[8][6:8])
        time['hr'] = hour
        minute = int(row[8][8:])
        time['min'] = minute
        second = float(row[9])
        time['sec'] = second
        data['time'] = time
        data_list.append(data)

# process data in nakamura_2005_dm_locations.csv
file = open("C:\\Users\\Cooki\\Desktop\\nasa_hacker\\dataCollector\\nakamura_2005_dm_locations.csv")
reader = csv.reader(file)
for row in reader:
    data = {}
    if (reader.line_num != 1):
        name = 'A' + row[0]
        data['name'] = name
        lat = float(row[2])
        data['latitude'] = lat
        long = float(row[4])
        data['longtitude'] = long
        dep = int(row[6])
        data['depth'] = dep
        time = None
        data['time'] = time
        typ = 'Deep Moonquake'
        data['type'] = typ
        data_list.append(data)

with open("moonquake_data", 'w', encoding="utf-8") as file:
    json.dump(data_list, file, ensure_ascii=False, indent=4)
print("資料已儲存")
