import application.controllers.productos.config as config
import hashlib
import app

class Index:
    
    def __init__(self):
        pass
    
    def GET(self):
        if app.ssl is True:
            config.validate_https() # validate HTTPS connection
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = config.check_secure_val(app.session.username) # get the session_username
            session_privilege = int(config.check_secure_val(app.session.privilege)) # get the session_privilege
            
            access = config.model_pages_urls.get_pages_urls_access(session_privilege,"productos","index")
            if access != None:
                if access.get_url == 1: # access True
                    return self.GET_INDEX() # call GET_INDEX() function
                elif access.get_url == 0: # access False
                    raise config.web.seeother('/') # rendner guess.html
            else:
                raise config.web.seeother('/') # rendner guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_INDEX():
        result = config.model_productos.get_all_productos().list() # get productos table list
        for row in result:
            row.id_producto = config.make_secure_val(str(row.id_producto)) # apply HMAC to id_producto (primary key)
        return config.render.index(result) # render productos index.html
