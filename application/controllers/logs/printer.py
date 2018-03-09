import application.controllers.logs.config as config
import app


class Printer:

    def __init__(self):
        pass

    def GET(self):
        if app.session.loggedin is True:
            # session_username = config.check_secure_val(app.session.username) # get the session_username
            session_privilege = int(config.check_secure_val(app.session.privilege)) # get the session_privilege
            if session_privilege == 0:
                return self.GET_PRINTER()
            elif session_privilege == 1:
                raise config.web.seeother('/guess')
        else:
            raise config.web.seeother('/login')

    def GET_PRINTER(self):
        result = config.model_logs.get_all_logs().list()
        for row in result:
            row.username = config.make_secure_val(str(row.username))
        return config.render.printer(result)