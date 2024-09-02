import openpyxl
import tkinter as tk
from tkinter import messagebox

try:
    with open('../additional/imperiya_path.txt', 'r') as file:
        excel_path = file.read().strip()
        if not excel_path:
            raise ValueError('Необходимо указать файл базы данных Империи Люстр')

    workbook = openpyxl.load_workbook(excel_path)

    worksheet = workbook['Products']
    worksheet_attributes = workbook['ProductAttributes']
    worksheet_SEO = workbook['ProductSEOKeywords']
    worksheet_imgs = workbook['AdditionalImages']

except ValueError as ve:
    print(f'Ошибка: {ve}')

def delete_rows(id_list):
    rows_to_delete = {
        'Products': [],
        'ProductAttributes': [],
        'ProductSEOKeywords': [],
        'AdditionalImages': []
    }

    for i, cell in enumerate(worksheet['A'][1:], start=2):
        if cell.value in id_list:
            rows_to_delete['Products'].append(i)

    for i, cell in enumerate(worksheet_attributes['A'][1:], start=2):
        if cell.value in id_list:
            rows_to_delete['ProductAttributes'].append(i)

    for i, cell in enumerate(worksheet_SEO['A'][1:], start=2):
        if cell.value in id_list:
            rows_to_delete['ProductSEOKeywords'].append(i)

    for i, cell in enumerate(worksheet_imgs['A'][1:], start=2):
        if cell.value in id_list:
            rows_to_delete['AdditionalImages'].append(i)

    for sheet_name, rows in rows_to_delete.items():
        sheet = workbook[sheet_name]
        for row in sorted(rows, reverse=True):
            sheet.delete_rows(row)

    workbook.save('../excel_tables/data_base_update.xlsx')

def delete_imgs(img_list, ftp):
    for img in img_list:
        try:
            ftp.delete(f'/im/public_html/image/{img}')
            break
        except Exception as e:
            root = tk.Tk()
            root.withdraw()
            messagebox.showerror("Error in delete/delete_imperiya", f"Invalid img_path: {img}")
            root.destroy()

    ftp.quit()