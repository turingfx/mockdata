import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# 读取两个 CSV 文件
df1 = pd.read_csv('cpumock2.csv', names=['timestamp', 'value'], parse_dates=['timestamp'])
df2 = pd.read_csv('cpumock2_mw_2.csv', names=['timestamp', 'value'], parse_dates=['timestamp'])

# 排序
df1.sort_values('timestamp', inplace=True)
df2.sort_values('timestamp', inplace=True)

# 绘图
plt.figure(figsize=(14, 6))

# 第一条曲线 - 蓝色
plt.plot(df1['timestamp'], df1['value'],
         linewidth=1.5, color='#2E86AB',
         marker='o', markersize=3, label='Data 1', alpha=0.8)

# 第二条曲线 - 橙色
plt.plot(df2['timestamp'], df2['value'],
         linewidth=1.5, color='#F77F00',
         marker='s', markersize=3, label='Data 2', alpha=0.8)

# 格式化
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d %H:%M'))
plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=2))

plt.title('Comparison of Two Time Series', fontsize=14, fontweight='bold')
plt.xlabel('Time', fontsize=12)
plt.ylabel('Value', fontsize=12)
plt.legend(loc='best', fontsize=11)
plt.grid(True, alpha=0.3)
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig('comparison.png', dpi=300)
plt.show()

# 打印统计
print("=== Data 1 ===")
print(f"Max: {df1['value'].max():.2f}, Min: {df1['value'].min():.2f}, Avg: {df1['value'].mean():.2f}")
print("\n=== Data 2 ===")
print(f"Max: {df2['value'].max():.2f}, Min: {df2['value'].min():.2f}, Avg: {df2['value'].mean():.2f}")
