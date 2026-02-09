import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

# 设置随机种子以保证结果可重复
np.random.seed(42)


def random_walk_3d(n_steps):
    """
    生成三维随机游走的数据
    :param n_steps: 游走的步数
    :return: 包含所有坐标点的数组
    """
    # 定义 6 个可能的移动方向：上下、左右、前后
    directions = np.array([
        [1, 0, 0], [-1, 0, 0],
        [0, 1, 0], [0, -1, 0],
        [0, 0, 1], [0, 0, -1]
    ])

    # 从 6 个方向中随机抽取 n_steps 次
    random_indices = np.random.randint(0, len(directions), size=n_steps)
    steps = directions[random_indices]

    # 使用累加函数 (cumsum) 计算每一步的位置，初始点为 (0,0,0)
    path = np.vstack([[0, 0, 0], np.cumsum(steps, axis=0)])
    return path


# 模拟 5000 步
n_steps = 5000
path = random_walk_3d(n_steps)

# 提取坐标
x, y, z = path[:, 0], path[:, 1], path[:, 2]

# 绘图
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# 绘制路径，设置 alpha 透明度使重叠轨迹更清晰
ax.plot(x, y, z, alpha=0.7, lw=0.6, color='royalblue')

# 标记起点和终点
ax.scatter(x[0], y[0], z[0], color='green', s=100, label='Start (0,0,0)', edgecolors='black')
ax.scatter(x[-1], y[-1], z[-1], color='red', s=100, label=f'End ({x[-1]}, {y[-1]}, {z[-1]})', edgecolors='black')

# 设置图表标签
ax.set_title(f"3D Random Walk Simulation ({n_steps} steps)")
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.legend()

# plt.savefig('random_walk_3d.png')
plt.show()