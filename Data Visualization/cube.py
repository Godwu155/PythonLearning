import matplotlib.pyplot as plt

x_values = range(0, 5000)
y_values = [x**3 for x in x_values]

fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values,cmap='Blues', s=10)
# ax.plot(x_values, y_values, c='r')
ax.set_title('Cubic Numbers', fontsize=14)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Cubic Number', fontsize=14)

plt.show()
