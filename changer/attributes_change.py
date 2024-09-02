def attribute_changer(product):
    attributes = []
    attributes_to_check = ['Источник света', 'Материал арматуры', 'Цвет арматуры', 'Цвет стекла', 'Высота', 'Длина',
                           'Вес упаковки', 'Ширина','Диаметр', 'Цоколь', 'Количество ламп', 'Общая мощность',
                           'Степень пылевлагозащиты','Гарантийный срок', 'Дополнительная информация',
                           'Рекомендуемая площадь освещения', 'Страна производитель', 'Помещение']

    for key, value in product.items():
        if key in attributes_to_check:
            if value in [' ', None, 'None', ' 0 мм', '  кг', '  шт', '  м2', 'None мм', 'None кг', 'None шт',
                         'None м2', 'None мес', 'None Вт', 'None кв.м', '-', '_']:
                continue
            elif key in ['Гарантийный срок', 'Дополнительная информация', 'Рекомендуемая площадь освещения',
                         'Страна производитель', 'Помещение']:
                attribute = {
                    'attribute_group': 'Эксплуатационные характеристики',
                    'attribute': key,
                    'value': value
                }
            else:
                attribute = {
                    'attribute_group': 'Конструктивные характеристики',
                    'attribute': key,
                    'value': value
                }
            attributes.append(attribute)

    return attributes