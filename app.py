'''
Author : Salvador Hernandez Mendoza
Email  : salvadorhm@gmail.com
Twitter: @salvadorhm
kuorra version: 0.7.3.0
Created: 07/Mar/2018
'''
import web
import config
import urls

# activate ssl certificate
ssl = False

# time session
expires = 1 # minutes

# get urls
urls = urls.urls

# key for HMAC
secret_key = "kuorra_key"

app = web.application(urls, globals())

"""
if ssl is True:
    from web.wsgiserver import CherryPyWSGIServer
    CherryPyWSGIServer.ssl_certificate = "ssl/server.crt"
    CherryPyWSGIServer.ssl_private_key = "ssl/server.key"
"""
if web.config.get('_session') is None:
    db = config.db
    store = web.session.DBStore(db, 'sessions')
    session = web.session.Session(
        app,
        store,
        initializer={
        'login': 0,
        'privilege': -1,
        'user': 'anonymous',
        'expire': '0000-00-00 00:00:00',
        'loggedin': False,
        'count': 0
        }
        )
    web.config._session = session
else:
    session = web.config._session

class Count:
    def GET(self):
        session.count += 1
        return str(session.count)

def InternalError(): 
    raise config.web.seeother('/500')

def NotFound():
    raise config.web.seeother('/404')

if __name__ == "__main__":
    db.printing = False # hide db transactions
    web.config.debug = False # hide debug print
    web.config.db_printing = False # hide db transactions
    app.internalerror = InternalError # page show in internal error
    app.notfound = NotFound # page show in page not found
    app.run()
