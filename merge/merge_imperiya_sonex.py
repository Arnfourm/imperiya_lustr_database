from changer.name_change import name_changer_sonex
from changer.img_change import img_download
from changer.categories_change import categories_changer_sonex
from changer.price_change import price_changer
from changer.description_change import description_change
from changer.attributes_change import attribute_changer

def change_and_delete_sonex(products_imperia, products_sonex):
    id_list = []
    img_list = []
    i = 0

    while i < len(products_imperia):
        imperia = products_imperia[i]
        found = False
        for j in range(len(products_sonex)):
            sonex = products_sonex[j]
            if imperia['model'] == sonex['model']:
                found = True
                imperia['sort_order'] = '1'
                #Меняем цену на актуальную
                if sonex['promotion_price'] not in [' ', 'None', None]:
                    imperia['price'] = sonex['promotion_price']
                    sonex['sale'] = 'Yes'
                else:
                    imperia['price'] = sonex['price']
                    sonex['sale'] = 'No'
                del products_sonex[j]
                break

        if found == False:
            id_list.append(products_imperia[i]['id'])
            img_list.append(products_imperia[i]['main_img'])
            for img in products_imperia[i]['additional_img']:
                img_list.append(img)
            del products_imperia[i]
        else:
            i += 1
    return id_list, img_list

def append_sonex(products_imperia, products_sonex):
    for sonex in products_sonex:
        if sonex['manufactor'] in ['Сонекс', 'Lumion', 'Odeon Light']:
            name, categories = name_changer_sonex(sonex['type_1'], sonex['type_2'], sonex['manufactor'], sonex['model'],
                                                  sonex['family'])
            main_img, imgs = img_download(sonex['imgs'], sonex['manufactor'])

            product = {
                #Основная информация
                'id': f'id_{sonex['model']}',
                'name': name,
                'categories': categories_changer_sonex(categories, sonex['type_2']),
                'model': sonex['model'],
                'manufactor': sonex['manufactor'],
                'price': price_changer(sonex['promotion_price'], sonex['price']),
                'meta_title': f'{name} {sonex['Цвет арматуры']}',
                'meta_description': f'({name}, {sonex['Материал арматуры']}, {sonex['Цвет арматуры']}, {sonex['Помещение']})',
                'meta_keywords': f'{sonex['type_1']}, {sonex['type_1']} {sonex['Цвет арматуры']}, Цена,'
                                 f' {sonex['manufactor']}, {sonex['model']}, Купить, в {sonex['Помещение']}',
                'tags': f'Товары в серии {sonex['family']}',
                'code': sonex['code'],
                'description': description_change(sonex['Описание']),
                'sort_order': '0',

                #Картинки
                'main_img': main_img,
                'additiobal_imgs': imgs,

                #Характеристики
                'attributes': attribute_changer(sonex)
            }
            products_imperia.append(product)
        else:
            continue
    return products_imperia