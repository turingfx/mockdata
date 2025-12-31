import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# 配置文件列表
files = [
    ('cpumock2.csv', 'Server A', '#2E86AB', 'o'),
    ('cpumock2_mv.csv', 'Server B', '#F77F00', 's'),
    # ('data3.csv', 'Server C', '#06A77D', '^'),  # 可选第三条
]

plt.figure(figsize=(16, 7))

# 循环绘制
for csv_file, label, color, marker in files:
    df = pd.read_csv(csv_file, names=['timestamp', 'value'],
                     parse_dates=['timestamp'])
    df.sort_values('timestamp', inplace=True)

    plt.plot(df['timestamp'], df['value'],
             linewidth=2, color=color, marker=marker,
             markersize=3, label=label, alpha=0.8, markevery=10)

    plt.fill_between(df['timestamp'], df['value'],
                     alpha=0.15, color=color)

# 格式化
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d %H:%M'))
plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=2))

plt.title('Multi-Server Comparison', fontsize=16, fontweight='bold')
plt.xlabel('Time', fontsize=12)
plt.ylabel('CPU %', fontsize=12)
plt.legend(loc='best', fontsize=11)
plt.grid(True, alpha=0.3)
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig('multi_comparison.png', dpi=300)
plt.show()