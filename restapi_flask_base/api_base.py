from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Helloworld(Resource):
    def get(self):
        return {'data':'Hello, World!'}

class Helloname(Resource):
    def get(self, name):
        return {'data':'Hello, {}'.format(name)}

api.add_resource(Helloworld,'/helloworld')
api.add_resource(Helloname,'/helloworld/<string:name>')

if __name__ == '__main__':
    app.run(debug=True,port=8000)
