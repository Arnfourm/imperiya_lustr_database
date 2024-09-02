#прочитать файл лайтстар
def lightstar_reader():
    products = []

    for i, cell in enumerate(worksheet['D'][3:], start=4):
        sale = None

        if cell.value == 'Sale':
            sale = True

        product = {
            # Основная информация
            'model': worksheet[f'B{i}'].value,
            'price': worksheet[f'H{i}'].value,
            'name': worksheet[f'C{i}'].value, #разделить сплитом и использовать как type, так как его нет
            'family': worksheet[f'AB{i}'].value,
            'manufactor': 'Lightstar',

            # характеристики
            'Материал': worksheet[f'AS{i}'].value,
            'Цвет покрытия': worksheet[f'AX{i}'].value,
            'Материал абажур/плафон': worksheet[f'BK{i}'].value,
            'Цвет абажур/плафон': worksheet[f'BP{i}'].value,
            'Высота': worksheet[f'U{i}'].value,
            'Длина': worksheet[f'S{i}'].value,
            'Ширина': worksheet[f'AE{i}'].value,
            'Диаметр': worksheet[f'AJ{i}'].value,
            'Тип лампы': worksheet[f'AC{i}'].value,
            'Цоколь': worksheet[f'BM{i}'].value,
            'Кол-во ламп': worksheet[f'AM{i}'].value,
            'Мощность': worksheet[f'Z{i}'].value,
            'Защита': worksheet[f'AP{i}'].value,
            'Страна': 'Италия',
            'Стиль': worksheet[f'AZ{i}'].value,
            'Помещение': worksheet[f'O{i}'].value
        }

        if sale == True:
            product['sale'] = 'Yes'
        else:
            product['sale'] = 'No'

        products.append(product)

    return products