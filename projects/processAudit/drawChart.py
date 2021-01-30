# -*- coding: utf-8 -*-


"""
# 要观察三个指标
- 内存
- CPU
- 句柄

* 将每个指标存储在一个 list 或 csv 文件中，每天获取报告时，一键生成可视化的图表曲线
* 告警：
	- 内存 相比初始 内存 占用超过 2MB，则发送邮件告警： 每 10分钟检测一次
	- CPU 相比初始  CPU 占用连续两次检测均超过 2%，则发送邮件告警： 每10s检测一次
	- 句柄 连续检测3次， 超过 600 则发送邮件告警
"""

import numpy as np 
import matplotlib.pyplot as plt 

"""
 - 为 CPU 数据绘图
"""

# 绘制 CPU 图形
def drawCPUChart(listData):
	x = np.linspace(0, 1440, 720)
	plt.plot(x, listData, label="CPU")

	plt.xlabel("Time-min")
	plt.ylabel("%")

	plt.title("nac_agent CPU usage")
	plt.legend()

	plt.savefig("./cpu.png", dpi=400, bbox_inches='tight')


	