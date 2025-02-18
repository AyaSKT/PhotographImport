import os
import sys
import time
import random
import shutil as st

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


mode = int(input('Enter the mode: '))

clear_screen()

time_start = time.time()

os.makedirs('JPG', exist_ok=True)
os.makedirs('NEF', exist_ok=True)

current_dir = os.getcwd()

for file in os.listdir(current_dir):
    print(file, end = ' ')
    if os.path.isfile(file):
        file_name, file_ext = os.path.splitext(file)
        if file_ext == '.JPG' or file_ext == '.jpg':
            st.copy2(file, 'JPG')
            print('-> JPG')
            if mode == 2:
                os.remove(file)
        elif file_ext == '.NEF' or file_ext == '.nef':
            st.copy2(file, 'NEF')
            print('-> NEF')
            if mode == 2:
                os.remove(file)
    else:
        print('-> Ignored')

time_end = time.time()


print(f'\n\n\nFinished in {time_end - time_start} seconds')
input('Press Enter to exit...')
