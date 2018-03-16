import web
import hmac
import application.models.model_pages_urls as model_pages_urls
import app

render = web.template.render('application/views/pages_urls/', base='master')

secret_key = app.secret_key

def hash_str(s):
    return hmac.new(secret_key, s).hexdigest()


def make_secure_val(s):
    return "%s!%s" % (s, hash_str(s))


def check_secure_val(h):
    val = h.split('!')[0]
    if h == make_secure_val(val):
        return val
