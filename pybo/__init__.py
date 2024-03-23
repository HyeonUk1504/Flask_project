from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    # ORM
    db.init_app(app)
    migrate.init_app(app,db)
    from . import models

    # 블루프린트
    from .views import main_views, question_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)

    return app


# app = Flask(__name__)

# # app = Flask(__name__) 는 flask 애플리케이션을 생성하는 코드
# # __name__ 은 현재 파일(모듈)이 직접 실행되는지, 아니면 import 되는지 구별하기 위해 사용
#
# @app.route('/')
# def hello_pybo():
#     return 'Hello, Pybo!'
#
# # @app.route 은 URL과 Flask code를 맵핑하는 flask 데코레이터다. '/' URL이 요청되면 Flask는 hello_pybo() 함수를 실행시킨다.

