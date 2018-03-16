import application.controllers.pages_urls.config as config
import hashlib
import app
import operator
import time
import datetime


class Insert:

    def __init__(self):
        pass

    def GET(self):
        if app.session.loggedin is True:
            # get now time
            now = datetime.datetime.now()
            now_str = str(now).split('.')[0]

            expires = config.check_secure_val(app.session.expires)

            print "now    : " , now_str
            print "expires: " , expires

            expires = config.check_secure_val(app.session.expires)

            if (now_str > expires): # compare now with time login
                raise config.web.seeother('/logout')

            # session_username = config.check_secure_val(app.session.username)
            session_privilege = int(config.check_secure_val(app.session.privilege))  # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_INSERT() # call GET_INSERT() function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = config.check_secure_val(app.session.username)
            session_privilege = int(config.check_secure_val(app.session.privilege)) # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_INSERT() # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_INSERT():
        tmp = list(app.urls)
        url = []
        pages = []
        for i in range(0,len(tmp),2):
            url.append(tmp[i].strip('(.+)'))

        for i in range(1,len(tmp),2):
            controller = tmp[i].split(".")[2]
            c_view = tmp[i].split(".")[3]

            pages.append(controller + "-" + c_view)
        
        x = dict(zip(url, pages))
        remove_urls = ["/", 
                    "/404", 
                    "/500",
                    "/login",
                    "/logout",
                    "/logs",
                    "/logs/printer",
                    "/logs/view/",
                    "/pages_urls",
                    "/pages_urls/delete/",
                    "/pages_urls/edit/",
                    "/pages_urls/view/",
                    "/pages_urls/insert",
                    "/profile",
                    "/users",
                    "/users/change_pwd",
                    "/users/delete/",
                    "/users/edit/",
                    "/users/insert",
                    "/users/printer",
                    "/users/view/"
                    ]
        
        for url in remove_urls:
            x.pop(url)

        sorted_x = sorted(x.items(), key=operator.itemgetter(0))
        return config.render.insert(sorted_x) # render insert.html

    @staticmethod
    def POST_INSERT():
        form = config.web.input() # get form data

        # call model insert_pages_urls and try to insert new data
        uri = form['url_full'].split('-')
        controller = uri[0]
        c_view = uri[1]
        config.model_pages_urls.insert_pages_urls(
            form['user_np'],
            form['get_url'],
            form['post_url'],
            controller,
            c_view,
            "/"+controller+"/"+c_view
        )
        raise config.web.seeother('/pages_urls') # render pages_urls index.html
