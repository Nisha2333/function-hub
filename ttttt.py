import math
import numpy as np #导入数值计算模块
import matplotlib.pyplot as plt #导入绘图模块
import mpl_toolkits.axisartist as axisartist #导入坐标轴加工模块
fig=plt.figure(figsize=(4,2)) #新建画布
ax=axisartist.Subplot(fig,111) #使用axisartist.Subplot方法创建一个绘图区对象ax
fig.add_axes(ax) #将绘图区对象添加到画布中

ax.axis[:].set_visible(False) #隐藏原来的实线矩形

ax.axis["x"]=ax.new_floating_axis(0,0,axis_direction="bottom") #添加x轴
ax.axis["y"]=ax.new_floating_axis(1,0,axis_direction="bottom") #添加y轴

ax.axis["x"].set_axisline_style("->",size=1.0) #给x坐标轴加箭头
ax.axis["y"].set_axisline_style("->",size=1.0) #给y坐标轴加箭头
ax.annotate(s='x' ,xy=(2*math.pi,0) ,xytext=(2*math.pi,0.1)) #标注x轴
ax.annotate(s='y' ,xy=(0,1.0) ,xytext=(-0.5,1.0)) #标注y轴

plt.xlim(-6.3,6.3) #设置横坐标范围
plt.ylim(-1.1,1.1) #设置纵坐标范围
ax.set_xticks([-2*math.pi,-math.pi,0,math.pi,2*math.pi]) #设置x轴刻度
ax.set_yticks([-1,1]) #设置y轴刻度

y=[] #用来存放函数值
x=np.linspace(-2*math.pi,2*math.pi,100) #构造横坐标数据
for xi in x: #生成函数值
    y.append(math.sin(xi))#追加

plt.plot(x,y,color="blue") #描点连线
plt.show() #出图