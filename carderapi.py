
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
        parama=int(param.a)
        paramb=int(param.b)
        print param.opt
        if param.opt=='+':
            return parama+paramb
        elif param.opt=='-':
            return parama-paramb
        elif param.opt=='x':
            return parama*paramb
        elif param.opt=='/':
            try:
                
                return parama / paramb

            except Exception as e:
                #return "Second value cannot be zero!"
                return e
        else:
            return "didnt understand the operand"+param.opt

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
