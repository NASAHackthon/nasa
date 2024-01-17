# askForData.py - retrieve the data which are in the range of minimum time
# and maximun time from mongodb database, and print them out

from pymongo import MongoClient

# connect to local database
client = MongoClient('mongodb://localhost:27017')
db = client.moonquake
collection = db.moonquakes

# example input
year_max = 1974
month_max = 1
date_max = 5
hr_max = 12
min_max = 34
sec_max = 59.2
year_min = 1973
month_min = 5
date_min = 24
hr_min = 4
min_min = 29
sec_min = 14.5

'''
# 拆分比較需考慮時間問題的各種Case
# Case 1:
if (hr_max > hr_min)
for moonquake in moonquakes.find({"$and":[{"time.Year":{"$gte":year_min}}, {"time.Year":{"$lte":year_max}},
                                          {"time.hr":{"$gte":hr_min}}, {"time.hr":{"$lte":hr_max}},
                                          {"time.min":{"$gte":min_min}}, {"time.min":{"$lte":min_max}},
                                          {"time.sec":{"$gte":sec_min}}, {"time.sec":{"$lte":sec_max}}]}):
  print(moonquake)
......
'''

# 合併比較較省事
maxi = str(year_max) + str(month_max) + str(date_max) + str(hr_max) + str(min_max) + str(sec_max)
mini = str(year_min) + str(month_min) + str(date_min) + str(hr_min) + str(min_min) + str(sec_min)

for moonquake in collection.find({"$and":[{"time_cmp":{"$lte":maxi}}, {"time_cmp":{"$gte":mini}}]}):
    # find designated data and do whatever you like 
    print(moonquake)
