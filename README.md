# 介绍
本代码为[instant-ngp](https://github.com/NVlabs/instant-ngp)的自编gui界面

## 已实现的功能

1. 通过视频文件路径实现三维重建
2. 自定义视频抽帧帧数
3. 使用图像梯度算法优化视频抽帧，提高重建精度
4. 分级gui，首界面为`已有图片和位姿`和`从视频开始`，点击后跳转到不同的界面

## 待实现的功能

1. 添加`生成mesh文件`选项

## instant-ngp功能

1. [如何保存重建视频](https://www.youtube.com/watch?v=3TWxO1PftMc)

# 使用

1. 如果你使用RTX30系或RTX40系显卡，在[此处](https://github.com/NVlabs/instant-ngp/releases/download/continuous/Instant-NGP-for-RTX-3000-and-4000.zip)下载instant-ngp的release版本代码。如果你的下载速度较慢，也可以使用我分享的[百度云](https://pan.baidu.com/s/1XWwEZgd8lK6CahG1-_XoOA?pwd=dnid)链接进行下载(提取码：dnid)
2. 将本库克隆到`Instant-NGP-for-RTX-3000-and-4000\`下（与`instant-ngp.exe`同级）<br>![示例](/image/Snipaste.jpg "文件示例")
3. 安装`gui.py`必要的包后运行它，你也可以直接运行`gui.exe`，即可实现视频的三维重建

