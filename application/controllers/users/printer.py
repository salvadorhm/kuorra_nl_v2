"""
    Class for show a users list for print
"""
import application.controllers.users.config as config
import app
import time
import datetime


class Printer:
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
                return self.GET_PRINTER() # call GET_PRINTER() function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else:# the user dont have logged
            raise config.web.seeother('/login')

    @staticmethod
    def GET_PRINTER():
        result = config.model_users.get_all_users().list() # get all users data
        for row in result: 
            row.username = config.make_secure_val(str(row.username)) # apply HMAC to username
        return config.render.printer(result) # render printer.html
