from flask import Flask
from flask import render_template,redirect,Response,make_response
from functools import wraps

app = Flask(__name__)

def zhuangshii(func):
    @wraps(func)
    def inner():
        print("login执行之前执行")
        r = func()
        return r
    return  inner


@app.route("/login/")
@zhuangshii
def login():
    #return "Hello world" # str
    # print(type(render_template("login.html"))) # str
    # return render_template("login.html")
    # print(type(redirect("https://www.baidu.com"))) # response
    # return redirect("https://www.baidu.com")
    # 1. 显示在页面的数据  2. 状态码
    return Response("我是自己创建的文件",404)
    # resp = make_response(render_template('login.html'))
    # resp.headers['tag'] = 'chang ping jing li zhen  shi  ge  gou zi'
    # return resp

    return "chang ping jing li zhen  shi  ge  gou zi",200


# 返回字符串
    # return "Hello world" # str
    # print(type(render_template("login.html"))) # str
    # return render_template("login.html")
# 返回Response对象
    # print(type(redirect("https://www.baidu.com"))) # response
    # return redirect("https://www.baidu.com")
    # 1. 显示在页面的数据  2. 状态码
    # return Response("我是自己创建的文件",404)
    # resp = make_response(render_template('login.html'))
    # resp.headers['tag'] = 'chang ping jing li zhen  shi  ge  gou zi'
    # return resp
# 返回元组
    # return "chang ping jing li zhen  shi  ge  gou zi", 200


if __name__ == '__main__':

    app.run(debug=True)


