from selenium import webdriver
import time
def main():
    b = webdriver.Chrome()
    b.get('https://www.taobao.com/')
    time.sleep(5)
    b.quit()
if __name__ == '__main__':
    main()
