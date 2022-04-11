import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['axes.unicode_minus']=False#解决保存图像时负号'-'显示为方块的问题
plt.rcParams['font.sans-serif'] = ['SimHei']#指定默认字体
nl = [23,23,27,27,39,41,47,49,50,52,54,54,56,57,58,58,60,61]
tz = [9.5,26.5,7.8,17.8,31.4,25.9,27.4,27.2,31.2,34.6,42.5,28.8,33.4,30.2,34.1,32.9,41.2,35.7]

# print(nl,len(nl))
# print(tz,len(tz))
l = len(nl)
# 均值
nl_mean = np.mean(nl)
tz_mean = np.mean(tz)
print(nl_mean,tz_mean)
# 中位数
nl_middle = (nl[l//2] + nl[l//2-1])//2
tz_middle = (tz[l//2] + tz[l//2-1])//2
print(nl_middle,tz_middle)
# 标准差
nl_std = np.std(nl,ddof=1)
tz_std = np.std(tz,ddof=1)
print(nl_std,tz_std)

plt.boxplot([nl,tz],labels=["年龄","体脂率"])
plt.title("盒图")
plt.show()

import seaborn as sns
import pandas as pd
# Q-Q图
ls1 = sorted(nl)
ls2 = sorted(tz)
sns.regplot(pd.Series(ls1),pd.Series(ls2),ci=None, color="b",line_kws={"color":"r"})
plt.xlabel("年龄")
plt.ylabel("体脂率")
plt.title("Q-Q")
plt.show()
# 散点图
plt.scatter(nl,tz)
plt.xlabel("年龄")
plt.ylabel("体脂率")
plt.title("散点")
plt.show()
