from src import run
import traceback
import pathlib

#
# try:
#     run()
# except Exception as e:
#     print(f"Error - {e}")

try:
    if __name__ == '__main__':
        print("Running design_tool")
        DIR_PATH = str(pathlib.Path().absolute()).replace("\\", "/") + '/'
        options = {"DIR_PATH": DIR_PATH}
        run(options)
except Exception as e:
    with open('debug.txt', 'w') as debug_file:
        debug_file.write(str(e))
        debug_file.write(traceback.format_exc())