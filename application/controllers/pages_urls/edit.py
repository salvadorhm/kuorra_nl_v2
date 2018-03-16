import application.controllers.pages_urls.config as config
import hashlib
import app
import time
import datetime


class Edit:
    
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
                return self.GET_EDIT(id_page_url) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_page_url, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = config.check_secure_val(app.session.username) # get the session_username
            session_privilege = int(config.check_secure_val(app.session.privilege)) # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(id_page_url) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html


    @staticmethod
    def GET_EDIT(id_page_url, **k):
        message = None # Error message
        id_page_url = config.check_secure_val(str(id_page_url)) # HMAC id_page_url validate
        result = config.model_pages_urls.get_pages_urls(int(id_page_url)) # search for the id_page_url
        result.id_page_url = config.make_secure_val(str(result.id_page_url)) # apply HMAC for id_page_url
        return config.render.edit(result, message) # render pages_urls edit.html

    @staticmethod
    def POST_EDIT(id_page_url, **k):
        form = config.web.input()  # get form data
        form['id_page_url'] = config.check_secure_val(str(form['id_page_url'])) # HMAC id_page_url validate
        # edit user with new data
        result = config.model_pages_urls.edit_pages_urls(
            form['id_page_url'],
            form['user_np'],
            form['get_url'],
            form['post_url'],
            form['controller'],
            form['c_view'],
            form['url_full']
        )
        if result == None: # Error on udpate data
            id_page_url = config.check_secure_val(str(id_page_url)) # validate HMAC id_page_url
            result = config.model_pages_urls.get_pages_urls(int(id_page_url)) # search for id_page_url data
            result.id_page_url = config.make_secure_val(str(result.id_page_url)) # apply HMAC to id_page_url
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/pages_urls') # render pages_urls index.html
