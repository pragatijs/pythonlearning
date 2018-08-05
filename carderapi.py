
import json
import web
#from random import randint

urls = (
        "/add","add",
        "/minus","minus",
        "/div","divide",
        "/mul","multiply"
)

class add:
    def GET(self):
        param = web.input(a=10,b=9,opt='+')
        if param.opt=='+':
            return a+b
        elif param.opt=='-':
            return a-b
        elif opt=='x':
            return a*b
        elif opt=='/':
            if b!=0:
                return a/b
            else:
                return "Second value cannot be zero!"


        """a = 1
        b = 2
        c = a + b
        return c"""

class minus:
    def GET(self):
        a = 12
        b = 2
        c = a - b
        return c

class divide:
    def GET(self):
        a = 10
        b = 2
        c = a / b
        return c

class multiply:
    def GET(self):
        a = 1
        b = 2
        c = a * b
        return c



if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
else:
    application = web.application(urls, globals()).wsgifunc()
