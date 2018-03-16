import application.controllers.pages_urls.config as config
import hashlib
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
        result = config.model_pages_urls.get_all_pages_urls().list() # get pages_urls table list
        for row in result:
            row.id_page_url = config.make_secure_val(str(row.id_page_url)) # apply HMAC to id_page_url (primary key)
        return config.render.index(result) # render pages_urls index.html
