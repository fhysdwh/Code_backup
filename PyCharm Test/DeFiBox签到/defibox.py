from selenium import webdriver
import time


driver = webdriver.Chrome('./chromedriver')
url = 'https://www.defibox.com/assets/?utm_source=3253793'
driver.get(url)
cookie1 = {
    'name': '_uab_collina',
    'value': '161341007836472657869715'
}
cookie2 = {
    'name': '__cfduid',
    'value': 'd81ba3bf51c91c2a92c7517b7baa979231613493818'
}
cookie3 = {
    'name': '_ha_session',
    'value': '1613499946535'
}
cookie4 = {
    'name': 'dgg-uc-token',
    'value': '"alKIKoUaNLuUcyPuBPuWz/mTRCg9ZIXWlp/yYUkVTbUlKJ90B7WhTMPSDOOOWSVtmwaZVfuoJa57N6ZnR6UpLKemxwRY0jQHjvFI5BYWU9z44EvCCAIkdmsGshnXlm6nkoIcIVIoySlEqxRiVJXbd2N/WzHJ6G850/3U+vkupqg="'
}
driver.add_cookie(cookie1)
driver.add_cookie(cookie2)
driver.add_cookie(cookie3)
driver.add_cookie(cookie4)
time.sleep(2)
response = driver.get(url)
time.sleep(5)

driver.quit()