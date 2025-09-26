# # # Python 3.x
# import numpy as np
#
# matrix = np.array([[7, 5, 3, 4, 7, 5, 7654, 4],
#                    [2, 4, 1, 6, 7, 5, 3, 4],
#                    [5, 8, 6, 7, 7, 7654, 3, 4],
#                    [3, 4, 5, 6, 7, 5, 3, 4],
#                    [7, 5, 5433, 4, 7, 5, 3, 4],
#                    [2, 4, 1, 6, 76, 5, 3, 4],
#                    [5, 8, 8765, 7, 7, 5, 3, 4],
#                    [3, 4, 5, 6, 7, 5, 3, 4]
#                    ])
# det = np.linalg.det(matrix)
# print("Determinant of the matrix is:", round(det))


import numpy as np


def get_matrix_from_user(n):
    """
    通过用户输入构建一个n x n的方阵，并进行严格的输入验证。

    参数:
    n (int): 矩阵的阶数，即行数和列数。

    返回:
    numpy.ndarray: 经过验证的n x n的NumPy矩阵。
    """
    matrix_size = n * n
    while True:
        try:
            # 提示用户在单行输入所有矩阵元素，用空格分隔
            print(f"\n请输入一个{n}x{n}矩阵的{matrix_size}个元素，以空格分隔：")
            input_string = input(">>> ")

            # 使用map和split将字符串输入转换为整数列表
            # map(int,...) 将对每个分割后的字符串元素调用int()进行转换
            # 如果任何元素无法转换为整数，int()将抛出ValueError
            elements = list(map(int, input_string.split()))

            # 将整数列表转换为NumPy数组，并尝试重塑为n x n的矩阵
            # 如果元素数量不等于matrix_size，reshape()将抛出ValueError
            matrix = np.array(elements).reshape(n, n)

            print("\n成功接收并构建矩阵：")
            print(matrix)

            return matrix

        except ValueError as e:
            # 捕获因输入无效（非数字或数量不符）而引起的ValueError
            print(f"\n错误：输入的格式不正确或元素数量不正确。{e}")
            print("请确保输入的是数字，且总共有{matrix_size}个元素。")


def calculate_determinant(matrix):
    """
    使用NumPy的linalg.det函数计算矩阵的行列式。

    参数:
    matrix (numpy.ndarray): 一个方阵。

    返回:
    float: 矩阵的行列式值。
    """
    # np.linalg.det() 调用底层高度优化的LAPACK例程（基于LU分解）
    # 确保了计算的高效性和准确性。
    determinant_value = np.linalg.det(matrix)
    return determinant_value


def main():
    """
    主程序流程，负责获取用户输入、计算行列式并打印结果。
    """
    matrix_order = 8

    # 引导用户输入矩阵
    input_matrix = get_matrix_from_user(matrix_order)

    # 计算行列式
    determinant = calculate_determinant(input_matrix)

    # 打印最终结果
    print(f"\n您输入的{matrix_order}阶矩阵的行列式值为：{determinant}")
    print("\n程序执行完毕。")


if __name__ == "__main__":
    main()