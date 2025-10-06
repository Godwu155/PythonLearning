import numpy
import math

# from sklearn.externals.array_api_compat.cupy import arange

# a = numpy.arange(0, 20, 2)
# b = a + 1

b = numpy.arange(12).reshape(3, 4)
print(b)

c = numpy.random.random((3, 4))


def gradient_descent(start_x, lr, iter, dy):
    x = start_x  # 起点
    for i in range(iter):
        g = dy(x)
        print("%2d x=%f y(%f)=%f dy(x)=%f" % (i, x, x, dy(x), g))
        x = x - lr * g
        if abs(g) < 1e-6:
            break

    return x


gradient_descent(5, 0.05, 100)


