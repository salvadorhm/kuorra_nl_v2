import web
import app
import hmac
import application.models.model_productos as model_productos
import application.models.model_pages_urls as model_pages_urls

render = web.template.render('application/views/productos/', base='master')

secret_key = "kuorra_key"


def hash_str(s):
    return hmac.new(secret_key, s).hexdigest()


def make_secure_val(s):
    return "%s!%s" % (s, hash_str(s))


def check_secure_val(h):
    val = h.split('!')[0]
    if h == make_secure_val(val):
        return val

def validate_https():
    if app.web.ctx.protocol == "http":
        dom = app.web.ctx.homedomain
        dom = dom.replace("http","https")
        dom += app.web.ctx.path
        raise app.web.seeother(dom)