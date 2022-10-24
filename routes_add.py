from bottle import Bottle, jinja2_template as template,request, redirect
from bottle import response
import routes
from models import connection, Books
from utils.auth import Auth
import urllib.parse as urlpar

#routesからappを読み込む
app  = routes.app
auth = Auth()

@app.route('/add')
def add():
    #認証確認
    auth.check_login()
    return template('add.html')

@app.route('/store', method=['GET', 'POST'])
def store():
    if request.forms.get('next') == 'back':
        #確認画面から戻るボタンを押す
        #登録フォームに戻る
        response.status = 307
        response.set_header("Location", '/add')
        return response
    else:
        #フォームから値を取得する
        id = request.forms.decode().get('id')
        name  = request.forms.decode().get('name')
        volume   = request.forms.decode().get('volume')
        author = request.forms.decode().get('author')
        publisher = request.forms.decode().get('publisher')
        memo = request.forms.decode().get('memo')

        #sqlを記入する
        sql = """insert into book_user(user_id, passwd, email, user_shi, user_mei, del) values(%(user_id)s, %(passwd)s, %(email)s, %(user_shi)s, %(user_mei)s, false);"""
        #入力する値の辞書を設定する
        val = {'user_id':user_id, 'passwd':passwd, 'email':email, 'user_shi':user_shi,'user_mei':user_mei}
        with get_connection() as con:#DBの接続を取得
            with con.cursor() as cur:#カーソルを取得
                cur.execute(sql, val)
            con.commit()
        redirect('/add')