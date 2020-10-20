import math
import random
import time
import pymongo
from selenium.webdriver import \
    Chrome  # Специальный объект который позволяет нам получить, объект для управления браузером(WebDriver)
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

client = pymongo.MongoClient('localhost', 27017)
db = client['FarPost']
house_coll = db['House']
flat_coll = db['Flat']


def cd_flat(url, cost, area, address, type_flat, space):
    return {
        'url': url,
        'cost': cost,
        'area': area,
        'address': address,
        'type_flat': type_flat,
        'space': space
    }


def cd_home(url, area, address, developer):
    return {
        'url': url,
        'area': area,
        'address': address,
        'developer': developer

    }


def delay(min_t=10):
    max_t = min_t + 10
    s_time = random.randint(min_t, max_t)
    print('Выполняю задержку в ' + str(s_time) + ' секунд')
    time.sleep(s_time)


def load_data(collection, name_elem, link):
    print('=========================================================================')
    url_dict = {'url': link}
    result = collection.find_one(url_dict)
    if result:  # Если было найдено совпадение
        list_values = list(result.values())
        current_id = {'_id': list_values[0]}
        collection.update_one(current_id, {'$set': name_elem})
        print('Данные обновились: ' + str(name_elem))
    else:
        collection.insert_one(name_elem)
        print('Данные занесенны в бд: ' + str(name_elem))
    print('=========================================================================')


url_for_maxPage = "https://www.farpost.ru/vladivostok/realty/sell_flats"
url_CurrentPage = "https://www.farpost.ru/vladivostok/realty/sell_flats/?page="

driver = Chrome()
driver.get(url_for_maxPage)
maxPage = driver.find_element_by_id('itemsCount_placeholder')
count = maxPage.get_attribute('data-count')
numPage = math.ceil(int(count) / 50)

for i in range(numPage):
    currentPage = str(i + 1)
    url = url_CurrentPage + currentPage
    driver.get(url)
    delay(100)
    table_page = driver.find_elements_by_class_name('pageableContent')  # Все таблицы на страницы(1)
    if len(table_page) == 0:
        print('Page is ' + currentPage + ' Empty. Go Next.')
        continue
    table_page = table_page[0]
    ads = table_page.find_elements_by_class_name('bull-item-content')  # Все объявления на страницы(50)
    for elem in ads:  # Перебераем по одному объявлению
        url_currentAds = elem.find_elements_by_class_name('bull-item__self-link')
        if len(url_currentAds) == 0:
            print(404)
            continue
        current_url = url_currentAds[0].get_attribute('href')
        price = elem.find_elements_by_class_name('price-block__price')
        if len(price) == 0:
            driver.execute_script('window.open()')
            driver.switch_to.window(driver.window_handles[1])
            driver.get(current_url)
            delay(10)
            view = driver.find_elements_by_id('fieldsetView')
            view = view[0]
            fields = view.find_elements_by_class_name('value')
            load_data(house_coll, cd_home(current_url, fields[0].text, fields[1].text, fields[4].text), current_url)
        else:
            cost = price[0].text
            driver.execute_script('window.open()')
            driver.switch_to.window(driver.window_handles[1])
            driver.get(current_url)
            delay(10)
            view = driver.find_elements_by_id('fieldsetView')
            view = view[0]
            fields = view.find_elements_by_class_name('value')
            load_data(flat_coll,
                      cd_flat(current_url, cost, fields[1].text, fields[2].text, fields[3].text, fields[5].text),
                      current_url)

        driver.execute_script('window.close()')
        driver.switch_to.window(driver.window_handles[0])
