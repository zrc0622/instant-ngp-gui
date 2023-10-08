import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.metrics import structural_similarity as ssim

# 打开两个视频文件
video_capture1 = cv2.VideoCapture('./videos/video_no_optimize.mp4')
video_capture2 = cv2.VideoCapture('./videos/video_with_optimize.mp4')

# 打开标准视频文件
standard_video_capture = cv2.VideoCapture('./videos/standard_video.mp4')

# 初始化列表来存储每一帧的PSNR和SSIM值
psnr_values1 = []
ssim_values1 = []
psnr_values2 = []
ssim_values2 = []

# 初始化列表来存储每一帧的梯度图像
gradient_magnitudes1 = []
gradient_magnitudes2 = []

# 抽帧并比较
while True:
    ret1, frame1 = video_capture1.read()
    ret2, frame2 = video_capture2.read()
    ret_standard, standard_frame = standard_video_capture.read()

    if not ret1 or not ret2 or not ret_standard:
        break

    # # 调整帧大小为(720, 1280)，与标准视频大小一致
    # frame1 = cv2.resize(frame1, (1280, 720))
    # frame2 = cv2.resize(frame2, (1280, 720))

    # 将帧转换为灰度图像
    gray_frame1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    gray_frame2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    gray_standard_frame = cv2.cvtColor(standard_frame, cv2.COLOR_BGR2GRAY)

    # 计算PSNR
    mse1 = np.mean((gray_frame1 - gray_standard_frame) ** 2)
    if mse1 == 0:
        psnr1 = 100  # PSNR无限大（完全相同的帧）
    else:
        max_pixel = 255.0
        psnr1 = 20 * np.log10(max_pixel / np.sqrt(mse1))

    mse2 = np.mean((gray_frame2 - gray_standard_frame) ** 2)
    if mse2 == 0:
        psnr2 = 100
    else:
        psnr2 = 20 * np.log10(max_pixel / np.sqrt(mse2))

    psnr_values1.append(psnr1)
    psnr_values2.append(psnr2)

    # 计算SSIM
    ssim_value1 = ssim(gray_frame1, gray_standard_frame)
    ssim_value2 = ssim(gray_frame2, gray_standard_frame)

    ssim_values1.append(ssim_value1)
    ssim_values2.append(ssim_value2)

    # 计算图像梯度
    gradient_x1 = cv2.Sobel(gray_frame1, cv2.CV_64F, 1, 0, ksize=3)
    gradient_y1 = cv2.Sobel(gray_frame1, cv2.CV_64F, 0, 1, ksize=3)
    
    gradient_x2 = cv2.Sobel(gray_frame2, cv2.CV_64F, 1, 0, ksize=3)
    gradient_y2 = cv2.Sobel(gray_frame2, cv2.CV_64F, 0, 1, ksize=3)

    # 计算梯度幅度
    gradient_magnitude1 = np.sqrt(gradient_x1**2 + gradient_y1**2)
    gradient_magnitude2 = np.sqrt(gradient_x2**2 + gradient_y2**2)

    gradient_magnitudes1.append(gradient_magnitude1)
    gradient_magnitudes2.append(gradient_magnitude2)

# 关闭视频文件
video_capture1.release()
video_capture2.release()
standard_video_capture.release()

# 绘制PSNR和SSIM比较曲线
frame_numbers = range(len(psnr_values1))
plt.figure(figsize=(12, 6))
plt.plot(frame_numbers, psnr_values1, label='no optimize')
plt.plot(frame_numbers, psnr_values2, label='optimize')
plt.xlabel('frame')
plt.ylabel('PSNR')
plt.legend()
plt.title('PSNR curve')
plt.savefig('./picture/psnr_comparison.png')

plt.figure(figsize=(12, 6))
plt.plot(frame_numbers, ssim_values1, label='no optimize')
plt.plot(frame_numbers, ssim_values2, label='optimize')
plt.xlabel('frame')
plt.ylabel('SSIM')
plt.legend()
plt.title('SSIM curve')
plt.savefig('./picture/ssim_comparison.png')

# 绘制和保存梯度图像
frame_numbers = range(len(gradient_magnitudes1))
mean_gradient_magnitude1 = np.mean(gradient_magnitudes1, axis=(1, 2))
mean_gradient_magnitude2 = np.mean(gradient_magnitudes2, axis=(1, 2))
plt.figure(figsize=(12, 6))
plt.plot(frame_numbers, mean_gradient_magnitude1, label='no optimize')
plt.plot(frame_numbers, mean_gradient_magnitude2, label='optimize')
plt.xlabel('frame')
plt.ylabel('gradient')
plt.legend()
plt.title('gradient curve')

# 保存梯度幅度曲线为图像文件（例如PNG）
plt.savefig('./picture/gradient_comparison.png')