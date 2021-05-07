from src import run
import traceback

#
# try:
#     run()
# except Exception as e:
#     print(f"Error - {e}")

try:
    if __name__ == '__main__':
        print("Running design_tool")
        run()
except Exception as e:
    with open('debug.txt', 'w') as debug_file:
        debug_file.write(str(e))
        debug_file.write(traceback.format_exc())