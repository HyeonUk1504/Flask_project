from flask import Blueprint, url_for

from werkzeug.utils import redirect


bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/hello')
def hello_pybo():
    return 'Hello, Pybo!'


@bp.route('/')
def index():
    return redirect(url_for('question._list')) #  question._list는 question, _list 순서로 해석되어 라우팅 함수를 찾는다. question은 등록된 블루프린트 별칭, _list는 블루프린트에 등록된 함수명

# 리다이렉트(redirect)는 웹 애플리케이션에서 사용자의 요청을 다른 URL로 보내는 것을 의미
