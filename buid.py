# 生成exe文件
import subprocess
import os

# 获取脚本所在的目录
script_dir = os.path.dirname(os.path.abspath(__file__))

# 使用PyInstaller打包你的代码
subprocess.run(["pyinstaller", "--onefile", "gui.py"])
