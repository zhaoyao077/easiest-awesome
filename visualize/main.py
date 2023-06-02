# import pandas as pd
# pd.set_option('display.unicode.east_asian_width',True)
# pd.set_option( 'display.max_columns', None)
# pd.set_option( 'display.max_rows', None)
# path = "data.xlsx"
# df = pd.read_excel(path)
# counts = df['user'].value_counts()
# # 找到出现次数最多的值
# max_count_user = counts.index[0]
# # 使用loc函数根据条件筛选出对应的行数据
# max_count_rows = df.loc[df['user'] == max_count_user]
# # 输出行数据
# print(counts)
# print(max_count_rows)
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.ticker import PercentFormatter
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams["axes.unicode_minus"] = False
# 月份和百分比数据
version = ['v3.3.2' ,'v3.4.0-rc1', 'v3.4.0-rc2', 'v3.4.0-rc3','v3.4.0-rc4','v3.4.0-rc5','v3.4.0','v3.2.4']
# percentage_positive = [16.8,12.6,5.3,11.9,17.4,14.0,23.2,12.3]
# percentage_negative = [8.2,9.1,3.8,10.1,8.9,10.3,7.8,9.6]
# percentage_neural = [75.0,78.3,90.9,78.0,73.7,75.7,69.0,78.1]
# percentage_user6477701_positive = [20.6,12.8,11.1,50.0,16.0,10.8,50.0,10.3]
# percentage_user6477701_negative = [5.9,8.5,7.4,0.0,10.0,16.2,10.0,13.7]
# percentage_user6477701_neural = [73.5,78.7,81.5,50.0,74.0,73.0,40.0,76.0]
percentage_user1475305_positive = [0.0,11.4,5.6,0.0,12.2,14.7,0.0,12.0]
percentage_user1475305_negative = [5.3,14.3,11.1,0.0,7.8,2.9,33.3,9.0]
percentage_user1475305_neural = [94.7,74.3,83.3,100.0,80.0,82.4,66.7,79.0]
# 创建图形对象和子图对象
fig, ax = plt.subplots()
# # 设置字体
font_title = FontProperties(weight='bold', size=20)
font_label = FontProperties(weight='bold',size=15)
# # 绘制三条折线图
# plt.plot(version, percentage_positive, color='red', label='积极文本占比',alpha=0.8)
# plt.plot(version, percentage_negative, color='blue', label='消极文本占比',alpha=0.8)
# plt.plot(version, percentage_neural, color='green', label='中立文本占比',alpha=0.8)
# plt.plot(version, percentage_user6477701_positive, color='red', label='积极文本占比',alpha=0.8)
# plt.plot(version, percentage_user6477701_negative, color='blue', label='消极文本占比',alpha=0.8)
# plt.plot(version, percentage_user6477701_neural, color='green', label='中立文本占比',alpha=0.8)
plt.plot(version, percentage_user1475305_positive, color='red', label='积极文本占比',alpha=0.8)
plt.plot(version, percentage_user1475305_negative, color='blue', label='消极文本占比',alpha=0.8)
# plt.plot(version, percentage_user1475305_neural, color='green', label='中立文本占比',alpha=0.8)
# for i in range(len(version)):
#     plt.text(version[i], percentage_positive[i], f'{percentage_positive[i]:.1f}%', ha='center', va='bottom',color='red',fontsize=20)
# for i in range(len(version)):
#     plt.text(version[i], percentage_negative[i], f'{percentage_negative[i]:.1f}%', ha='center', va='bottom',color='blue',fontsize=20)
# for i in range(len(version)):
#     plt.text(version[i], percentage_neural[i], f'{percentage_neural[i]:.1f}%', ha='center', va='bottom',color='green',fontsize=20)
# for i in range(len(version)):
#     plt.text(version[i], percentage_user6477701_positive[i], f'{percentage_user6477701_positive[i]:.1f}%', ha='center', va='bottom',color='red',fontsize=20)
# for i in range(len(version)):
#     plt.text(version[i], percentage_user6477701_negative[i], f'{percentage_user6477701_negative[i]:.1f}%', ha='center', va='bottom',color='blue',fontsize=20)
# for i in range(len(version)):
#     plt.text(version[i], percentage_user6477701_neural[i], f'{percentage_user6477701_neural[i]:.1f}%', ha='center', va='bottom',color='green',fontsize=20)
for i in range(len(version)):
    plt.text(version[i], percentage_user1475305_positive[i], f'{percentage_user1475305_positive[i]:.1f}%', ha='center', va='bottom',color='red',fontsize=20)
for i in range(len(version)):
    plt.text(version[i], percentage_user1475305_negative[i], f'{percentage_user1475305_negative[i]:.1f}%', ha='center', va='bottom',color='blue',fontsize=20)
# for i in range(len(version)):
#     plt.text(version[i], percentage_user1475305_neural[i], f'{percentage_user1475305_neural[i]:.1f}%', ha='center', va='bottom',color='green',fontsize=20)
# 设置标题、图例和坐标轴标签
plt.title("情绪文本占比波动图（个人）", fontproperties=font_title)
plt.legend()
plt.xlabel('Group Version', fontproperties=font_label)
plt.ylabel('Percentage', fontproperties=font_label)
plt.xticks(fontsize=18)
plt.yticks(fontsize=18)
plt.gca().yaxis.set_major_formatter(PercentFormatter(100))
for y in ax.yaxis.get_ticklocs():
    ax.axhline(y, color='gray', alpha=0.5, linewidth=0.5)
# 显示图形
plt.show()


