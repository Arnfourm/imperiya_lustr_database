#прочитать файл фрея
def freya_reader():
    products = []

    for i, cell in enumerate(worksheet['B'][8:], start=9):
        if cell.value is None:
            continue
        else:
            product = {
                # Основная информация
                'model': worksheet[f'A{i}'].value,
                'old_model': worksheet[f'C{i}'].value,
                'price': worksheet[f'J{i}'].value,
                'type': worksheet[f'F{i}'].value,
                'family': worksheet[f'E{i}'].value,
                'manufactor': worksheet[f'B{i}'].value,

                # характеристики
                'Материал': worksheet[f'Q{i}'].value,
                'Цвет покрытия': worksheet[f'R{i}'].value,
                'Высота': worksheet[f'V{i}'].value,
                'Длина': worksheet[f'W{i}'].value,
                'Ширина': worksheet[f'X{i}'].value,
                'Диаметр': worksheet[f'Y{i}'].value,
                'Цоколь': worksheet[f'AC{i}'].value,
                'Кол-во ламп': worksheet[f'AD{i}'].value,
                'Мощность': worksheet[f'AF{i}'].value,
                'Гарантия': worksheet[f'AI{i}'].value,
                'Площадь': worksheet[f'AL{i}'].value,
                'Защита': worksheet[f'AQ{i}'].value,
                'Страна': worksheet[f'AH{i}'].value
            }

            products.append(product)

    return products