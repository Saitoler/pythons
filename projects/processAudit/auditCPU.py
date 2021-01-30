# -*- coding: utf-8 -*-

import proInfoGet
import time
import datetime

"""
- 监控 nac_agent.exe 的 CPU，保存数据到列表中
- 用于可视化画图时使用
- 数据获取频率: 10min 采集一次

"""


curHour = datetime.datetime.now().strftime('%H')
curMin = datetime.datetime.now().strftime('%M')


cpuData = []


while True:
	cpu = proInfoGet.getCpuPercentByName("nac_agent.exe")

	cpuData.append(cpu)
	# 10min 采集一次数据
	time.sleep(600)

	# 
	if "23" == curHour and curMin > "50":
		# drawChart(cpuData) 画图并保存到文件中
		cpuData.clear()
		sleep(600)







