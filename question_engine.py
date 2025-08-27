import json
import time
import re
from typing import List

from selenium.webdriver.remote.webdriver import WebDriver, WebElement

from operation_engine import goto_next_question, submit_exam
from question import Question


def get_questions_answers(browser: WebDriver) -> List[Question]:
    result = browser.find_element_by_id("questions").find_elements_by_class_name("question_holder")
    question_list = []
    # dic = {"选项A":0, "选项B":1, "选项C":2, "选项D":3}
    for question in result:
        question_text = question.find_element_by_class_name("question_text").text
        pattern1 = r'^\d+\.'
        pattern2 = r'^[A-D]+、'
        question_text = re.sub(pattern1, '', question_text).strip()
        # answers_option = []
        correct_texts = []
        answers = []
        for answer in question.find_elements_by_class_name("answer"):
            answers.append(answer.find_element_by_class_name("answer_text").text)
        for answer in question.find_elements_by_class_name("correct_answer"):
            correct_texts.append(answer.find_element_by_class_name("answer_text").text)

        # for option in question.find_elements_by_class_name("row"):
        #     option_text = option.find_elements_by_tag_name("label")[0].text
        #     if option_text.startswith("选项") == False:
        #         continue
        #     answer_text = option.find_element_by_tag_name("span").text
        #     if(option_text in answers_option):
        #         correct_texts.append(answer_text)
        #     answers.append(answer_text)
            
        # correct_answers = question.find_elements_by_class_name("info")
        # correct_ids = [correct.get_attribute("id").split("_")[1] for correct in correct_answers]
        # correct_texts = [question.find_elements_by_xpath(f'//label[@for="answer-{correct_id}"]')[0].text for correct_id in correct_ids]
        # dic = {"stem": question_text, "answers": answers, "correct_answers": correct_texts}
        question_list.append(Question(question_text, answers, correct_texts))
        # question_list.append(Question.from_dict(dic))
        print(f"question_text: {question_text}")
        print(f"answers: {answers}")
        print(f"correct_text: {correct_texts}")
    return question_list


def question_list_to_dict(question_list: List[Question]) -> dict:
    result = {}
    for question in question_list:
        if question.stem not in result:
            result[question.stem] = [question]
        else:
            result[question.stem].append(question)
    return result


def question_list_merge(a: List[Question], b: List[Question]):
    # merge to a
    a_set = question_list_to_dict(a)
    for question in b:
        flag = True
        if question.stem in a_set:
            for a_question in a_set[question.stem]:
                if question.equal(a_question):
                    flag = False
        if flag:
            a.append(question)


def answer_question(browser: WebDriver, question_dict: dict):
    # time.sleep(3)
    try:
        problem = browser.find_element_by_class_name("question_text").text
        pattern1 = r'^\d+\.'
        pattern2 = r'^[A-D]+、'
        problem = re.sub(pattern1, '', problem).strip()
        answers_element = browser.find_element_by_tag_name("fieldset").find_elements_by_class_name("answer")
        answers = []
        for answer in answers_element:
            text = answer.find_element_by_class_name("answer_label").text
            if(text==''):
                exit()
                continue
            answers.append(re.sub(pattern2, '', text).strip())
        cur_question = Question(stem=problem, answers=answers)
        print(problem)
        print(answers)
        find_question = None
        if cur_question.stem in question_dict:
            for question in question_dict[cur_question.stem]:
                if cur_question.equal(question):
                    find_question = question
                    break
        if find_question is None:
            return
        correct_answers_set = find_question.correct_answers_set
        for ele in answers_element:
            text = ele.find_element_by_class_name("answer_label").text
            text = re.sub(pattern2, '', text).strip()
            if text in correct_answers_set:
                ele.find_element_by_class_name("question_input").click()
    except:
        print("error")


def answer_all_questions(browser: WebDriver, question_dict: dict):
    num = 1
    answer_question(browser, question_dict)
    while num < 100 and goto_next_question(browser) is not None:
        num += 1
        answer_question(browser, question_dict)
    time.sleep(5)
    submit_exam(browser)


def save_question_list(question_list: List[Question], path):
    with open(path, 'w') as f:
        f.write(json.dumps([question.to_dict() for question in question_list]))


def load_question_list(path):
    with open(path, 'r', encoding='utf8') as f:
        question_list_json = json.loads(f.read())
    return [Question.from_dict(question) for question in question_list_json]
