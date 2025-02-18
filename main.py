import os
import sys
import time
import random
import shutil as st
import tkinter as tk
from tkinter import filedialog


# 跨平台清屏
def clear_screen():
    # Windows系统
    if os.name == 'nt':
        os.system('cls')
    # Unix/Linux/MacOS系统
    else:
        os.system('clear')

clear_screen()

print('Mode options:')
print('1 Keep original files')
print('2 Delete original files')


# mode = int(input('Enter the mode: '))
mode = 1

clear_screen()

# time_start = time.time()


root = tk.Tk()
root.withdraw()

current_dir = filedialog.askdirectory(title="Choose directory")  # 弹出对话框并获取用户选择的文件夹路径
if not current_dir:
    print("No directory selected")
    sys.exit(1)

jpg_dir = os.path.join(current_dir, 'JPG')
nef_dir = os.path.join(current_dir, 'NEF')
os.makedirs(jpg_dir, exist_ok=True)
os.makedirs(nef_dir, exist_ok=True)

# print(jpg_dir)
# print(nef_dir)
j_num = 0
n_num = 0
i_num = 0


for file in os.listdir(current_dir):
    print(file, end = ' ')
    file_path = os.path.join(current_dir, file)
    file_jpath = os.path.join(jpg_dir, file)
    file_npath = os.path.join(nef_dir, file)
    if os.path.isfile(os.path.join(current_dir, file)):
        file_name, file_ext = os.path.splitext(file)
        if os.path.exists(file_jpath) or os.path.exists(file_npath):
            print('-> Existed and ignored')
            i_num += 1
        elif file_ext == '.JPG' or file_ext == '.jpg':
            st.copy2(file_path, jpg_dir)
            j_num += 1
            print(f'-> {jpg_dir}')
            if mode == 2:
                os.remove(file)
        elif file_ext == '.NEF' or file_ext == '.nef':
            st.copy2(file_path, nef_dir)
            n_num += 1
            print(f'-> {nef_dir}')
            if mode == 2:
                os.remove(file)
        else:
            print('-> Ignored')
            i_num += 1
    else:
        print('-> Ignored')
        i_num += 1
# time_end = time.time()


print(f'JPG: {j_num} times, NEF: {n_num} times, Ignored: {i_num} times')
print(f'\n\n\nFinished')

# input('Press Enter to exit...')
