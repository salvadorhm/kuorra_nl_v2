import application.controllers.productos.config as config
import hashlib
import app


class View:

    def __init__(self):
        pass

    def GET(self, id_producto):
        if app.ssl == True:
            config.validate_https() # validate HTTPS connection
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = config.check_secure_val(app.session.username) # get the session_username
            session_privilege = int(config.check_secure_val(app.session.privilege)) # get the session_privilege
            
            access = config.model_pages_urls.get_pages_urls_access(session_privilege,"productos","view")
            if access != None:
                if access.get_url == 1: # access True
                    return self.GET_VIEW(id_producto) # call GET_VIEW() function
                elif access.get_url == 0: # access False
                    raise config.web.seeother('/') # render guess.html
            else:
                raise config.web.seeother('/') # render index.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_VIEW(id_producto):
        id_producto = config.check_secure_val(str(id_producto)) # HMAC id_producto validate
        result = config.model_productos.get_productos(id_producto) # search for the id_producto data
        return config.render.view(result) # render view.html with id_producto data
