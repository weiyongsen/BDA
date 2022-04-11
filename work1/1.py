import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['axes.unicode_minus']=False#解决保存图像时负号'-'显示为方块的问题
plt.rcParams['font.sans-serif'] = ['SimHei']#指定默认字体
s = [13, 15, 16, 16, 19, 20, 20, 21, 22, 22, 25, 25, 25, 25, 30, 33, 33, 35, 35, 35, 35, 36, 40, 45, 46, 52, 70]
l = len(s)
# 均值
m = sum(s)/l
# 中位数
z = s[l//2]
print(l,m,z)

# 绘制盒图
plt.boxplot(s,showmeans=True)
plt.ylim([0, 80])
plt.show()

# 绘制分位图
import scipy.stats as stats
stats.probplot(s, dist="norm" ,plot=plt)
plt.show()