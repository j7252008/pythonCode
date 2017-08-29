# coding: utf-8
"""
火车票查询
"""

import stations
import requests
import re


date = "2017-09-29"
from_station = stations.getCode("北京") 
to_station = stations.getCode("西安")

url = "https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={}\
&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT".format(date, from_station, to_station)

r = requests.get(url, verify=False)
rawTrains = r.json()['data']['result']

print(date, stations.getName(from_station),stations.getName(to_station))

for rawTrain in rawTrains:
    dataList = rawTrain.split("|")
    
    print(dataList[3], stations.getName(dataList[6]), stations.getName(dataList[7]), "出发:" + dataList[8]
    , "到达:" + dataList[9], "历时:" + dataList[10], dataList[32], dataList[31], dataList[30]
    , "软卧:" + (dataList[23] or "--"), "硬卧:"+dataList[28], "硬座:" + dataList[29], "无座:" + dataList[26])
    # train_num = dataList[3]
    # from_station_code = data_list[6]
    # from_station_name = self.code_dict[from_station_code]
    # to_station_code = data_list[7]
    # to_station_name = self.code_dict[to_station_code]
    # start_time = data_list[8]
    # arrive_time = data_list[9]
    # run_time = data_list[10]
    # special_seat = data_list[32] or '--'
    # first_seat = data_list[31] or '--'
    # second_seat = data_list[30] or '--'
    # soft_sleep = data_list[23] or '--'
    # hard_sleep = data_list[28] or '--'
    # hard_seat = data_list[29] or '--'
    # no_seat = data_list[26] or '--'




# stationUrl = "https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9025"

# rSation = requests.get(stationUrl, verify = False)

# rawStations = re.findall(u'([\u4300-\u9fa5]+)\|([A-Z]+)', rSation.text) 
# dictStations = dict(rawStations) 
