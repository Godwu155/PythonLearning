# image_compression_compare.py
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from numpy.linalg import svd
import os

# -----------------------------
# 函数：SVD低秩压缩
# -----------------------------
def svd_compress(image_array, k):
    """
    对灰度图像矩阵进行SVD低秩近似压缩
    :param image_array: np.array，灰度图像矩阵
    :param k: int，保留奇异值数量
    :return: np.array，压缩后的图像矩阵
    """
    U, S, Vt = svd(image_array, full_matrices=False)
    S_k = np.diag(S[:k])
    U_k = U[:, :k]
    Vt_k = Vt[:k, :]
    A_k = np.dot(U_k, np.dot(S_k, Vt_k))
    return np.clip(A_k, 0, 255)

# -----------------------------
# 主程序
# -----------------------------
def main():
    # 读取图像，转灰度
    img_path = "test.jpg"  # 替换为你本地图像路径
    img = Image.open(img_path).convert("L")
    img_array = np.array(img, dtype=np.float64)

    # 设置SVD保留的奇异值数量
    svd_ranks = [10, 50, 100]
    compressed_svd = [svd_compress(img_array, k) for k in svd_ranks]

    # 保存JPEG压缩
    jpeg_out = "jpeg_compressed.jpg"
    img.save(jpeg_out, "JPEG", quality=30)
    compressed_jpeg = np.array(Image.open(jpeg_out), dtype=np.float64)

    # -----------------------------
    # 绘制对比图
    # -----------------------------
    total = 2 + len(svd_ranks)  # 原图 + SVD若干 + JPEG
    fig, axes = plt.subplots(1, total, figsize=(4*total, 5))

    # 原图
    axes[0].imshow(img_array, cmap='gray')
    axes[0].set_title("Original")
    axes[0].axis('off')

    # SVD压缩
    for i, k in enumerate(svd_ranks):
        axes[i+1].imshow(compressed_svd[i], cmap='gray')
        axes[i+1].set_title(f"SVD rank={k}")
        axes[i+1].axis('off')

    # JPEG压缩
    axes[-1].imshow(compressed_jpeg, cmap='gray')
    axes[-1].set_title("JPEG quality=30")
    axes[-1].axis('off')

    plt.tight_layout()
    plt.show()

    # -----------------------------
    # 文件大小对比
    # -----------------------------
    original_size = os.path.getsize(img_path) / 1024
    jpeg_size = os.path.getsize(jpeg_out) / 1024
    print(f"原图大小: {original_size:.2f} KB")
    print(f"JPEG压缩后大小: {jpeg_size:.2f} KB")
    for i in enumerate(svd_ranks):
        print(f"")

if __name__ == "__main__":
    main()
