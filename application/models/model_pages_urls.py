import web
import app

db = app.db


def get_all_pages_urls():
    try:
        return db.select('pages_urls')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_pages_urls(id_page_url):
    try:
        return db.select('pages_urls', where='id_page_url=$id_page_url', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None

def get_pages_urls_access(user_np, controller, c_view):
    try:
        return db.select('pages_urls', where='user_np=$user_np and controller=$controller and c_view=$c_view', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None

def delete_pages_urls(id_page_url):
    try:
        return db.delete('pages_urls', where='id_page_url=$id_page_url', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_pages_urls(user_np,get_url,post_url,controller,c_view,url_full):
    try:
        return db.insert('pages_urls',user_np=user_np,
                        get_url=get_url,
                        post_url=post_url,
                        controller=controller,
                        c_view=c_view,
                        url_full=url_full)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_pages_urls(id_page_url,user_np,get_url,post_url,controller,c_view,url_full):
    try:
        return db.update('pages_urls',id_page_url=id_page_url,
                        user_np=user_np,
                        get_url=get_url,
                        post_url=post_url,
                        controller=controller,
                        c_view=c_view,
                        url_full=url_full,
                  where='id_page_url=$id_page_url',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
