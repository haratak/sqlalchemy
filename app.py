#coding: utf-8
from flask import Flask, request, render_template
import datetime
import os
# データベースを使うにあたり追加
# from assets.database import db_session
# from assets.models import Data

app = Flask(__name__)


@app.route('/')
def bbs():
    return "hello world!"
    # # データベースから読み込む
    # data = db_session.query(Data.name, Data.article, Data.timestamp).all()

    # # index.htmlに返す
    # return render_template('index.html', data=data)


# postメソッドを受け取る
# @app.route('/result', methods=['POST'])
# def result():
#     # requestでarticleとnameの値を取得する
#     article = request.form['article']
#     name = request.form['name']
#     # today関数でpostメソッドを受け取った日時を変数に代入
#     today = datetime.datetime.today()

#     # index_resultからの情報をデータベースに書き込む
#     row = Data(name=name, article=article, timestamp=today)
#     print('do!!!')
#     db_session.add(row)
#     print('commit!!!')
#     db_session.commit()

#     # index_result.htmlに返す
    # return render_template('index_result.html', article=article, name=name)


if __name__ == '__main__':
    app.run()


# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
# db = SQLAlchemy(app)


# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True)
#     email = db.Column(db.String(120), unique=True)

#     def __init__(self, username, email):
#         self.username = username
#         self.email = email

#     def __repr__(self):
#         return '<User %r>' % self.username
# #
