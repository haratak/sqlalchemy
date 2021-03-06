#coding: utf-8

# database.py/sqliteなど、どのデータベースを使うのか初期設定を扱うファイル
from sqlalchemy import create_engine, engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import datetime
import os

# data_dbという名前で、database.pyのある場所に（os.path.dirname(__file__)）、絶対パスで（os.path.abspath）、data_dbを保存する
db_uri = os.environ.get('DATABASE_URL').replace("://", "ql://", 1)

# or "postgresql://localhost/user_db"
# DATABASE = 'postgresql'
# USER = 'takuya'
# PASSWORD = 'postgres'
# HOST = 'localhost'
# PORT = '5432'
# DB_NAME = 'user_db'

# CONNECT_STR = '{}://{}:{}@{}:{}/{}'.format(
#     DATABASE, USER, PASSWORD, HOST, PORT, DB_NAME)


# database_file = os.path.join(os.path.abspath(
#     os.path.dirname(__file__)), 'users.db')

# データベースsqliteを使って（engin)、database_fileに保存されているdata_dbを使う、またechoで実行の際にsqliteを出す（echo=True)
# connecting sqlite
# engine = create_engine(os.environ.get(
#     'DATABASE_URL') or 'sqlite:///' + database_file, convert_unicode=True, echo=True)
engine = create_engine(db_uri)

db_session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine
    )
)

# declarative_baseのインスタンス生成する
Base = declarative_base()
Base.query = db_session.query_property()


# データベースの初期化をする関数
def init_db():
    # assetsフォルダのmodelsをインポート
    import assets.models
    Base.metadata.create_all(bind=engine)
