import json
import os
import time
from selenium import webdriver

from environment import auth_url, cookie_path, input_wait_time, driver_path, main_page, if_load_cookie,usrname,password


def load_cookies(log_url, browser, path=cookie_path):
    """
    获取cookies保存至本地
    """
    browser.get(log_url)
    time.sleep(input_wait_time)  # 进行扫码
    dictCookies = browser.get_cookies()  # 获取list的cookies
    jsonCookies = json.dumps(dictCookies)  # 转换成字符串保存

    with open(path, 'w') as f:
        f.write(jsonCookies)
    print('cookies保存成功！')


def get_cookies(browser, path=cookie_path):
    with open(path, 'r', encoding='utf8') as f:
        listCookies = json.loads(f.read())
    for cookie in listCookies:
        browser.add_cookie(cookie)


def driver_get_with_cookies(url, path=cookie_path):
    browser = webdriver.Edge(executable_path=driver_path)
    # if not os.path.exists(path) or if_load_cookie:
    #     try:
    #         load_cookies(auth_url, browser, path)
    #     finally:
    #         print("123")
            # browser.quit()
            # browser = webdriver.Edge(executable_path=driver_path)
    # if()
    # load_cookies(auth_url, browser, "./my_cookie.txt")
    browser.get(url)
    time.sleep(1)
    browser.find_elements_by_class_name("el-input--suffix")[1].find_element_by_tag_name("input").send_keys(usrname)
    browser.find_elements_by_class_name("el-input--suffix")[2].find_element_by_tag_name("input").send_keys(password)
    # browser.find_element_by_id("password").send_keys(password)
    browser.find_element_by_class_name("el-button--primary").click()
    
    # get_cookies(browser, path)
    
    # browser.refresh()
    
    time.sleep(1)
    browser.get(url)
    # browser.find_element_by_class_name("card").find_elements_by_tag_name("div")[2].find_elements_by_tag_name("input")[0].click()
    # time.sleep(1)
    
    # browser.find_element_by_class_name("clearfix_index").find_elements_by_tag_name("div")[0].find_element_by_tag_name("a").click()
    
    # time.sleep(1)
    # browser.execute_script("document.getElementsByClassName('btn btn-default')[0].click()")
    return browser


# if __name__ == "__main__":
#     driver = webdriver.Edge(executable_path=driver_path)
#     load_cookies(auth_url, driver, "./my_cookie.txt")
#     input()
#     driver.quit()
