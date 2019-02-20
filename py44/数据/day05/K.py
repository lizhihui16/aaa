# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import matplotlib.pyplot as mp
import datetime as dt
import matplotlib.dates as md

# 定义函数,转换日期格式


def dmy2ymd(dmy):
    dmy = str(dmy, encoding='utf-8')
    date = dt.datetime.strptime(
        dmy, '%d-%m-%Y').date()
    s = date.strftime("%Y-%m-%d")
    return s

# 加载文件
dates, opening_prices, highest_prices, \
    lowest_prices, closing_prices = \
    np.loadtxt(
        '../data/aapl.csv',
        delimiter=',',
        usecols=(1, 3, 4, 5, 6),
        unpack=True,
        dtype='M8[D], f8, f8, f8, f8',
        converters={1:dmy2ymd})

# 绘制收盘价的折线图
mp.figure('AAPL', facecolor='lightgray')
mp.title('AAPL', fontsize=18)
mp.xlabel('Date', fontsize=14)
mp.ylabel('Price', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
#设置刻度定位器, x轴需要显示时间信息
ax = mp.gca()
# x轴主刻度为每周一
ax.xaxis.set_major_locator(
    md.WeekdayLocator(byweekday=md.MO))
ax.xaxis.set_major_formatter(
    md.DateFormatter('%Y-%m-%d'))
# x轴次刻度为每天
ax.xaxis.set_minor_locator(
    md.DayLocator())
# 把日期数组元素类型改为md可识别的类型
dates = dates.astype(md.datetime.datetime)
mp.plot(dates, closing_prices,
        color='dodgerblue', linewidth=3,
        linestyle=':', label='closing_price',
        alpha=0.2)

# 整理蜡烛图所需的颜色
# 填充色
rise = closing_prices > opening_prices
color = np.array(
    [('white' if x else 'green')
     for x in rise])
# 边框色
ecolor = np.array(
    [('red' if x else 'green')
     for x in rise])

# 绘制K线图的影线
mp.bar(dates,
       highest_prices - lowest_prices,
       0.1, lowest_prices, color=ecolor,alpha=0.2)

# 绘制K线图的实体
mp.bar(dates,
       closing_prices - opening_prices,
       0.8, opening_prices,
       edgecolor=ecolor, color=color,alpha=0.2)



# 通过 最高价最低价收盘价取得每天的趋势点
trend_points = (
    highest_prices + closing_prices +
    lowest_prices) / 3

# 绘制趋势点
mp.scatter(dates, trend_points,
           color='dodgerblue', alpha=0.8,
           zorder=4)
# 通过线性拟合,获取一条与趋势点匹配的拟合直线
days = dates.astype('M8[D]').astype('int32')
a = np.column_stack((days, np.ones(days.size)))
# 求取拟合结果
x = np.linalg.lstsq(a, trend_points)[0]
# 获取趋势线  y=kx+b
trend_line = days * x[0] + x[1]
# 绘制趋势线
mp.plot(dates, trend_line,
        color='dodgerblue', linewidth=3,
        label='Trend Line')

spreads = highest_prices - lowest_prices
# 绘制顶部压力线 (trend+(highest-lowest))
resistance_points = trend_points + spreads
mp.scatter(dates, resistance_points,
           color='orangered', alpha=0.8,
           zorder=4)
a = np.column_stack((days, np.ones(days.size)))
# 求取拟合结果
x = np.linalg.lstsq(a, resistance_points)[0]
# 获取趋势线  y=kx+b
resistance_line = days * x[0] + x[1]
# 绘制趋势线
mp.plot(dates, resistance_line,
        color='orangered', linewidth=3,
        label='resistance Line')


# 绘制底部支撑线 (trend-(highest-lowest))
support_points = trend_points - spreads
mp.scatter(dates, support_points,
           color='limegreen', alpha=0.8,
           zorder=4)
a = np.column_stack((days, np.ones(days.size)))
# 求取拟合结果
x = np.linalg.lstsq(a, support_points)[0]
# 获取趋势线  y=kx+b
support_line = days * x[0] + x[1]
# 绘制趋势线
mp.plot(dates, support_line,
        color='limegreen', linewidth=3,
        label='support Line')





mp.legend()
# 自动格式化日期显示方式
mp.gcf().autofmt_xdate()
mp.tight_layout()
mp.show()
