import openpyxl
import xml.etree.ElementTree as ET
from attribute_changer.kink_light_attribute_change import light_source, room

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

#Xml файлы
try:
    with open('../additional/brand_xml_path.txt', 'r') as file:
        xml_path = file.read().strip()
        if not xml_path:
            raise ValueError('Необходимо указать xml файл базы данных Бренда')

    with open(xml_path, 'r', encoding='windows-1251') as xml_file:
        xml_content = xml_file.read()

    root = ET.fromstring(xml_content)

except ValueError as ve:
    print(f'Ошибка: {ve}')

#прочитать файл кинк лайта
def kink_light_reader():
    products = []

    for i, cell in enumerate(worksheet['C'][3:], start=4):
        if cell.value is None:
            continue
        else:
            imgs = [worksheet[f'I{i}'].value, worksheet[f'J{i}'].value, worksheet[f'K{i}'].value,
                    worksheet[f'L{i}'].value]
            product = {
                # Основная информация
                'model': worksheet[f'C{i}'].value,
                'promotion_price': worksheet[f'G{i}'].value,
                'price': worksheet[f'H{i}'].value,
                'type': worksheet[f'M{i}'].value,
                'family': worksheet[f'N{i}'].value,
                'manufactor': worksheet[f'AG{i}'].value,
                'code': worksheet[f'B{i}'].value,
                'name': worksheet[f'A{i}'].value,
                'Описание': None,

                # картинки
                'imgs': imgs,

                # характеристики
                'Источник света': light_source(worksheet[f'O{i}'].value),
                'Материал арматуры': worksheet[f'Q{i}'].value,
                'Цвет арматуры': worksheet[f'R{i}'].value,
                'Цвет стекла': worksheet[f'S{i}'].value,
                'Вес упаковки': f'{worksheet[f'T{i}'].value} кг',
                'Высота': f'{worksheet[f'V{i}'].value}0 мм',
                'Длина': f'{worksheet[f'W{i}'].value}0 мм',
                'Ширина': f'{worksheet[f'X{i}'].value}0 мм',
                'Диаметр': f'{worksheet[f'Y{i}'].value}0 мм',
                'Цоколь': worksheet[f'AC{i}'].value,
                'Количество ламп': f'{worksheet[f'AD{i}'].value} шт',
                'Общая мощность': worksheet[f'AF{i}'].value,
                'Гарантийный срок': worksheet[f'AI{i}'].value,
                'Дополнительная информация': worksheet[f'AJ{i}'].value,
                'Рекомендуемая площадь освещения': f'{worksheet[f'AL{i}'].value} м2',
                'Степень пылевлагозащиты': worksheet[f'AQ{i}'].value,
                'Страна производитель': worksheet[f'AH{i}'].value,
                'Помещение': None
            }
            for offer in root.findall('.//offer'):
                if offer.get('id') == product['code']:
                    product['Помещение'] = room(offer.find('naznachenie').text)
                    product['Описание'] = offer.find('description').text
            products.append(product)
    return products