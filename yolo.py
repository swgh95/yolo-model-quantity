import os
import time
from datetime import datetime
start_time = time.perf_counter()
path = "./"  # 当前文件夹
txt_count = 0
img_count = 0
line_count = 0
total_txt_count = 0
file_names = os.listdir()
for filename in os.listdir(path):
    if filename.endswith('.txt') and filename != "classes.txt":
        # 判断文件名是否和图片名相同
        img_filename = filename.replace(".txt", ".jpg")  # 默认图片文件名为txt文件名加上.jpg
        if os.path.exists(img_filename):
            txt_count += 1
            with open(filename) as f:
                line_count += sum(1 for line in f)
        total_txt_count += 1
    elif filename.endswith('.jpg') or filename.endswith('.png'):
        img_count += 1

difference = img_count - txt_count
txt_difference = total_txt_count - txt_count
end_time = time.perf_counter()
run_time = end_time - start_time
# 计算并输出程序运行时间
print('---------------------------------------------------------------------------')
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print("             时间戳:", current_time)
print("---------------------------------------------------------------------------")
print(' 注意！只有当txt文件名与图片名称一一对应上时，才会被计入框数统计')
print(" classes.txt作为标签文件在统计结果中会被排除，不对应的txt也会排除")
print("---------------------------------------------------------------------------")
print('')
print("             总框数: %s" % line_count)
print('')
print("             计算用时: %.4f 秒" % run_time)
print('')
print("             计入统计的txt文件数量: %s" % txt_count)
print('')
print("             当前文件夹图片文件总数量: %s" % img_count)
print('')
print("             除classes.txt文件外其他所有txt文件总数量: %s" % total_txt_count)
print('')
print('---------------------------------------------------------------------------')
print('')
print("             图片总数与被统计的txt文件的差额: %s" % difference)
print('')
print("             除classes.txt文件外总txt文件数量与被统计的txt的差额: %s" % txt_difference)
print('')
print('---------------------------------------------------------------------------')
print(' 注释：如果第一个差额不为0，代表有图片未标注或多余；需要检查')
print('       如果第二个差额不为0，代表有多余的txt；需要检查')
# 遍历文件名
found = False
for file_name in file_names:
    # 判断是否是图片文件
    if file_name.endswith('.jpg') or file_name.endswith('.png'):
        # 判断是否有对应重复名称的 txt 文件
        if file_name[:-4] + '.txt' not in file_names:
            if not found:
                found = True
                print("---------------------------------------------------------------------------")
                print('')
                print(" 哎呀！检测到上面差额不为零了，已显示此文件你要不检查一下？")
                print('')
                print(" 文件列表：")
                # 输出图片文件名
            print("           ", file_name)
            print('')
for file_name in file_names:
    # 判断是否是txt文件
    if file_name == 'classes.txt':
        continue
    if file_name.endswith('.txt'):
        # 判断是否有对应重复名称的图片文件
        if file_name[:-4] + '.jpg' not in file_names and file_name[:-4] + '.png' not in file_names:
            if not found:
                found = True
            print("           ", file_name)
            print('')
print('---------------------------------------------------------------------------')
print(' 设计：by-sw 仅供内部使用，做完了勿把此脚本一起压缩上传！')
print('---------------------------------------------------------------------------')
print('')
print('')
input('       -本次计算完成请自行记录文件统计的结果，现在按回车即可退出-')

# 时间：2023-01-15  (•‿•)
# 脚本设计：MBH-旺仔
# 公司地址：盐城大数据产业园
# 版权申明：一个破脚本申明个几把
