import os
import time

from cookie_engine import driver_get_with_cookies
from environment import if_add_question, question_path, main_page, cookie_path
from operation_engine import generate_answer
from question_engine import load_question_list, get_questions_answers, question_list_merge, save_question_list

if __name__ == "__main__":
    for i in range(0,10):
        driver = driver_get_with_cookies(main_page, cookie_path)

        # time.sleep(10)
        # try:
            
        print("-------------------开始获得答案信息------------------")
        question_list_old = []
        if os.path.exists(question_path) and if_add_question:
            question_list_old = load_question_list(question_path)

        generate_answer(driver)
        question_list = get_questions_answers(driver)
        question_list_merge(question_list, question_list_old)
        save_question_list(question_list, question_path)
        # finally:
            # driver.quit()
# https://uis.fudan.edu.cn/authserver/login?service=https%3A%2F%2Ftac.fudan.edu.cn%2Foauth2%2Fauthorize.act%3Fclient_id%3De6b06fa1-edb8-40cd-adf4-5a992e4d6de0%26response_type%3Dcode%26redirect_uri%3Dhttp%3A%2F%2Flsem.fudan.edu.cn%2Ffd_aqks_new%2Findex