import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.metrics import structural_similarity as ssim

# 打开两个视频文件
video_capture1 = cv2.VideoCapture('./videos/video_no_optimize.mp4')
video_capture2 = cv2.VideoCapture('./videos/video_with_optimize.mp4')

# 初始化列表来存储每一帧的PSNR和SSIM值
psnr_values = []
ssim_values = []

# 逐帧读取视频并比较
while True:
    ret1, frame1 = video_capture1.read()
    ret2, frame2 = video_capture2.read()

    if not ret1 or not ret2:
        break

    # 转换帧为灰度图像
    gray_frame1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    gray_frame2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

    # 计算PSNR
    mse = np.mean((gray_frame1 - gray_frame2) ** 2)
    if mse == 0:
        psnr = 100  # PSNR无限大（完全相同的帧）
    else:
        max_pixel = 255.0
        psnr = 20 * np.log10(max_pixel / np.sqrt(mse))

    # 计算SSIM
    ssim_value = ssim(gray_frame1, gray_frame2)
    
    psnr_values.append(psnr)
    ssim_values.append(ssim_value)

# 关闭视频文件
video_capture1.release()
video_capture2.release()

# 绘制PSNR和SSIM比较曲线
frame_numbers = range(len(psnr_values))
plt.figure(figsize=(12, 6))
# plt.plot(frame_numbers, psnr_values, label='PSNR')
plt.plot(frame_numbers, ssim_values, label='SSIM')
plt.xlabel('帧数')
plt.ylabel('值')
plt.legend()
plt.title('视频质量比较')
plt.show()
