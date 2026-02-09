import matplotlib.pyplot as plt
import numpy as np

# 1. 数据部分 (已替换为 CSV 文件中的新数据)
v_naoh = np.array([
    1.22, 2.32, 3.26, 4.8, 5.87, 7.05, 8.14, 9.18, 10.2, 11.22,
    12.25, 13.47, 13.6, 13.72, 13.81,13.99, 14.10, 14.96, 16.2, 17
])

ph = np.array([
    3, 3.63, 3.95, 4.25, 4.43, 4.61, 4.74, 4.9, 5.08, 5.27,
    5.57, 6.32, 6.7, 7.7, 9.4,10.8,11.0, 11.43, 11.74, 11.86
])

# 2. 计算一阶导数 (ΔpH / ΔV)
dv1 = np.diff(v_naoh)
dph1 = np.diff(ph)
# 防止除以0
with np.errstate(divide='ignore', invalid='ignore'):
    deriv1 = dph1 / dv1

v_mid1 = (v_naoh[:-1] + v_naoh[1:]) / 2  # 一阶导数对应的体积中点

# 3. 计算二阶导数 (Δ(ΔpH/ΔV) / ΔV)
dv2 = np.diff(v_mid1)
dderiv1 = np.diff(deriv1)
with np.errstate(divide='ignore', invalid='ignore'):
    deriv2 = dderiv1 / dv2

v_mid2 = (v_mid1[:-1] + v_mid1[1:]) / 2  # 二阶导数对应的体积中点

# 4. 绘图 (三子图模式)
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 12), sharex=True)

# 子图1: 滴定曲线
ax1.plot(v_naoh, ph, 'o-', color='tab:blue', label='pH Curve', markersize=4)
ax1.set_ylabel('pH', fontsize=12)
ax1.set_title('Titration Analysis: pH, 1st & 2nd Derivatives', fontsize=14)
ax1.grid(True, linestyle='--', alpha=0.6)
ax1.legend()

# 子图2: 一阶导数
ax2.plot(v_mid1, deriv1, 's-', color='tab:red', label='dpH / dV (1st Deriv)', markersize=4)
ax2.set_ylabel('dpH / dV', fontsize=12)
ax2.grid(True, linestyle='--', alpha=0.6)
ax2.legend()

# 子图3: 二阶导数
ax3.plot(v_mid2, deriv2, 'D-', color='tab:green', label='d^2pH / dV^2 (2nd Deriv)', markersize=4)
ax3.set_xlabel('V(NaOH) / mL', fontsize=12)
ax3.set_ylabel('d^2pH / dV^2', fontsize=12)
ax3.axhline(0, color='black', linewidth=1, linestyle='-')  # 绘制 0 值参考线
ax3.grid(True, linestyle='--', alpha=0.6)
ax3.legend()

# 5. 标注理论滴定终点 (在一阶导数最大处)
# 注意：你的数据中有一个点 (14.96, 11.43) pH值有所下降，这可能会影响局部导数计算
max_idx = np.argmax(deriv1)
v_eq = v_mid1[max_idx]
# 对应原始pH大概位置
ph_at_max = ph[max_idx]

ax1.annotate(f'Equivalence Point\nV ≈ {v_eq:.2f} mL',
             xy=(v_eq, ph_at_max),
             xytext=(v_eq - 6, ph_at_max - 2), # 调整了下位置防止遮挡
             arrowprops=dict(facecolor='black', shrink=0.05, width=1))

print(f"基于当前数据检测到的等当点体积: {v_eq:.2f} mL")
print(f"一阶导数最大值: {np.max(deriv1):.2f}")

plt.tight_layout()
plt.show()