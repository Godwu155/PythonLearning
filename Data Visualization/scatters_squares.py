import matplotlib.pyplot as plt

plt.style.use('ggplot')
# x_values = [1, 2, 3, 4, 5, 6]
# y_values = [1, 4, 9, 16, 25, 36]
x_values = range(1,1001)
y_values = [x*x for x in x_values]



fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=5, c=y_values,cmap=plt.cm.Blues ,label='Square Numbers')

ax.set_title('Square Numbers', fontsize=14)
ax.axis([0,1100,0,1_100_000])
plt.show()
