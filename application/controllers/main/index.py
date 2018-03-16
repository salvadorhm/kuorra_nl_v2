import application.controllers.main.config  as config
import app
import web
import time
import datetime


class Index:
    
    def __init__(self):
        pass

    @staticmethod
    def GET():
        if app.ssl == True:
            config.validate_https() # validate HTTPS connection

        if app.session.loggedin is True:
            # get now time
            now = datetime.datetime.now()
            now_str = str(now).split('.')[0]

            expires = config.check_secure_val(app.session.expires)

            print "now    : " , now_str
            print "expires: " , expires

            expires = config.check_secure_val(app.session.expires)

            if (now_str > expires): # compare now with time login
                raise config.web.seeother('/logout')

            session_username = config.check_secure_val(app.session.username) # get the session_username
            session_privilege = int(config.check_secure_val(app.session.privilege)) # get the session_privilege
            params = {}
            params['username'] = session_username
            params['privilege'] = session_privilege
            if session_privilege == 0:
                return config.render.admin(params)
            elif session_privilege == 1:
                return config.render.guess(params)
        else:
            params = {}
            params['username'] = 'anonymous'
            params['privilege'] = '-1'
            return config.render.index(params)
