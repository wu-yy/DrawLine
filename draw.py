# encoding=utf-8
import matplotlib.pyplot as plt
from pylab import *
import numpy as np
mpl.rcParams['font.sans-serif'] = ['SimHei']
x = [1,2,3]
y = [91.52631579,89.47619048,88
,87.375
,83.22580645
,83.41176471
,81.23809524
,81.0952381
,80.15789474
,81.64705882
,77.57142857
,76.21052632
,74.57894737
,75.94117647
,70.4
,70.51851852
,69.0952381
,66.65625
,67.22222222
]
y_mean=np.mean(y)
print(y_mean)
y1=[91.52631579,89.47619048,88]
y2=[69.0952381,66.65625,67.22222222]
y3=[y_mean,y_mean,y_mean]
#plt.plot(x, y, 'ro-')
#plt.plot(x, y1, 'bo-')
#pl.xlim(-1, 11)  # 限定横轴的范围
plt.ylim(60, 100)  # 限定纵轴的范围
plt.plot(x, y1, marker='o', mec='r', mfc='w',label=u'前三名成绩')
plt.plot(x, y2, marker='*', ms=10,label=u'后三名成绩')
plt.plot(x, y3, ms=10,label=u'平均值78.7')
plt.legend()  # 让图例生效
plt.xticks(x, x, rotation=45)
plt.margins(0)
plt.subplots_adjust(bottom=0.15)
plt.xlabel(u"标号") #X轴标签
plt.ylabel("必修+限选+任选") #Y轴标签
plt.title("班级成绩") #标题

plt.show()