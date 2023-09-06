# -*- coding: utf-8 -*-


import webview
from flask import Flask, render_template

app = Flask(__name__)


# def open_webview():
    # webview.create_window("My Webview", "http://192.168.20.128:5000/index")


@app.route('/index', methods=["GET"])
def first_page():
    content = {
        'username': "刘德华"
    }
    return render_template("index.html", **content)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    # open_webview()
