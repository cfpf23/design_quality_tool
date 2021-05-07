import shutil
import PyInstaller.__main__

import sys

sys.setrecursionlimit(5000)
# pyinstaller --onefile --paths=c:\\users\\c.ferrao\\anaconda3\\lib\\site-packages design_quality_tool.py

PyInstaller.__main__.run([
    '--name=design_quality_tool',
    # '--add-data=C:/Users/c.ferrao/Anaconda3/Lib/tkinter/ttk/',
    # '--add-data=assets/4ico.ico;.',
    # '--add-data=assets/side_img.png;.',
    # '--hidden-import=tkinter',
    '--onefile',
    '--windowed',
    'design_quality_tool.py',
])