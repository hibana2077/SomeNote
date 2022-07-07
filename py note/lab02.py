'''
Author: error: git config user.name && git config user.email & please set dead value or install git
Date: 2022-07-07 10:31:01
LastEditors: error: git config user.name && git config user.email & please set dead value or install git
LastEditTime: 2022-07-07 10:40:58
FilePath: \summer project\lab\lab02.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
#test api send array to python
from flask import Flask, request,jsonify
from flask_cors import CORS
import time
import json

app = Flask(__name__)
CORS(app)

@app.route('/test')#getlist
def test():
    templist = request.args.getlist('test')
    print(templist)
    return jsonify({"status": "success"})

@app.route('/test2')#getstring use this is better
def test2():
    templist = request.args.get('test')
    print(templist.split(','))
    return jsonify({"status": "success"})

@app.route('/welcome')
def welcome():
    return jsonify({"status": "success"})

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=9999)
    except Exception as e:
        print(e)
        pass