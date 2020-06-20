from flask import Flask, render_template


def init_app():
    @app.route("/")
    def hello():
        return "hello world"

    @app.route("/index")
    def index():
        return render_template('/style/index.html')