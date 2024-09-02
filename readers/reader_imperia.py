import openpyxl
try:
    with open('../additional/imperiya_path.txt', 'r') as file:
        excel_path = file.read().strip()
        if not excel_path:
            raise ValueError('Необходимо указать файл базы данных Империи Люстр')

    workbook = openpyxl.load_workbook(excel_path)

    worksheet = workbook['Products']
    worksheet_attributes = workbook['ProductAttributes']
    worksheet_imgs = workbook['AdditionalImages']

except ValueError as ve:
    print(f'Ошибка: {ve}')


#Прочитать бд Империи люстр
def imperia_brand_reader(brand_name):
    products = []

    for i, cell in enumerate(worksheet['M'][1:], start=2):
        if cell.value == brand_name:
            product = {
                #Основная информация
                'id': worksheet[f'A{i}'].value,
                'name': worksheet[f'B{i}'].value,
                'categories': worksheet[f'C{i}'].value,
                'model': worksheet[f'L{i}'].value,
                'manufactor': worksheet[f'M{i}'].value,
                'price': worksheet[f'P{i}'].value,
                'meta_title': worksheet[f'AD{i}'].value,
                'meta_description': worksheet[f'AE{i}'].value,
                'meta_keywords': worksheet[f'AF{i}'].value,
                'tags': worksheet[f'AK{i}'].value,
                'description': worksheet[f'AC{i}'].value,
                'sort_order': worksheet[f'AL{i}'].value,

                #Картинки
                'main_img': worksheet[f'N{i}'].value,
                'additional_img':[],

                #Характеристики
                'attributes': []
            }
            products.append(product)

    product_dict = {product['id']: product for product in products}

    #Добавить характеристики
    for j, cell in enumerate(worksheet_attributes['A'][1:], start=2):
        if cell.value in product_dict:
            product_attributes = {
                'attribute_group': worksheet_attributes[f'B{j}'].value,
                'attribute': worksheet_attributes[f'C{j}'].value,
                'value': worksheet_attributes[f'D{j}'].value
            }
            product_dict[cell.value]['attributes'].append(product_attributes)

    #Добавить дополнительные изображения
    for k, cell in enumerate(worksheet_imgs['A'][1:], start=2):
        if cell.value in product_dict:
            additional_image = worksheet_imgs[f'B{k}'].value
            product_dict[cell.value]['additional_img'].append(additional_image)

    return products

'''
tk_lighting_products = imperia_brand_reader('TK Lighting')
eurosvet_products = imperia_brand_reader('Eurosvet')
bogates_products = imperia_brand_reader('Bogate\'s')
crystal_lux_products = imperia_brand_reader('Crystal lux')
lightstar_products = imperia_brand_reader('Lightstar')
maytoni_products = imperia_brand_reader('Maytoni')
omnilux_products = imperia_brand_reader('Omnilux')
odeon_light_products = imperia_brand_reader('Odeon Light')
lumion_products = imperia_brand_reader('Lumion')
leset_products = imperia_brand_reader('Leset')
modelux_products = imperia_brand_reader('MODELUX')
zortes_products = imperia_brand_reader('Zortes')
freya_products = imperia_brand_reader('Freya')
led4u_products = imperia_brand_reader('LED4U')'''