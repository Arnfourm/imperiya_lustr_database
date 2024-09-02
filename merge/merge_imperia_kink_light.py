from changer.name_change import name_changer_kink_light
from changer.price_change import price_changer
from changer.categories_change import categories_changer_kink_light
from changer.attributes_change import attribute_changer
from changer.description_change import description_change
from changer.img_change import img_download
from changer.meta_description_change import meta_description

def change_and_delete_kink_light(products_imperia, products_kink_light):
    id_list = []
    img_list = []
    i = 0

    while i < len(products_imperia):
        imperia = products_imperia[i]
        found = False
        for j in range(len(products_kink_light)):
            kink_light = products_kink_light[j]
            if imperia['model'] == kink_light['model']:
                found = True
                imperia['sort_order'] = '1'
                #Меняем цену на актуальную
                if kink_light['promotion_price'] != ' ':
                    imperia['price'] = kink_light['promotion_price']
                    kink_light['sale'] = 'Yes'
                else:
                    imperia['price'] = kink_light['price']
                    kink_light['sale'] = 'No'
                del products_kink_light[j]
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


def append_kink_light(products_imperia, products_kink_light):
    for kink_light in products_kink_light:
        if kink_light['type'] in ['Комплектующие', 'Текстильная трековая система Сатори', 'Мебель из ротанга',
                                  'Трековые системы']:
            continue

        name, categories = name_changer_kink_light(kink_light['name'], kink_light['manufactor'], kink_light['model'],
                                                   kink_light['family'])
        main_img, imgs = img_download(kink_light['imgs'], 'kink light')

        product = {
            #Основная информация
            'id': f'id_{kink_light['model']}',
            'name': name,
            'categories': categories_changer_kink_light(categories),
            'model': kink_light['model'],
            'manufactor': kink_light['manufactor'],
            'price': price_changer(kink_light['promotion_price'], kink_light['price']),
            'meta_title': f'{name} {kink_light['Цвет арматуры']}',
            'meta_description': meta_description(name, kink_light['Материал арматуры'], kink_light['Цвет арматуры'],
                                                 kink_light['Помещение']),
            'meta_keywords': f'{kink_light['type']}, {kink_light['type']} {kink_light['Цвет арматуры']}, Цена, '
                             f'{kink_light['manufactor']}, {kink_light['model']}, Купить, в {kink_light['Помещение']}',
            'tags': f'Товары в серии {kink_light['family']}',
            'code': kink_light['code'],
            'description': description_change(kink_light['Описание']),
            'sort_order': '0',

            #Картинки
            'main_img': main_img,
            'additiobal_imgs': imgs,

            #Характеристики
            'attributes': attribute_changer(kink_light)
        }
        products_imperia.append(product)
    return products_imperia