'''
How use the API

user_hash is the user_hash for one user

Get all tables row -> action=get
http://localhost:8080/api_table_name?user_hash=XXXX&action=get

GET one table row -> action=get
http://localhost:8080/api_table_name?user_hash=XXXX&action=get&primary_key=X

DELETE one row -> action=delete
http://localhost:8080/api_table_name?user_hash=XXXX&action=delete&primary_key=X

UPDATE one row -> action=update
http://localhost:8080/api_table_name?user_hash=XXXX&action=put&primary_key=X&field1=XX&field2=XX..

INSERT onw row -> action=put
http://localhost:8080/api_table_name?user_hash=XXXX&action=put&field1=XX&field2=XX...

'''
import web
import application.api.productos.config
import json
import application.models.model_users as model_users


class Api_productos:
    def __init__(self):
        pass
        
    def get(self, id_producto):
        try:
            # GET all table rows
            if id_producto is None:
                result = config.model_productos.get_all_productos()
                data = []
                for row in result:
                    tmp = dict(row)
                    data.append(tmp)
                web.header('Content-Type', 'application/json')
                response = {"result":[{"status":200}],"data":data}
                return json.dumps(response, ensure_ascii=False).encode('utf8')
            else:
            # GET one table row
                result = config.model_productos.get_productos(int(id_producto))
                data = []
                data.append(dict(result))
                response = {"result":[{"status":200}],"data":data}
                web.header('Content-Type', 'application/json')
                return json.dumps(response, ensure_ascii=False).encode('utf8')
        except Exception as e:
            print "GET Error {}".format(e.args)
            e = str(e.args)
            e = e.strip('(\"')
            e = e.strip('\",)')
            response = {"result":[{"status":400,"error":e}],"data":[]}
            web.header('Content-Type', 'application/json')
            return json.dumps(response, ensure_ascii=False).encode('utf8')

    # INSERT row 
    def put(self, producto,existencias,precio):
        try:
            result = config.model_productos.insert_productos(producto,existencias,precio)
            response = {}
            if  isinstance(result,long):
                response = {"result":[{"status":200}],"data":[]}
            else:
                response = {"result":[{"status":400,"error":result}], "data":[]}
            web.header('Content-Type', 'application/json')
            return json.dumps(response, ensure_ascii=False).encode('utf8')
        except Exception as e:
            print "result".format(e.args)
            response = {"result":[{"status":400,"error":e.args}],"data":[]}
            web.header('Content-Type', 'application/json')
            return json.dumps(response, ensure_ascii=False).encode('utf8')

    # DELETE row
    def delete(self, id_producto):
        try:
            result = config.model_productos.delete_productos(id_producto)
            response = {}
            if result == 1:
                response = {"result":[{"status":200}],"data":[]}
            else:
                response = {"result":[{"status":400,"error":"not deleted"}],"data":[]}
            web.header('Content-Type', 'application/json')
            return json.dumps(response, ensure_ascii=False).encode('utf8')
        except Exception as e:
            print "DELETE Error {}".format(e.args)
            response = {"result":[{"status":400,"error":e.args}],"data":[]}
            web.header('Content-Type', 'application/json')
            return json.dumps(response, ensure_ascii=False).encode('utf8')

    # UPDATE one row 
    def update(self, id_producto, producto,existencias,precio):
        try:
            result = config.model_productos.edit_productos(id_producto,producto,existencias,precio)
            response = {}
            if result == 1:
                response = {"result":[{"status":200}],"data":[]}
            else:
                response = {"result":[{"status":400,"error":"not updated"}],"data":[]}
            web.header('Content-Type', 'application/json')
            return json.dumps(response, ensure_ascii=False).encode('utf8')
        except Exception as e:
            print "UPDATE Error {}".format(e.args)
            response = {"result":[{"status":400,"error":e.args}],"data":[]}
            web.header('Content-Type', 'application/json')
            return json.dumps(response, ensure_ascii=False).encode('utf8')

    def GET(self):
        user_data = web.input(
            user_hash=None,
            action=None,
            id_producto=None,
            producto=None,
            existencias=None,
            precio=None,
        )
        try:
            user_hash = user_data.user_hash  # user validation
            action = user_data.action  # action GET, PUT, DELETE, UPDATE
            id_producto=user_data.id_producto
            producto=user_data.producto
            existencias=user_data.existencias
            precio=user_data.precio
            user_hash = model_users.get_user_hash(user_hash) # validate user_hash
            
            if user_hash != None: # search user_hash 
                if user_hash.api_access == 1: # check api_access enable/disable
                    if action is None:
                        web.header('Content-Type', 'application/json')
                        response = {"result":[{"status":400,"error":"not action founded"}], "data":[]}
                        return json.dumps(response, ensure_ascii=False).encode('utf8')
                    elif action == 'get':
                        return self.get(id_producto)
                    elif action == 'put':
                        return self.put(producto,existencias,precio)
                    elif action == 'delete':
                        return self.delete(id_producto)
                    elif action == 'update':
                        return self.update(id_producto, producto,existencias,precio)
                else:
                    web.header('Content-Type', 'application/json')
                    response = {"result":[{"status":400,"error":"user_hash disabled"}], "data":[]}
                    return json.dumps(response, ensure_ascii=False).encode('utf8')
            else:
                web.header('Content-Type', 'application/json')
                response = {"result":[{"status":400,"error":"user_hash not found"}], "data":[]}
                return json.dumps(response, ensure_ascii=False).encode('utf8')
        except Exception as e:
            print "WEBSERVICE Error {}".format(e.args)
            e = str(e.args)
            e = e.strip('(\"')
            e = e.strip('\",)')
            web.header('Content-Type', 'application/json')
            response = {"result":[{"status":400,"error":e}],"data":[]}
            return json.dumps(response, ensure_ascii=False).encode('utf8')
