"""
    File for config the tables models and use HMAC
"""
import application.models.model_users as model_users
import web
import hmac

render = web.template.render('application/views/users/', base='master')

secret_key = "kuorra_key"


def hash_str(s):
    return hmac.new(secret_key, s).hexdigest()


def make_secure_val(s):
    return "%s!%s" % (s, hash_str(s))


def check_secure_val(h):
    val = h.split('!')[0]
    if h == make_secure_val(val):
        return val
