import os
import sys
import time
import random
import shutil as st

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
        elif file_ext == '.NEF' or file_ext == '.nef':
            st.copy2(file, 'NEF')
            print('-> NEF')
    else:
        print('-> Ignored')

print('\n\n\n Finished')
os.system('pause')
