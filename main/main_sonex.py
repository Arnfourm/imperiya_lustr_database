from ftplib import FTP
from readers.reader_imperia import imperia_brand_reader
from delete.delete_imperiya import delete_rows, delete_imgs

def main_sonex():
    from readers.reader_sonex_ecosystem import sonex_ecosystem_reader
    from merge.merge_imperiya_sonex import append_sonex
    from merge.merge_imperiya_sonex import change_and_delete_sonex

    print('Программа начилась')
    products_imperia_odeon_light = imperia_brand_reader('Odeon Light')
    products_imperia_lumion = imperia_brand_reader('Lumion')
    products_imperia_sonex = imperia_brand_reader('Сонекс')
    products_imperia = products_imperia_odeon_light + products_imperia_lumion + products_imperia_sonex
    print('(1/8) Считался файл базы данных Империи люстр...')
    products_sonex_ecosystem = sonex_ecosystem_reader()
    print('(2/8) Считался файл сонекса..')
    id_list, img_list = change_and_delete_sonex(products_imperia, products_sonex_ecosystem)
    print('(3/8) Составился список удаления позиций...')
    all_new_products = append_sonex(products_imperia, products_sonex_ecosystem)
    print('(4/8) Составился список новых товаров и скачались картинки...')

    delete_rows(id_list)
    print('(5/8) Удалились ненужные позиции...')

    ftp = FTP('vh340.timeweb.ru')
    ftp.login(user='lustri33', passwd='1arthur_nyamaa1')

    #delete_imgs(img_list, ftp)
    print('(6/8) Удалились картинки с сервера...')


    from write.write_imperiy import write

    write(all_new_products)
    print('(7/8) Добавились новые товары...')
    from changer.all_id_change import id_change

    id_change()
    print('(8/8) Подкорретировались все айдишники...')
    print('Программа закончилась')