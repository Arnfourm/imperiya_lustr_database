import os
import requests
from concurrent.futures import ThreadPoolExecutor
import re

def sanitize_filename(filename):
    return re.sub(r'[<>:"\\|?*]', '_', filename)

def get_filename_from_url(img_url):
    if 'catalog_itemPics' in img_url:
        # Извлечь код из URL
        match = re.search(r'code=([0-9A-Za-z]+)', img_url)
        if match:
            return match.group(1) + '.jpg'  # Предполагаем формат JPG
    else:
        # Извлечь имя файла из URL второго типа
        img_name = os.path.basename(img_url)
        if not re.search(r'\.\w+$', img_name):  # Если нет расширения
            img_name += '.jpg'  # Добавляем расширение по умолчанию
        return sanitize_filename(img_name)

def download_image(img_url, dir_path, brand_name):
    if img_url.strip() == '':
        return None

    try:
        response = requests.get(img_url, stream=True)
        response.raise_for_status()

        img_name = get_filename_from_url(img_url)
        img_path = os.path.join(dir_path, img_name)

        with open(img_path, 'wb') as img_file:
            for chunk in response.iter_content(chunk_size=8192):
                img_file.write(chunk)

        relative_path = f'catalog/{brand_name}/{img_name}'
        return relative_path

    except (requests.exceptions.HTTPError, requests.exceptions.RequestException):
        return None

def img_download(imgs, brand_name):
    dir_path = os.path.join('../imgs', f'img_{brand_name}')
    successful_downloads = []

    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(download_image, img_url, dir_path, brand_name) for img_url in imgs]

        for future in futures:
            result = future.result()
            if result:
                successful_downloads.append(result)

    main_img = successful_downloads.pop(0) if successful_downloads else None

    return main_img, successful_downloads