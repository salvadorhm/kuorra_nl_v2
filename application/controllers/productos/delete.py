import application.controllers.productos.config as config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    def GET(self, id_producto, **k):
        if app.ssl == True:
            config.validate_https() # validate HTTPS connection
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = config.check_secure_val(app.session.username) # get the session_username
            session_privilege = int(config.check_secure_val(app.session.privilege)) # get the session_privilege
            
            access = config.model_pages_urls.get_pages_urls_access(session_privilege,"productos","delete")
            if access != None:
                if access.get_url == 1: # Access True
                    return self.GET_DELETE(id_producto) # call GET_DELETE function
                elif access.get_url == 0: # Acess False
                    raise config.web.seeother('/') # render guess.html
            else:
                raise config.web.seeother('/') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, id_producto, **k):
        if app.ssl == True:
            config.validate_https() # validate HTTPS connection
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = config.check_secure_val(app.session.username) # get the session_username
            session_privilege = int(config.check_secure_val(app.session.privilege)) # get the session_privilege
            
            access = config.model_pages_urls.get_pages_urls_access(session_privilege,"productos","delete")
            if access != None:
                if access.post_url == 1: # access True
                    return self.POST_DELETE(id_producto) # call POST_DELETE function
                elif access.post_url == 0: # access False
                    raise config.web.seeother('/') # render guess.html
            else:
                raise config.web.seeother('/') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(id_producto, **k):
        message = None # Error message
        id_producto = config.check_secure_val(str(id_producto)) # HMAC id_producto validate
        result = config.model_productos.get_productos(int(id_producto)) # search  id_producto
        result.id_producto = config.make_secure_val(str(result.id_producto)) # apply HMAC for id_producto
        return config.render.delete(result, message) # render delete.html with user data

    @staticmethod
    def POST_DELETE(id_producto, **k):
        form = config.web.input() # get form data
        form['id_producto'] = config.check_secure_val(str(form['id_producto'])) # HMAC id_producto validate
        result = config.model_productos.delete_productos(form['id_producto']) # get productos data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            id_producto = config.check_secure_val(str(id_producto))  # HMAC user validate
            id_producto = config.check_secure_val(str(id_producto))  # HMAC user validate
            result = config.model_productos.get_productos(int(id_producto)) # get id_producto data
            result.id_producto = config.make_secure_val(str(result.id_producto)) # apply HMAC to id_producto
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/productos') # render productos delete.html 
