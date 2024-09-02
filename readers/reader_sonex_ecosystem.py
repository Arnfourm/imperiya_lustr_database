import openpyxl
from attribute_changer.sonex_attribute_change import light_source, height, manufactor

#Excel файлы
try:
    with open('../additional/brand_xlsx_path.txt', 'r') as file:
        excel_path = file.read().strip()
        if not excel_path:
            raise ValueError('Необходимо указать xlsx файл базы данных Бренда')

    workbook = openpyxl.load_workbook(excel_path)
    worksheet = workbook.active

except ValueError as ve:
    print(f'Ошибка: {ve}')

#Прочитать сонекс
def sonex_ecosystem_reader():
    products = []

    for i, cell in enumerate(worksheet['B'][1:], start=2):
        imgs_temp = [
            worksheet[f'DL{i}'].value, worksheet[f'DN{i}'].value, worksheet[f'DP{i}'].value,
            worksheet[f'DQ{i}'].value, worksheet[f'DR{i}'].value, worksheet[f'DS{i}'].value,
            worksheet[f'DT{i}'].value, worksheet[f'DU{i}'].value, worksheet[f'DV{i}'].value,
            worksheet[f'DM{i}'].value, worksheet[f'DO{i}'].value
        ]
        imgs = [value for value in imgs_temp if value is not None]

        product = {
            # Основная информация
            'model': worksheet[f'B{i}'].value,
            'name': worksheet[f'C{i}'].value,
            'promotion_price': worksheet[f'F{i}'].value,
            'price': worksheet[f'E{i}'].value,
            'type_1': worksheet[f'P{i}'].value,
            'type_2':worksheet[f'Q{i}'].value,
            'family': worksheet[f'R{i}'].value,
            'manufactor': manufactor(worksheet[f'N{i}'].value),
            'code': worksheet[f'A{i}'].value,
            'Описание': worksheet[f'BG{i}'].value,

            #Картинки
            'imgs': imgs,

            # характеристики
            'Источник света': light_source(worksheet[f'U{i}'].value),
            'Материал арматуры': worksheet[f'AJ{i}'].value,
            'Цвет арматуры': worksheet[f'AK{i}'].value,
            'Тип поверхности арматуры': worksheet[f'AM{i}'].value,
            'Материал плафона': worksheet[f'AN{i}'].value,
            'Цвет плафона': worksheet[f'AO{i}'].value,
            'Тип поверхности плафона': worksheet[f'AQ{i}'].value,
            'Вид декора': worksheet[f'AR{i}'].value,
            'Материал декора': worksheet[f'AS{i}'].value,
            'Цвет декора': worksheet[f'AT{i}'].value,
            'Высота': f'{height(worksheet[f'BM{i}'].value, worksheet[f'BN{i}'].value)} мм',
            'Длина': f'{worksheet[f'BS{i}'].value} мм',
            'Ширина': f'{worksheet[f'BV{i}'].value} мм',
            'Диаметр': f'{worksheet[f'BP{i}'].value} мм',
            'Вес': f'{worksheet[f'EO{i}'].value} кг',
            'Цоколь': worksheet[f'S{i}'].value,
            'Количество ламп': f'{worksheet[f'AA{i}'].value} шт',
            'Общая мощность': f'{worksheet[f'AC{i}'].value} Вт',
            'Гарантийный срок': f'{worksheet[f'BA{i}'].value} мес',
            'Рекомендуемая площадь освещения': f'{worksheet[f'AH{i}'].value} кв.м',
            'Степень пылевлагозащиты': worksheet[f'AW{i}'].value,
            'Страна производитель': worksheet[f'EB{i}'].value,
            'Дизайн': worksheet[f'BH{i}'].value,
            'Дополнительная информация': worksheet[f'BC{i}'].value,
            'Помещение': worksheet[f'BE{i}'].value,
            'Крепление': worksheet[f'BF{i}'].value,

        }

        products.append(product)

    return products