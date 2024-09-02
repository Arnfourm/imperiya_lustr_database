#прочитать файл кристаллюкса
def crystallux_reader():
    products = []

    for i, cell in enumerate(worksheet['U'][2:], start=3):
        sale = None

        if cell.value == 'Снято с производства':
            sale = True

        product = {
            # Основная информация
            'model': worksheet[f'D{i}'].value,
            'price': None,
            'type': worksheet[f'V{i}'].value,
            'family': worksheet[f'C{i}'].value,
            'manufactor': worksheet[f'S{i}'].value,
            'code': worksheet[f'B{i}'].value,

            # характеристики
            'Материал': worksheet[f'AQ{i}'].value,
            'Цвет покрытия': worksheet[f'AS{i}'].value,
            'Материал абажур/плафон': worksheet[f'AT{i}'].value,
            'Цвет абажур/плафон': worksheet[f'AU{i}'].value,
            'Материал подвески': worksheet[f'AV{i}'].value,
            'Цвет подвески': worksheet[f'AW{i}'].value,
            'Высота': worksheet[f'Y{i}'].value,
            'Длина': worksheet[f'X{i}'].value,
            'Ширина': worksheet[f'AA{i}'].value,
            'Диаметр': worksheet[f'Z{i}'].value,
            'Цоколь': worksheet[f'AC{i}'].value,
            'Кол-во ламп': worksheet[f'AD{i}'].value,
            'Мощность': worksheet[f'AE{i}'].value,
            'Защита': worksheet[f'AL{i}'].value,
            'Страна': worksheet[f'T{i}'].value,
            'Стиль': worksheet[f'W{i}'].value,
            'Описание': worksheet[f'AY{i}'].value
        }

        if sale == True:
            product['sale'] = 'Yes'
        else:
            product['sale'] = 'No'

        products.append(product)

    for product in products:
        model = product['model']
        for j, cell in enumerate(worksheet_price['B'][7:], start=8):
            if cell.value == model:
                product['price'] = worksheet_price[f'D{j}'].value
                break

    return products