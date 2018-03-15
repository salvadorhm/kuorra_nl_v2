"""
    Class for show a user detail
"""
import application.controllers.users.config as config
import app



class View:
    def __init__(self):
        pass

    def GET(self, username):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = config.check_secure_val(app.session.username) # get the session_username
            session_privilege = int(config.check_secure_val(app.session.privilege)) # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_VIEW(username) # call GET_VIEW() function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_VIEW(username):
        username = config.check_secure_val(str(username)) # HMAC username validate
        result = config.model_users.get_users(username)  # search for the user data
        return config.render.view(result) # render view.html with user data