from selenium.webdriver.remote.webdriver import WebDriver, WebElement
import time

def take_exam(driver: WebDriver):
    try:
        driver.execute_script("document.getElementById('take_quiz_link').click()")
    except:
        driver.find_element_by_class_name("btn-primary").click()
        
    # driver.find_element_by_id("examOnlineIndexDiv").find_elements_by_class_name("fl enter_test")[3].find_element_by_tag_name("div").find_element_by_tag_name("a").click()
    time.sleep(3)   
    # driver.find_element_by_id("examOnlineStrat").click()

def submit_exam(driver: WebDriver):
    # driver.find_element_by_id("submit_quiz_button").click()
    # alert = driver.switch_to.alert
    # alert.accept()
    time.sleep(1)
    try:
        driver.find_element_by_id("submit_quiz_button").click()
    finally:
        alert = driver.switch_to.alert
        print(f"弹窗文本: {alert.text}")
        alert.accept()  # 点击"确定"或"是"
    # time.sleep(3)
    # driver.execute_script("document.getElementsByClassName('bootstrap-dialog-footer-buttons')[0].getElementsByTagName('button')[0].click()")
    # time.sleep(10)
    
def goto_next_question(driver: WebDriver):
    target = driver.find_element_by_class_name("next-question")
    target.click()
    time.sleep(1)
    return True


def generate_answer(driver: WebDriver):
    take_exam(driver)
    submit_exam(driver)
