from tkinter import filedialog

def select_xlsx_file_imperiya():
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*xlsx*")])
    return file_path

def select_xlsx_file_brand():
    file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*xlsx*")])
    return file_path

def select_xml_file_brand():
    file_path = filedialog.askopenfilename(filetypes=[("XML files", "*.xml*")])
    return file_path

def select_add_file_brand():
    file_path = filedialog.askopenfilename(filetypes=[("All files", "*.*")])
    return file_path