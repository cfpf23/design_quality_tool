import cx_Freeze
from cx_Freeze import Executable
import sys
# import tkinter
# import pandas
# import webbrowser
# import xlsxwriter
# import PIL
# import setuptools
# from pyinstaller_setuptools import setup
# import os
# import pandas as pd
# from PIL import Image
# from psd_tools import PSDImage
# from datetime import datetime
# import xlsxwriter
# from openpyxl import load_workbook
# import shutil, os

base = None

if sys.platform == 'Win32':
    base = 'Win32GUI'
executables = [Executable('design_quality_tool.py', base=base)]
cx_Freeze.setup(
    name = 'design_quality_tool',
    options = {'build_exe':{'packages':[
        'PIL',
        'numpy.core._dtype',
        'numpy',
        'tkinter',
        'pandas',
        'shutil',
        'os',
        'psd_tools',
        'xlsxwriter',
        'openpyxl',
        'datetime'
    ]}},
    verison = '0.1',
    description = 'design_quality_tool',
    executables = executables
)
