####爬取淘宝网的商品信息###

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote
from pyquery import PyQuery as pq

brower = webdriver.Chrome()
wait = WebDriverWait(brower, 10)
KEYWORD = 'iPad'


def get_products():
    """
    提取商品信息
    :return:
    """
    html = brower.page_source
    doc = pq(html)
    items = doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        product = {
            'image': item.find(' .pic .img').attr('data-src'),
            'price': item.find(' .price').text(),
            'deal': item.find(' .deal-cnt').text(),
            'title': item.find(' .title').text(),
            'shop': item.find(' shop').text(),
            'location': item.find(' .location').text()
        }
        print(product)


def index_page(page):
    """
    抓取索引页
    :param page: 页码
    :return:
    """
    print('正在爬取第', page, '页')
    try:
        url = 'https://s.taobao.com/search?q=' + quote(KEYWORD)
        # url = 'https://www.taobao.com/'
        brower.get(url)
        if page > 1:
            input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager div.form > input')))
            submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager div.form > span.btn.J_Submit')))
            input.clear()
            input.send_keys(page)
            submit.click()
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager li.item.active > span'), str(page)))
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ' .m-itemlist .items .item')))

        get_products()
    except TimeoutException:
        index_page(page)