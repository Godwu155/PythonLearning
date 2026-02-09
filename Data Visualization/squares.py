import matplotlib.pyplot as plt

value = [1,2,3,4,5]
squares = [1, 4, 9, 16, 25]

fig, ax = plt.subplots()    #初始化图表
plt.style.use('ggplot')

ax.plot(value,squares, linewidth = 3)
ax.set_title('Square Numbers', fontsize = 24)   #表头
ax.set_xlabel("Value", fontsize = 14)
ax.set_ylabel("Square of Value", fontsize = 14) #坐标轴
plt.title("New Square Numbers", fontsize = 18)

ax.tick_params(labelsize = 14)  #刻度


plt.savefig('NewSquareNumber.png')
plt.show()