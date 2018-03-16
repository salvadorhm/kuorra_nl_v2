import application.controllers.pages_urls.config as config
import hashlib
import app
import time
import datetime


class Delete:
    
    def __init__(self):
        pass

    def GET(self, id_page_url, **k):
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
                return self.GET_DELETE(id_page_url) # call GET_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_page_url, **k):
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
                return self.POST_DELETE(id_page_url) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html
    
    @staticmethod
    def GET_DELETE(id_page_url, **k):
        message = None # Error message
        id_page_url = config.check_secure_val(str(id_page_url)) # HMAC id_page_url validate
        result = config.model_pages_urls.get_pages_urls(int(id_page_url)) # search  id_page_url
        result.id_page_url = config.make_secure_val(str(result.id_page_url)) # apply HMAC for id_page_url
        return config.render.delete(result, message) # render delete.html with user data

    @staticmethod
    def POST_DELETE(id_page_url, **k):
        form = config.web.input() # get form data
        form['id_page_url'] = config.check_secure_val(str(form['id_page_url'])) # HMAC id_page_url validate
        result = config.model_pages_urls.delete_pages_urls(form['id_page_url']) # get pages_urls data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            id_page_url = config.check_secure_val(str(id_page_url))  # HMAC user validate
            id_page_url = config.check_secure_val(str(id_page_url))  # HMAC user validate
            result = config.model_pages_urls.get_pages_urls(int(id_page_url)) # get id_page_url data
            result.id_page_url = config.make_secure_val(str(result.id_page_url)) # apply HMAC to id_page_url
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/pages_urls') # render pages_urls delete.html 
