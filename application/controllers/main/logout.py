import application.controllers.main.config as config
import app


class Logout:
    def __init__(self):
        pass

    @staticmethod
    def GET():
        if app.ssl == True:
            config.validate_https() # validate HTTPS connection
        app.session.username = 'anonymous'
        app.session.privilege = -1
        app.session.kill()
        raise config.web.seeother('/')
