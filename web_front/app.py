# encoding: utf-8

from flask import Flask, render_template,request
import config


app = Flask(__name__)
app.config.from_object(config)


# 首页
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


# 用户注册页面
@app.route('/resist/', methods=['GET', 'POST'])
def resist():
    return render_template('resist.html')


# 文件上传页面
@app.route('/uploads/', methods=['GET', 'POST'])
def uploads():
    return render_template('uploads.html')


# 首次进入页面
@app.route('/first/', methods=['GET', 'POST'])
def first():
    return render_template('first.html')


# 一次上传一图页面
@app.route('/single/', methods=['GET', 'POST'])
def single():
    return render_template('singlefile.html')


# 统计分析页面
@app.route('/analyse/', methods=['GET', 'POST'])
def analyse():
    return render_template('analyse.html')


if __name__ == '__main__':
    app.run()
