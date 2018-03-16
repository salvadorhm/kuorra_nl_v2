import application.controllers.pages_urls.config as config
import hashlib
import app
import time
import datetime


class View:

    def __init__(self):
        pass

    def GET(self, id_page_url):
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
                return self.GET_VIEW(id_page_url) # call GET_VIEW() function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_VIEW(id_page_url):
        id_page_url = config.check_secure_val(str(id_page_url)) # HMAC id_page_url validate
        result = config.model_pages_urls.get_pages_urls(id_page_url) # search for the id_page_url data
        return config.render.view(result) # render view.html with id_page_url data
