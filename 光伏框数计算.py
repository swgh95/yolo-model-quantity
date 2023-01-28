import os
import glob
import pyperclip
import tkinter as tk

import sys
# 使用folder_path来访问文件夹
if len(sys.argv) < 2:
    folder_path = input("请输入文件夹路径: ")
else:
    folder_path = sys.argv[1]


# 创建窗口
root = tk.Tk()
root.title("My GUI")



# 设置总行数为 0
total_line_count = 0

# 遍历文件夹内所有文件想·
for file_path in glob.glob(os.path.join(folder_path, '*.txt')):
    # 如果文件名是 classes.txt，则跳过
    if os.path.basename(file_path) == "classes.txt":
        continue
    # 判断文件名是否和图片文件名相同
    img_file_path = os.path.splitext(file_path)[0] + ".jpg"
    if not os.path.exists(img_file_path):
        continue
    # 读取文件内容
    with open(file_path, 'r') as f:
        lines = f.readlines()
    # 统计行数
    line_count = len(lines)
    # 累加到总行数
    total_line_count += line_count

# 输出总行数
print('---------------------------------------------------------------------------')
print("                      总框数: ", total_line_count)
print('---------------------------------------------------------------------------')
input('                    --感谢使用回车后退出--')


