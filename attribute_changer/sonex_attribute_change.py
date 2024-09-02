import tkinter as tk
from tkinter import messagebox

def light_source(type):
    if type in [' ', None, 'LED']:
        return type
    elif type == 'накаливания':
        return 'Лампа накаливания'
    elif type == 'светодиодная (LED)':
        return 'Cветодиодная (LED)'
    elif type == 'галогенная':
        return 'Лампа галогенная'
    elif type == 'светодиодная':
        return 'Светодиодная'
    elif type == 'компактная люминесцентная (КЛЛ)':
        return 'Лампа люминесцентная '
    else:
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror("Error in attribute_changer/sonex_attribute_change", f"Invalid type: {type}")
        root.destroy()

def height(value_1, value_2):
    if value_1 is None and value_2 is None:
        return None
    elif value_1 is not None and value_2 is None:
        return value_1
    elif value_2 is not None and value_1 is None:
        return value_2
    elif value_1 is not None and value_2 is not None:
        return f'{value_2} - {value_1}'
    else:
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror("Error in attribute_changer/sonex_attribute_change", f"Invalid type: {value_1, value_2}")
        root.destroy()

def manufactor(brand):
    brand_words = brand.split()
    format_brand = [word[0].upper() + word[1:].lower() for word in brand_words if word]
    return ' '.join(format_brand)