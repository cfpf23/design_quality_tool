from src.image_analyzer import dataframe_generation, save_file, save_and_append, save_data



def start_audit(path_to_images, destination_to_report, templates_root, path_old_file=True):

    template_plus_standard_2021 = f"{templates_root}/TEMPLATE_A Plus_standard_2021.png".replace("\\", "/")
    template_premium_page_desktop_2021 = f"{templates_root}/TEMPLATE_A Premiumpage_2021.png".replace("\\", "/")
    template_premium_page_mobile_2021 = f"{templates_root}/TEMPLATE_A Premiumpage_2021.png".replace("\\", "/")

    templates = {
        "plus_standard": template_plus_standard_2021,
        "premium_page_desktop": template_premium_page_desktop_2021,
        "premium_page_mobile": template_premium_page_mobile_2021
    }
    df_from_folder = dataframe_generation(path_to_images)
    if path_old_file:
        save_data(df_from_folder, destination_to_report, templates)
        # save_and_append(df_from_folder, path_old_file, destination_to_report)
    else:
        # save_file(df_from_folder, destination_to_report, templates)
        return




# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     path = r'C:\Users\c.ferrao\Pathfinder23\Beata Michalik - Pliki do testu'
#     run(path, save=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
