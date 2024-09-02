import tkinter as tk
from tkinter import messagebox

def light_source(type):
    if type in ['Led, с led драйвером в комплекте', 'LED', 'GU10', 'Led, с led драйвером в комплекте (3шт)', 'G9',
                ' ', None]:
        return type
    elif type == 'Накаливания':
        return 'Лампа накаливания'
    elif type == 'Галогеновая':
        return 'Лампа галогеновая'
    elif type == 'Накаливания/Led, с led лампами в комплекте':
        return 'Лампа накаливания/Led, с led лампами в комплекте'
    elif type == 'Накаливания/Led, с led драйвером в комплекте':
        return 'Лампа накаливания/Led, с led драйвером в комплекте'
    elif type == 'Накаливания/LED':
        return 'Лампа накаливания/LED'
    else:
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror("Error in attribute_changer/kink_light_attribute_change", f"Invalid type: {type}")
        root.destroy()

def room(kind):
    if kind == 'Для комнаты':
        return 'Комната'
    elif kind == 'Для гостиной':
        return 'Гостиная'
    elif kind == 'Освещение кафе и ресторанов':
        return 'Кафе и рестораны'
    elif kind == 'Для кухни':
        return 'Кухня'
    elif kind == 'Для спальни':
        return 'Спальня'
    elif kind == 'Для ванной':
        return 'Ванна'
    elif kind == 'Для детской':
        return 'Детская'
    elif kind == 'Для веранды':
        return 'Веранда'
    elif kind in ['Архитектурная подсветка', ' ', None]:
        return ' '
    else:
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror("Error in attribute_changer/kink_light_attribute_change", f"Invalid kind: {kind}")
        root.destroy()