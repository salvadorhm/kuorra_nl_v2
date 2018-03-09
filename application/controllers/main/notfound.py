import application.controllers.main.config as config
import web
import app


class NotFound:
    
    def __init__(self):
        pass

    def GET(self):
        if app.session.loggedin is True:
            username = app.session.username
            privilege = app.session.privilege
            params = {}
            params['username'] = username
            params['privilege'] = privilege
        else:
            params = {}
            params['username'] = 'anonymous'
            params['privilege'] = '-1'

        return config.render.notfound(params)
