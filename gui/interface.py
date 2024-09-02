from tkinter import *
from tkinter import ttk
import sys
import threading
from file_selection import (select_xlsx_file_imperiya as select_imperiya_xlsx,
                            select_xlsx_file_brand as select_brand_xlsx,
                            select_xml_file_brand as select_brand_xml,
                            select_add_file_brand as select_brand_add)

class RedirectOutput:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, string):
        self.text_widget.insert(END, string)
        self.text_widget.see(END)

    def flush(self):
        pass

def on_brand_selected(event):
    selected_brand = event.widget.get()
    return selected_brand

def write_path_to_file(filename, path):
    with open(filename, 'w') as f:
        f.write(path)

def select_imperiya_file():
    file_path = select_imperiya_xlsx()
    if file_path:
        file_name = file_path.split('/')[-1]
        imperiya_xlsx_button.config(text=f"Выбран файл: {file_name}", width=len(f"Выбран файл: {file_name}"))
        imperiya_xlsx_button.place(x=60, y=100)
        write_path_to_file('../additional/imperiya_path.txt', file_path)
    return file_path

def select_brand_xlsx_file():
    file_path = select_brand_xlsx()
    if file_path:
        file_name = file_path.split('/')[-1]
        brand_xlsx_button.config(text=f"Выбран файл: {file_name}", width=len(f"Выбран файл: {file_name}"))
        brand_xlsx_button.place(x=480, y=135)
        write_path_to_file('../additional/brand_xlsx_path.txt', file_path)
    return file_path

def select_brand_xml_file():
    file_path = select_brand_xml()
    if file_path:
        file_name = file_path.split('/')[-1]
        brand_xml_button.config(text=f"Выбран файл: {file_name}", width=len(f"Выбран файл: {file_name}"))
        brand_xml_button.place(x=480, y=170)
        write_path_to_file('../additional/brand_xml_path.txt', file_path)
    return file_path

def select_brand_add_file():
    file_path = select_brand_add()
    if file_path:
        file_name = file_path.split('/')[-1]
        brand_add_button.config(text=f"Выбран файл: {file_name}", width=len(f"Выбран файл: {file_name}"))
        brand_add_button.place(x=480, y=205)
        write_path_to_file('../additional/brand_add_path.txt', file_path)
    return file_path

def main_start(selected_brand):
    if selected_brand == 'Kink Light':
        from main.main_kink_light import main_kink_light
        main_kink_light()
    elif selected_brand == 'Sonex':
        from main.main_sonex import main_sonex
        main_sonex()

def open_output_window():
    output_window = Toplevel()
    output_window.title("Output")
    output_window.geometry('600x400')
    output_window.attributes('-topmost', True)

    text_widget = Text(output_window, wrap='word')
    text_widget.pack(expand=True, fill='both')

    sys.stdout = RedirectOutput(text_widget)
    sys.stderr = RedirectOutput(text_widget)

    return output_window

def start_main_thread(selected_brand):
    threading.Thread(target=main_start, args=(selected_brand,)).start()

def interface():
    global imperiya_xlsx_button, brand_xlsx_button, brand_xml_button, brand_add_button

    paths = [
        '../additional/imperiya_path.txt',
        '../additional/brand_xlsx_path.txt',
        '../additional/brand_xml_path.txt',
        '../additional/brand_add_path.txt'
    ]
    for path in paths:
        open(path, 'w').close()

    window = Tk()
    window.title('Заливка на сайт')

    window.geometry('800x350')

    window.update_idletasks()
    x = (window.winfo_screenwidth() // 2) - (window.winfo_width() // 2)
    y = (window.winfo_screenheight() // 2) - (window.winfo_height() // 2)
    window.geometry(f'+{x}+{y}')

    imperiya = Label(window, text='Империя люстр', font=("Helvetica", 20))
    imperiya.place(x=100, y=50)

    brand = Label(window, text='Бренд', font=("Helvetica", 20))
    brand.place(x=550, y=50)

    brands = ['Kink Light', 'Sonex']
    selected_brand = StringVar()
    brand_combobox = ttk.Combobox(window, textvariable=selected_brand, values=brands, width=20)
    brand_combobox.place(x=525, y=100)

    brand_combobox.bind("<<ComboboxSelected>>", on_brand_selected)

    imperiya_xlsx_button = Button(window, text='Выбрать xlsx файл', command=select_imperiya_file)
    imperiya_xlsx_button.place(x=125, y=100)

    brand_xlsx_button = Button(window, text='Выбрать xlsx файл', command=select_brand_xlsx_file)
    brand_xlsx_button.place(x=520, y=135)

    brand_xml_button = Button(window, text='Выбрать xml файл', command=select_brand_xml_file)
    brand_xml_button.place(x=520, y=170)

    brand_add_button = Button(window, text='Выбрать доп файл', command=select_brand_add_file)
    brand_add_button.place(x=520, y=205)

    main_button = Button(window, text='Выполнить', command=lambda: [open_output_window(), start_main_thread(selected_brand.get())], width=35)
    main_button.place(x=270, y=275)

    window.mainloop()

if __name__ == "__main__":
    interface()