import application.controllers.main.config as config
import app
import hashlib
import web
import time
import datetime


class Login:
    def __init__(self):
        pass

    @staticmethod
    def GET(*a):
        if app.ssl == True:
            config.validate_https() # validate HTTPS connection
            
        message = None
        return config.render.login(message)

    @staticmethod
    def POST(*a):
        i = config.web.input()
        pwdhash = hashlib.md5(i.password + config.secret_key).hexdigest()
        check = config.model_users.validate_user(i.username, pwdhash)
        if check:
            app.session.loggedin = True
            app.session.username = config.make_secure_val(check['username'])
            app.session.privilege = config.make_secure_val(str(check['privilege']))
            # get time now and N minutes
            now = datetime.datetime.now()
            future = now + datetime.timedelta(minutes = app.expires)
            future_str = str(future).split('.')[0]
            app.session.expires = config.make_secure_val(future_str)

            change_pwd = check['change_pwd']
            ip = web.ctx['ip']
            result = config.model_logs.insert_logs(check['username'], ip)
            if result == None:
                print "Error in log"

            if check['status'] == 0:
                message = "User account disabled!!!!"
                return config.render.login(message)
            elif change_pwd == 1:
                raise config.web.seeother('/users/change_pwd')
            else:
                raise config.web.seeother('/')
        else:
            message = "User or Password are not correct!!!!"
            return config.render.login(message)
