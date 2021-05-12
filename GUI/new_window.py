from tkinter import *
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from src.starter import start_audit
from src.image_analyzer import file_reader


class SimpleWindow():


    def __init__(self, options):

        self.root = tk.Tk()
        self.root.title("Design Quality Tool")
        self.root.resizable(width=True, height=True)
        self.title = tk.Label(master=self.root, text="Design Quality Tool")
        self.title.config(font=("Amazon Ember", 25))
        self.title.grid(row=1, columnspan=3)
        self.templates_root = options['DIR_PATH'] + 'assets'

        # variables

        # self.file_origin_label_2 = tk.Label(master=self.root, text=f"Choose your file from previous report: ")
        # self.file_origin_label_2.config(font=("Amazon Ember", 9))
        # self.file_origin_label_2.grid(row=3, column=0, sticky=W)
        # self.file_origin_2 = tk.Entry(master=self.root, width=50)
        # self.file_origin_2.grid(row=3, column=1)
        # self.file_origin_getter_2 = tk.Button(master=self.root, text="Choose file", command=self.get_path_report)
        # self.file_origin_getter_2.grid(row=3, column=2, sticky='nesw')

        self.dir_origin_label_1 = tk.Label(master=self.root, text=f"Choose your folder from project: ")
        self.dir_origin_label_1.config(font=("Amazon Ember", 9))
        self.dir_origin_label_1.grid(row=5, column=0, sticky=W)
        self.dir_origin_1 = tk.Entry(master=self.root, width=50)
        self.dir_origin_1.grid(row=5, column=1)
        self.dir_origin_getter_1 = tk.Button(master=self.root, text="Choose folder", command=self.get_path_dir)
        self.dir_origin_getter_1.grid(row=5, column=2, sticky='nesw')

        self.dir_destination_label = tk.Label(master=self.root, text="Choose the destination: ")
        self.dir_destination_label.config(font=("Amazon Ember", 9))
        self.dir_destination_label.grid(row=7, column=0, sticky=W)
        self.dir_destination = tk.Entry(master=self.root, width=50)
        self.dir_destination.grid(row=7, column=1)
        self.dir_destination_getter = tk.Button(master=self.root, text="Choose path", command=self.get_destination)
        self.dir_destination_getter.grid(row=7, column=2, sticky='nesw')

        self.file_creator = tk.Button(master=self.root, text="Analyze", command=self.analyze_files, bg='orange')
        self.file_creator.grid(row=9, column=1)

        self.file_creator = None

        self.root.mainloop()


    def get_path_dir(self):

        self.path = filedialog.askdirectory()
        self.dir_origin_1.configure(text=self.path)
        self.dir_origin_1.delete(0, 'end')
        return self.dir_origin_1.insert(0,self.path)


    def get_path_report(self):
        path = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes = ([('Excel Files','*.xlsx')]))
        self.file_origin_2.configure(text=path)
        self.file_origin_2.delete(0, 'end')
        return self.file_origin_2.insert(0,path)


    def get_destination(self):
        destination = filedialog.askdirectory()
        self.dir_destination.configure(text=destination)
        self.dir_destination.delete(0, 'end')
        return self.dir_destination.insert(0,destination)

    def analyze_files(self):
        path_to_images = self.dir_origin_1.get()
        if path_to_images == '':
            return tk.messagebox.showinfo(title='Warning', message='Please insert a folder')
        destination_to_report = self.dir_destination.get()
        if destination_to_report == '':
            return tk.messagebox.showinfo(title='Warning', message='Please insert a destination')

        old_report_path = True
        templates_root = self.templates_root

        start_audit(path_to_images, destination_to_report, templates_root, old_report_path)

        return tk.messagebox.showinfo(title='Warning', message='Check your folder!')



    # def analyze_files(self):
    #     """
    #     retired function - do not delete
    #     """
    #     old_report_path = self.file_origin_2.get()
    #     if old_report_path == '':
    #         pass
    #     else:
    #         df = file_reader(old_report_path)
    #     path_to_images = self.dir_origin_1.get()
    #     if path_to_images == '':
    #         return tk.messagebox.showinfo(title='Warning', message='Please insert a folder')
    #     destination_to_report = self.dir_destination.get()
    #     if destination_to_report == '' and old_report_path !='':
    #         destination_to_report = '\\'.join(old_report_path.split('\\')[:-1])
    #     elif destination_to_report == '' and old_report_path =='':
    #         return tk.messagebox.showinfo(title='Warning', message='Please insert a destination')
    #
    #     start_audit(path_to_images, destination_to_report, old_report_path)
    #
    #     return tk.messagebox.showinfo(title='Warning', message='Check your folder!')

# if __name__ == "__main__":
#     SimpleWindow().root.mainloop()

    # help_getter = tk.Button(master=root, text="Help", command=get_help, bg='red')
    # help_getter.grid(row=6, column=0)


