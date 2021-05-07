import sys
import os


# print(sys._MEIPASS())

base_path = os.path.abspath(".")

print(base_path)

print(os.path.join(base_path, 'Gray-CIE_L.icc'))