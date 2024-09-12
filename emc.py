import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

'''
# Effective Mass Calculation

This script computes the effective mass of electrons by fitting their band structure data with polynomial and curve fitting methods, and visualizes the results. It converts wave vector data to inverse Bohr radii and energy data to Hartrees, applying `numpy.polyfit` and `scipy.optimize.curve_fit` to estimate and compare effective masses, making it a valuable tool for semiconductor physics analysis.
'''

# https://jingyan.baidu.com/article/c275f6ba0e6760e33d756797.html

# 数据定义
x1 = np.array([0, 0.01032, 0.02065, 0.03097, 0.04129])
x2 = 0.5292 * 2 * np.pi / 8.8763999938999998 * x1  # 转换波矢到Bohr半径的倒数
y1 = np.array([2.06515, 2.06646, 2.07006, 2.07506, 2.08028])
y2 = y1 / 27.21  # 转换能量到Hartree

# 方法1：使用np.polyfit进行二次多项式拟合
z = np.polyfit(x2, y2, 2)
m_eff_polyfit = 1 / (2 * z[0])

# 方法2：使用scipy.optimize.curve_fit进行拟合
def parabola(k, a, b, c):
    return a * k**2 + b * k + c

params, params_covariance = curve_fit(parabola, x2, y2)
m_eff_curvefit = 1 / (2 * params[0])

# 打印结果
print("Effective Mass with np.polyfit (in electron mass units):", m_eff_polyfit)
print("Effective Mass with curve_fit (in electron mass units):", m_eff_curvefit)

# 绘图展示
plt.figure(figsize=(10, 5))
plt.scatter(x2, y2, label='Original Data')
k_fit = np.linspace(min(x2), max(x2), 100)
plt.plot(k_fit, np.polyval(z, k_fit), label='Polyfit Curve', linestyle='-')
plt.plot(k_fit, parabola(k_fit, *params), label='Curve_fit Curve', linestyle='--')
plt.xlabel('Wave Vector k (1/Bohr)')
plt.ylabel('Energy E (Hartree)')
plt.legend()
plt.title('Comparison of Effective Mass Estimation Methods')
plt.show()
