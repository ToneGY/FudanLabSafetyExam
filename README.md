# FudanLabSafetyExam
复旦大学实验室安全考试校级试卷运行脚本
本项目参考https://github.com/dannyXSC/Fudan_FreshmanTest

## 成果
本项目的目标是尽可能地操作方便，以让更多的同学能够使用。

基本上能够稳上90分，如果未来因为题库更新的原因正确率下降，可以自行通过本项目自带的更新
题库功能，来提高准确率。

## 环境配置
### selenium
可以自行去网上搜索下载方案，比如
https://blog.csdn.net/qq_48736958/article/details/115179198

其中下载selenium时请使用
```text
pip install selenium==3.14.0
```
### 其他依赖
```text
selenium==3.14.0
json
os
time
typing
```
### 环境变量
（如果不需要优化本项目，仅仅想要使用的同学可以跳过这一部分）
本项目的环境变量在`environment.py`中

```python
driver_path = r"D:\path\msedgedriver.exe"
# default
main_page = f"https://uis.fudan.edu.cn/authserver/login?service=https%3A%2F%2Ftac.fudan.edu.cn%2Foauth2%2Fauthorize.act%3Fclient_id%3De6b06fa1-edb8-40cd-adf4-5a992e4d6de0%26response_type%3Dcode%26redirect_uri%3Dhttp%3A%2F%2Flsem.fudan.edu.cn%2Ffd_aqks_new%2Findex"

usrname = ""
password = ""

cookie_path = 'asset/cookies.txt'
question_path = "asset/questions.json"

if_add_question = True

```
- usrname: 复旦学号
- password: 账号密码
- driver_path: 如果你在安装selenium时，把webdriver放在了python的目录底下，就可以把这行注释掉了。
否则，要填入你的webdriver的路径。
- cookie_path: 保存cookie的位置（不上传到github）
- question_path: 保存题库的位置（上传）
- if_add_question: 每次更新是覆盖还是增加（为True则增加）

## 运行

自动答题
```text
python main.py
```

### 扩充题库
为了以防未来题库扩充，或者题库数据被污染，所以本项目带有扩充题库功能。

如果你需要删除以前的题库，则将`environment.py`中的`if_add_question`设置为False
```python
if_add_question = False
```
并执行以下命令，否则则将`if_add_question`设置为True，此时，题库将会增长而不覆盖。
```text
python load_question.py
```

