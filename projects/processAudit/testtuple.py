# -*- coding: utf-8 -*-

import numpy as np 
import matplotlib.pyplot as plt 

x = np.linspace(0, 2, 100)

plt.plot(x, x, label="linear")
plt.plot(x, x**2, label="quadratic")
plt.plot(x, x**3, label="cubic")

plt.xlabel('x label') # 横坐标名称
plt.ylabel('y label') # 纵坐标名称

plt.title("Simple Plot") # 图片标题

plt.legend()

# 保存图片到本地， dpi 是像素
plt.savefig(r"test.png", dpi=400, bbox_inches='tight')