import web
import hmac
import application.models.model_logs as model_logs
import application.models.model_users as model_users
import app

render = web.template.render('application/views/logs/', base='master')

secret_key = app.secret_key


def hash_str(s):
    return hmac.new(secret_key, s).hexdigest()


def make_secure_val(s):
    return "%s!%s" % (s, hash_str(s))


def check_secure_val(h):
    val = h.split('!')[0]
    if h == make_secure_val(val):
        return val
        