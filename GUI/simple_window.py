from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from src.starter import run
from src.image_analyzer import file_reader



# class MainWindow:
first = 'project folder'
second = 'previous report'



def get_path_dir():
    path = filedialog.askdirectory()
    dir_origin_1.configure(text=path)
    dir_origin_1.delete(0, 'end')
    return dir_origin_1.insert(0,path)


def get_path_report():
    path = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes = ([("CSV Files","*.csv"),('XLS Files','*.xls'), ('Excel Files','*.xlsx')]))
    file_origin_2.configure(text=path)
    file_origin_2.delete(0, 'end')
    return file_origin_2.insert(0,path)


def get_destination():
    destination = filedialog.askdirectory()
    dir_destination.configure(text=destination)
    dir_destination.delete(0, 'end')
    return dir_destination.insert(0,destination)


def analyze_files():
    old_report_path = file_origin_2.get()
    if old_report_path == '':
        pass
    else:
        df = file_reader(old_report_path)
    path_to_images = dir_origin_1.get()
    if path_to_images == '':
        return tk.messagebox.showinfo(title='Warning', message='Please insert a folder')
    destination_to_report = dir_destination.get()
    if destination_to_report == '' and old_report_path !='':
        destination_to_report = '\\'.join(old_report_path.split('\\')[:-1])
    elif destination_to_report == '' and old_report_path =='':
        return tk.messagebox.showinfo(title='Warning', message='Please insert a destination')


    run(path_to_images, destination_to_report, old_report_path)

    return tk.messagebox.showinfo(title='Warning', message='Check your folder!')

root = tk.Tk(className='Design Quality Tool')

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

title = tk.Label(master=root, text="Design Quality Tool")
title.config(font=("Amazon Ember", 25))
title.grid(row=1, columnspan = 3)

# word_input = tk.Label(master=root, text="Put the words separated by comma \",\": ")
# word_input.config(font=("Amazon Ember", 9))
# word_input.grid(row=2, column=0, sticky = W)
# word_input_user = tk.Entry(master=root, width=50)
# word_input_user.grid(row=2, column=1)

file_origin_label_2 = tk.Label(master=root, text=f"Choose your file from {second}: ")
file_origin_label_2.config(font=("Amazon Ember", 9))
file_origin_label_2.grid(row=3, column=0, sticky = W)
file_origin_2 = tk.Entry(master=root, width=50)
file_origin_2.grid(row=3, column=1)
file_origin_getter_2 = tk.Button(master=root, text="Choose file", command=get_path_report)
file_origin_getter_2.grid(row=3, column=2, sticky='nesw')

dir_origin_label_1 = tk.Label(master=root, text=f"Choose your folder from {first}: ")
dir_origin_label_1.config(font=("Amazon Ember", 9))
dir_origin_label_1.grid(row=5, column=0, sticky = W)
dir_origin_1 = tk.Entry(master=root, width=50)
dir_origin_1.grid(row=5, column=1)
dir_origin_getter_1 = tk.Button(master=root, text="Choose folder", command=get_path_dir)
dir_origin_getter_1.grid(row=5, column=2, sticky='nesw')

dir_destination_label = tk.Label(master=root, text="Choose the destination: ")
dir_destination_label.config(font=("Amazon Ember", 9))
dir_destination_label.grid(row=7, column=0, sticky = W)
dir_destination = tk.Entry(master=root, width=50)
dir_destination.grid(row=7, column=1)
dir_destination_getter = tk.Button(master=root, text="Choose path", command=get_destination)
dir_destination_getter.grid(row=7, column=2, sticky='nesw')

file_creator = tk.Button(master=root, text="Analyze", command=analyze_files, bg='orange')
file_creator.grid(row=9, column=1)

    # help_getter = tk.Button(master=root, text="Help", command=get_help, bg='red')
    # help_getter.grid(row=6, column=0)

tk.mainloop()
