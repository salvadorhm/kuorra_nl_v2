import application.controllers.productos.config as config
import hashlib
import app

class Insert:

    def __init__(self):
        pass

    def GET(self, **k):
        if app.ssl == True:
            config.validate_https() # validate HTTPS connection
        if app.session.loggedin is True:
            
            # session_username = config.check_secure_val(app.session.username) # get the session_username
            session_privilege = int(config.check_secure_val(app.session.privilege)) # get the session_privilege
            
            access = config.model_pages_urls.get_pages_urls_access(session_privilege,"productos","insert")
            if access != None:
                if access.get_url == 1: # access True
                    return self.GET_INSERT() # call GET_INSERT() function
                elif access.get_url == 0: # access False
                    raise config.web.seeother('/') # render guess.html
            else:
                raise config.web.seeother('/') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, **k):
        if app.ssl == True:
            config.validate_https() # validate HTTPS connection
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = config.check_secure_val(app.session.username) # get the session_username
            session_privilege = int(config.check_secure_val(app.session.privilege)) # get the session_privilege
            
            access = config.model_pages_urls.get_pages_urls_access(session_privilege,"productos","insert")
            if access != None:
                if access.post_url == 1: # access True
                    return self.POST_INSERT() # call POST_EDIT function
                elif access.post_url == 0: # access False
                    raise config.web.seeother('/') # render guess.html
            else:
                raise config.web.seeother('/') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_INSERT(**k):
        message = None
        return config.render.insert(message) # render insert.html

    @staticmethod
    def POST_INSERT(**k):
        form = config.web.input() # get form data
        # call model insert_productos and try to insert new data
        result = config.model_productos.insert_productos(
            form['producto'],
            form['existencias'],
            form['precio'],
        )
        if type(result) == long:
            message = "Insert succefull!!"
        else:
            message = "Error: check values!!!"
        return config.render.insert(message) # render insert.html
