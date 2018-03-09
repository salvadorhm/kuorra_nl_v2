"""
    Class for show a user detail
"""
import application.controllers.main.config as config
import app


class Profile:
    def __init__(self):
        pass

    def GET(self):
        if app.session.loggedin is True: # validate if the user is logged
            return self.GET_PROFILE() # call GET_PROFILE() function
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_PROFILE():
        session_username = config.check_secure_val(app.session.username) # get the session_username
        session_privilege = int(config.check_secure_val(app.session.privilege)) # get the session_privilege
        params = {}
        params['username'] = session_username
        params['privilege'] = session_privilege
        result = config.model_users.get_users(session_username)  # search for the user data
        return config.render.profile(params, result) # render view.html with user data
