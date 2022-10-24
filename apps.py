from operator import imod
import bottle
#各パスルーティング
import routes
# import routes_form
import routes_list
import routes_login
import routes_add
from utils.session import Session
app = routes.app
app_sess = routes.app_sess
if __name__ == '__main__':
    # this setting is running for development.
    bottle.run(app=app_sess, host='0.0.0.0',port=8888, reloader=True, debug=True)

