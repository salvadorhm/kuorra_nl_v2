import web
import app

db = app.db


def get_all_productos():
    try:
        return db.select('productos')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_productos(id_producto):
    try:
        return db.select('productos', where='id_producto=$id_producto', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_productos(id_producto):
    try:
        return db.delete('productos', where='id_producto=$id_producto', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_productos(producto,existencias,precio):
    try:
        return db.insert('productos',producto=producto,
existencias=existencias,
precio=precio)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return e.args


def edit_productos(id_producto,producto,existencias,precio):
    try:
        return db.update('productos',id_producto=id_producto,
producto=producto,
existencias=existencias,
precio=precio,
                  where='id_producto=$id_producto',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
