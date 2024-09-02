from ftplib import FTP
from readers.reader_imperia import imperia_brand_reader
from delete.delete_imperiya import delete_rows, delete_imgs

def main_kink_light():
    from readers.reader_kink_light import kink_light_reader
    from merge.merge_imperia_kink_light import append_kink_light
    from merge.merge_imperia_kink_light import change_and_delete_kink_light

    print('Программа начилась')
    products_imperia = imperia_brand_reader('Kink Light')
    print('(1/8) Считался файл базы данных Империи люстр...')
    products_kink_light = kink_light_reader()
    print('(2/8) Считался файл Кинк Лайта...')
    id_list, img_list = change_and_delete_kink_light(products_imperia, products_kink_light)
    print('(3/8) Составился список удаления позиций...')
    all_new_products = append_kink_light(products_imperia, products_kink_light)
    print('(4/8) Составился список новых товаров и скачались картинки...')

    delete_rows(id_list)
    print('(5/8) Удалились ненужные позиции...')

    ftp = FTP('vh340.timeweb.ru')
    ftp.login(user='lustri33', passwd='1arthur_nyamaa1')

    delete_imgs(img_list, ftp)
    print('(6/8) Удалились картинки с сервера...')


    from write.write_imperiy import write

    write(all_new_products)
    print('(7/8) Добавились новые товары...')
    from changer.all_id_change import id_change

    id_change()
    print('(8/8) Подкорретировались все айдишники...')
    print('Программа закончилась')