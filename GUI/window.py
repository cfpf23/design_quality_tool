import pandas as pd
from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

first = 'image folder'
second = 'IC report'

def get_folder_images():
    destination = filedialog.askdirectory()
    dir_destination.configure(text=destination)
    dir_destination.delete(0, 'end')
    return dir_destination.insert(0,destination)

# def get_path_ic():
#     path = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes = ([("CSV Files","*.csv"),('xls files','*.xls')]))
#     file_origin_2.configure(text=path)
#     file_origin_2.delete(0, 'end')
#     return file_origin_2.insert(0,path)

def get_destination():
    destination = filedialog.askdirectory()
    dir_destination.configure(text=destination)
    dir_destination.delete(0, 'end')
    return dir_destination.insert(0,destination)

def analyzer():
    words_search = word_input_user.get()
    if words_search == '':
        return tk.messagebox.showinfo(title='Warning', message='Please insert a list of words!')
    # words_search = 'Wetterstation, Wettervorhersage, Funkwetterstation, Thermometer, Hygrometer, Multifunktions-Holzfeuchte-Messgerät, Holzfeuchte-Messgerät, Holzfeuchte Messgerät'
    words_list = [x.strip().lower() for x in words_search.split(',')]
    ic_df_path = file_origin_2.get()
    # ic_df_path = r'C:\Users\ferraoc\Documents\PS\New_Process_rule_merge\report1.xls'

    month_sample_path = file_origin_1.get()
    destination = dir_destination.get()
    if ic_df_path == '' and month_sample_path == '':
        return tk.messagebox.showinfo(title='Warning', message='Please select at least one file!')
    if destination == '':
        return tk.messagebox.showinfo(title='Warning', message='Please select a destination folder!')
    # month_sample_path = r'C:\Users\ferraoc\Downloads\decoder-export-results-f89544c0-3a0a-4643-9752-04c07e6daa6d.csv'
    ic_df = ''
    month_sample_df = ''
    ic_list = []
    sample3m_list = []
    if ic_df_path == '':
        pass
    else:
        ic_df = pd.read_csv(ic_df_path, sep='\t')
        ic_df.fillna('').applymap(str)
        ic_df.iloc[:, 1] = ic_df.iloc[:, 1].str.lower()

        # print('ic_list')
    if month_sample_path == '':
        pass
    else:
        valid_sep = [',', ';']
        for s in valid_sep:
            try:
                # print(s)
                month_sample_df = pd.read_csv(month_sample_path, encoding = "utf-8", error_bad_lines=False, sep=s)
                month_sample_df.fillna('').applymap(str)
                month_sample_df.iloc[:,1] = month_sample_df.iloc[:,1].replace(['{ language_tag:de_DE, value:"', '\"'], '', regex=True).str.lower()
                # print(month_sample_df)
                break
            except:
                continue
        # print('sample3m_list')

    n_word_list = []

    for word in words_list:
        n=0
        if isinstance(month_sample_df, pd.DataFrame):
            for row in month_sample_df.iloc[:, 1]:
                if any([x in str(row).lower() for x in [word]]):
                    n=n+1
        #             ic_list.append({'ic_sample_count':n})
                else:
                    pass
            sample3m_list.append({'sample3m_sample_count':n})
            # print(word, n)
        n=0
        if isinstance(ic_df, pd.DataFrame):
            for row in ic_df.iloc[:, 1]:
                if any([x in str(row).lower() for x in [word]]):
                    n=n+1
        #             sample3m_list.append({'sample3m_sample_count':n})
                else:
                    pass
            ic_list.append({'ic_sample_count':n})
            # print(word, n)
        n_word_list.append({'word':word})

    df_ic_list = pd.DataFrame(ic_list)
    df_sample3m_list = pd.DataFrame(sample3m_list)
    df_n_word_list = pd.DataFrame(n_word_list)
    for df in [df_sample3m_list, df_ic_list]:
        if not df.empty:
            df_n_word_list = pd.concat([df_n_word_list, df], axis=1, sort=False)
    df_n_word_list = df_n_word_list.set_index('word', drop=True)
    # print(df_n_word_list)
    return df_n_word_list.to_excel(rf'{destination}\data-treated.xlsx'), tk.messagebox.showinfo(title='Warning', message='Check your folder!')

root = tk.Tk(className='POV merger')

root.resizable(width=True, height=True)

# def resource_path(relative_path):
#     """ Get absolute path to resource, works for dev and for PyInstaller """
#     try:
#         # PyInstaller creates a temp folder and stores path in _MEIPASS
#         base_path = sys._MEIPASS
#     except Exception:
#         base_path = os.path.abspath(".")
#
#     return os.path.join(base_path, relative_path)

#resource_path('C:\\Users\\ferraoc\\PycharmProjects\\untitled\\venv\\Peccy.ico')

title = tk.Label(master=root, text="POV merger")
title.config(font=("Amazon Ember", 25))
title.grid(row=1, columnspan = 3)

word_input = tk.Label(master=root, text="Put the words separated by comma \",\": ")
word_input.config(font=("Amazon Ember", 9))
word_input.grid(row=2, column=0, sticky = W)
word_input_user = tk.Entry(master=root, width=50)
word_input_user.grid(row=2, column=1)

file_origin_label_1 = tk.Label(master=root, text=f"Choose your path from {first}: ")
file_origin_label_1.config(font=("Amazon Ember", 9))
file_origin_label_1.grid(row=3, column=0, sticky = W)
file_origin_1 = tk.Entry(master=root, width=50)
file_origin_1.grid(row=3, column=1)
file_origin_getter_1 = tk.Button(master=root, text="Choose file", command=get_folder_images)
file_origin_getter_1.grid(row=3, column=2, sticky='nesw')

# file_origin_label_2 = tk.Label(master=root, text=f"Choose your file from {second}: ")
# file_origin_label_2.config(font=("Amazon Ember", 9))
# file_origin_label_2.grid(row=5, column=0, sticky = W)
# file_origin_2 = tk.Entry(master=root, width=50)
# file_origin_2.grid(row=5, column=1)
# file_origin_getter_2 = tk.Button(master=root, text="Choose file", command=get_path_ic)
# file_origin_getter_2.grid(row=5, column=2, sticky='nesw')

dir_destination_label = tk.Label(master=root, text="Choose the destination: ")
dir_destination_label.config(font=("Amazon Ember", 9))
dir_destination_label.grid(row=7, column=0, sticky = W)
dir_destination = tk.Entry(master=root, width=50)
dir_destination.grid(row=7, column=1)
dir_destination_getter = tk.Button(master=root, text="Choose path", command=get_destination)
dir_destination_getter.grid(row=7, column=2, sticky='nesw')

file_creator = tk.Button(master=root, text="Analyze", command=analyzer, bg='orange')
file_creator.grid(row=9, column=1)

# help_getter = tk.Button(master=root, text="Help", command=get_help, bg='red')
# help_getter.grid(row=6, column=0)

tk.mainloop()
