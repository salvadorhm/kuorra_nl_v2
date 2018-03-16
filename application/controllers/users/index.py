"""
    Class for show the users list
"""
import application.controllers.users.config as config
import app
import time
import datetime


class Index:
    def __init__(self):
        pass

    def GET(self):
        if app.session.loggedin is True: # validate if the user is logged
            # get now time
            now = datetime.datetime.now()
            now_str = str(now).split('.')[0]

            expires = config.check_secure_val(app.session.expires)

            print "now    : " , now_str
            print "expires: " , expires

            expires = config.check_secure_val(app.session.expires)

            if (now_str > expires): # compare now with time login
                raise config.web.seeother('/logout')

            # session_username = config.check_secure_val(app.session.username) # get the session_username
            session_privilege = int(config.check_secure_val(app.session.privilege)) # get the session_privilege 
            if session_privilege == 0: # admin user
                return self.GET_INDEX() # call GET_INDEX() function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # rendner guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_INDEX():
        result = config.model_users.get_all_users().list() # get users table list
        for row in result: 
            row.username = config.make_secure_val(str(row.username)) # apply HMAC to username (primary key)
        return config.render.index(result) # render index.html
