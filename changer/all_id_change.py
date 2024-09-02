import openpyxl

workbook = openpyxl.load_workbook('../excel_tables/data_base_update.xlsx')
worksheet_products = workbook['Products']
worksheet_additionalImages = workbook['AdditionalImages']
worksheet_productattributes = workbook['ProductAttributes']
worksheet_SEO = workbook['ProductSEOKeywords']

def id_change():
    # Словарь для сопоставления id
    id_map = {}
    for i, cell in enumerate(worksheet_products['A'][1:], start=1):
        if i != cell.value:
            id_map[cell.value] = i

    # обновление id
    def update_ids(worksheet, col='A'):
        for row in range(2, worksheet.max_row + 1):
            cell_value = worksheet[f'{col}{row}'].value
            if cell_value in id_map:
                worksheet[f'{col}{row}'].value = id_map[cell_value]

    update_ids(worksheet_products)
    update_ids(worksheet_additionalImages)
    update_ids(worksheet_productattributes)
    update_ids(worksheet_SEO)
    workbook.save('../excel_tables/data_base_update.xlsx')