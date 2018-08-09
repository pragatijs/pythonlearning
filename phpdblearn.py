import web
import json
import MySQLdb

urls = (
        "/","test",
        "/userdetails","username"
 )

db = web.database(dbn='mysql', user='root', pw='sumukh', db='dumbo')

class test:
    def GET(self):
        user_data=web.input()
        dbtable = db.query('select * from phythonuser where user_id=$id',vars={'id':user_data.idX})
        Dataarray=[]
        for row in dbtable:
            Dataarray.append({"id":row.user_id,"Name":row.user_name})
        return json.dumps(Dataarray)

class username:
    def GET(self):
        return "hello get"

    def POST(self):
        return "hello post"

    def PUT(self):
        return "hello put"


if __name__ == "__main__":
     app = web.application(urls, globals())
     app.run()
else:
     application = web.application(urls, globals()).wsgifunc()
