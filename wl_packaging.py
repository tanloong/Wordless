#
# Wordless: Packaging - Packaging Script
#
# Copyright (C) 2018-2021  Ye Lei (叶磊)
#
# This source file is licensed under GNU GPLv3.
# For details, see: https://github.com/BLKSerene/Wordless/blob/master/LICENSE.txt
#
# All other rights reserved.
#

import datetime
import os
import platform
import shutil
import subprocess
import time

def print_with_elapsed_time(message):
    print(f'[{datetime.timedelta(seconds = round(time.time() - time_start))}] {message}')

# Version number
with open('src/VERSION', 'r', encoding = 'utf_8') as f:
    for line in f:
        if line.strip() and not line.startswith('#'):
            wl_ver = line.strip()

time_start = time.time()

# Package
print_with_elapsed_time('Start packaging...')

if platform.system() == 'Windows':
    return_val_packaging = subprocess.call('pyinstaller --noconfirm --clean wl_packaging.spec', shell = True)
elif platform.system() == 'Darwin':
    return_val_packaging = subprocess.call('python3 -m PyInstaller --noconfirm --clean wl_packaging.spec', shell = True)
elif platform.system() == 'Linux':
    return_val_packaging = subprocess.call('python3.8 -m PyInstaller --noconfirm --clean wl_packaging.spec', shell = True)

if return_val_packaging == 0:
    print_with_elapsed_time('Packaging done!')

    # Create folders
    if platform.system() in ['Windows', 'Linux']:
        os.makedirs('dist/Wordless/Import')
        os.makedirs('dist/Wordless/Export')
    elif platform.system() == 'Darwin':
        os.makedirs('dist/Wordless.app/Contents/Macos/Import')
        os.makedirs('dist/Wordless.app/Contents/Macos/Export')

    if platform.system() == 'Windows':
        # Compress files
        print_with_elapsed_time('Compressing files...')

        os.chdir('dist')
        if os.path.exists('Wordless_windows.zip'):
            os.remove('Wordless_windows.zip')
        # "7z.exe" and "7z.dll" should be put under "C:\Windows\System32" first
        subprocess.call(f'7z a -tzip -mx9 wordless_{wl_ver}_windows.zip Wordless/', shell = True)

        print_with_elapsed_time('Compressing done!')

        # Test
        print_with_elapsed_time(f'Start testing...')

        os.chdir('Wordless')
        return_val_test = subprocess.call(os.path.join(os.getcwd(), 'Wordless.exe'), shell = True)

        # Remove custom settings file
        if os.path.exists('wl_settings.pickle'):
            os.remove('wl_settings.pickle')
    elif platform.system() == 'Darwin':
        # See: https://github.com/pyinstaller/pyinstaller/issues/5062#issuecomment-683743556
        # * The following command does not work on OS X 10.11
        subprocess.call(f"codesign --remove-signature {os.path.join(os.getcwd(), 'dist/Wordless.app/Contents/Macos/Python')}", shell = True)

        # Compress files
        print_with_elapsed_time('Compressing files...')

        os.chdir('dist')
        if os.path.exists('Wordless_macos.zip'):
            os.remove('Wordless_macos.zip')
        subprocess.call(f'ditto -c -k --sequesterRsrc --keepParent Wordless.app/ wordless_{wl_ver}_macos.zip', shell = True)

        print_with_elapsed_time('Compressing done!')

        # Test
        print_with_elapsed_time(f'Start testing...')

        return_val_test = subprocess.call(os.path.join(os.getcwd(), 'Wordless.app/Contents/Macos/Wordless'), shell = True)

        # Remove custom settings file
        if os.path.exists('Wordless.app/Contents/Macos/wl_settings.pickle'):
            os.remove('Wordless.app/Contents/Macos/wl_settings.pickle')
    elif platform.system() == 'Linux':
        # Compress files
        print_with_elapsed_time('Compressing files...')

        os.chdir('dist')
        subprocess.call(f'tar -czvf wordless_{wl_ver}_linux.tar.gz Wordless/', shell = True)

        print_with_elapsed_time('Compressing done!')

        # Test
        print_with_elapsed_time(f'Start testing...')

        os.chdir('Wordless')
        return_val_test = subprocess.call('./Wordless', shell = True)

        # Remove custom settings file
        if os.path.exists('wl_settings.pickle'):
            os.remove('wl_settings.pickle')

    if return_val_test == 0:
        print_with_elapsed_time(f'Testing passed!')
    else:
        print_with_elapsed_time(f'Testing failed!')
else:
    print_with_elapsed_time(f'Packaging failed!')
