import application.controllers.productos.config as config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    def GET(self, id_producto, **k):
        if app.ssl == True:
            config.validate_https() # validate HTTPS connection
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = config.check_secure_val(app.session.username) # get the session_username
            session_privilege = int(config.check_secure_val(app.session.privilege)) # get the session_privilege

            access = config.model_pages_urls.get_pages_urls_access(session_privilege,"productos","edit")
            if access != None:
                if access.get_url == 1: # admin user
                    return self.GET_EDIT(id_producto) # call GET_EDIT function
                elif access.get_url == 0: # guess user
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
            
            access = config.model_pages_urls.get_pages_urls_access(session_privilege,"productos","edit")
            if access != None:
                if access.post_url == 1: # admin user
                    return self.POST_EDIT(id_producto) # call POST_EDIT function
                elif access.post_url == 0: # guess user
                    raise config.web.seeother('/') # render guess.html
            else:
                raise config.web.seeother('/') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_EDIT(id_producto, **k):
        message = None # Error message
        id_producto = config.check_secure_val(str(id_producto)) # HMAC id_producto validate
        result = config.model_productos.get_productos(int(id_producto)) # search for the id_producto
        result.id_producto = config.make_secure_val(str(result.id_producto)) # apply HMAC for id_producto
        return config.render.edit(result, message) # render productos edit.html

    @staticmethod
    def POST_EDIT(id_producto, **k):
        form = config.web.input()  # get form data
        form['id_producto'] = config.check_secure_val(str(form['id_producto'])) # HMAC id_producto validate
        # edit user with new data
        result = config.model_productos.edit_productos(
            form['id_producto'],form['producto'],form['existencias'],form['precio'],
        )
        if result == None: # Error on udpate data
            id_producto = config.check_secure_val(str(id_producto)) # validate HMAC id_producto
            result = config.model_productos.get_productos(int(id_producto)) # search for id_producto data
            result.id_producto = config.make_secure_val(str(result.id_producto)) # apply HMAC to id_producto
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/productos') # render productos index.html
