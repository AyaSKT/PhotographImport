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

for file in os.listdir(current_dir):
    print(file, end = ' ')
    file_path = os.path.join(current_dir, file)
    if os.path.isfile(os.path.join(current_dir, file)):
        file_name, file_ext = os.path.splitext(file)
        
        if file_ext == '.JPG' or file_ext == '.jpg':
            st.copy2(file_path, jpg_dir)
            print('-> JPG')
            if mode == 2:
                os.remove(file)
        elif file_ext == '.NEF' or file_ext == '.nef':
            st.copy2(file_path, nef_dir)
            print('-> NEF')
            if mode == 2:
                os.remove(file)
    else:
        print('-> Ignored')

# time_end = time.time()


# print(f'\n\n\nFinished in {time_end - time_start} seconds')
input('Press Enter to exit...')
