# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from src.image_analyzer import dataframe_generation, save_file, save_and_append


def start_audit(path_to_images, destination_to_report, path_old_file):
    df_from_folder = dataframe_generation(path_to_images)
    if path_old_file:
        save_and_append(df_from_folder, path_old_file, destination_to_report)
    else:
        save_file(df_from_folder, destination_to_report)




# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     path = r'C:\Users\c.ferrao\Pathfinder23\Beata Michalik - Pliki do testu'
#     run(path, save=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
