import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

# ==========================================
# 1. 数据准备
# ==========================================
# 修改：横坐标值 (标准浓度 rho)
std_rho = np.array([0.0, 2.0, 4.0, 6.0, 8.0, 10.0])
# 对应的吸光度 A (保持不变)
abs_val = np.array([0.000, 0.233, 0.466, 0.692, 0.892, 1.137])
# 待测样品的吸光度
sample_abs = [0.686, 0.674]

# ==========================================
# 2. 线性回归计算
# ==========================================
slope, intercept, r_value, p_value, std_err = stats.linregress(std_rho, abs_val)
r_squared = r_value**2

# ==========================================
# 3. 绘图
# ==========================================
fig, ax = plt.subplots(figsize=(10, 6))

# (1) 绘制标准点
ax.scatter(std_rho, abs_val, color='blue', s=80, label='Standard Points', zorder=5)

# (2) 绘制拟合直线
# 修改：调整拟合线的x范围以覆盖新的横坐标 (0到11)
x_fit = np.linspace(0, 11, 100)
y_fit = slope * x_fit + intercept
label_text = f'Regression Line\nA = {slope:.4f}$\\rho$ + {intercept:.4f}\n$R^2$ = {r_squared:.4f}'
ax.plot(x_fit, y_fit, color='red', linestyle='--', linewidth=2, label=label_text)

# (3) 计算并标记待测样品
sample_calcs = [(a - intercept) / slope for a in sample_abs]
ax.scatter(sample_calcs, sample_abs, color='green', marker='x', s=100, label='Samples', zorder=5)

# 辅助函数：添加箭头注释
def add_annotation(idx, x, y, xytext_offset):
    ax.annotate(f'Sample {idx+1}\n({x:.2f}, {y:.3f})',
                xy=(x, y), xycoords='data',
                xytext=xytext_offset, textcoords='offset points',
                fontsize=9, color='green', fontweight='bold',
                arrowprops=dict(arrowstyle="->", color='green', connectionstyle="arc3,rad=.2"))
    # 添加辅助虚线
    ax.plot([x, x], [0, y], color='green', linestyle=':', alpha=0.4)
    ax.plot([0, x], [y, y], color='green', linestyle=':', alpha=0.4)

# 标记 Sample 1 (标签放在左下方)
add_annotation(0, sample_calcs[0], sample_abs[0], xytext_offset=(-80, -60))

# 标记 Sample 2 (标签放在右上方)
add_annotation(1, sample_calcs[1], sample_abs[1], xytext_offset=(40, 40))

# ==========================================
# 4. 图表美化
# ==========================================
ax.set_title('Standard Curve for Iron Determination', fontsize=14)
# 保持之前的标签修改
ax.set_xlabel(r'$\rho$ / (mg$\cdot$mL$^{-1}$)', fontsize=12)
ax.set_ylabel('Absorbance A', fontsize=12)
ax.legend(loc='upper left', frameon=True, shadow=True)
ax.grid(True, linestyle='--', alpha=0.5)

# 修改：扩大坐标轴显示范围
ax.set_xlim(-0.5, 11.0)
ax.set_ylim(0, 1.3)

plt.tight_layout()
plt.show()