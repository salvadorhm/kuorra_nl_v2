import application.controllers.logs.config as config
import app


class View:
    
    def __init__(self):
        pass

    def GET(self, username):
        if app.session.loggedin is True:
            # session_username = config.check_secure_val(app.session.username) # get the session_username
            session_privilege = int(config.check_secure_val(app.session.privilege)) # get the session_privilege
            if session_privilege == 0:
                return self.GET_VIEW(username)
            elif session_privilege == 1:
                raise config.web.seeother('/guess')
        else:
            raise config.web.seeother('/login')

    @staticmethod
    def GET_VIEW(username):
        username = config.check_secure_val(str(username))
        result = config.model_users.get_users(username)
        return config.render.view(result)
