# a stacked bar plot with errorbars
import numpy as np
import matplotlib.pyplot as plt
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']

N = 2
xinxi = (6,0)
guoke= (3, 0)
haijun=(1,0)
other=(0,10)
#menStd = (2, 3, 4, 1, 2)
#womenStd = (3, 5, 2, 3, 3)
ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, xinxi, width, color='#d62728')
p2 = plt.bar(ind, guoke, width,bottom=xinxi)
p3 = plt.bar(ind, haijun, width,bottom=guoke)
p4 = plt.bar(ind, other, width)
plt.ylabel('人数/人')
plt.title('工作外推情况')
plt.xticks(ind, ('G1', 'G2'))
plt.yticks(np.arange(0, 85, 10))
plt.legend((p1[0], p2[0],p3[0],p4[0]), ('外推(信息工程大学7人)', '外推（国防科大3人）','外推（海军工程 1人）','计划工作 10人'))

plt.show()
