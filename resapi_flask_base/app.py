from flask import Flask
from flask_restful import Resource, Api, reqparse, abort


app = Flask(__name__)
api = Api(app)
#^ Tasks store in dictionary
todos = {
      1: {"tasks":"1 Write Hello World","Summery":"write the code using python."},
      2: {"tasks":"2 Write Hello World","Summery":"write the code using python."},
      }
#^ Set config for Post request
#* A file or directory can contain a reparse point, which is a collection of user-defined data. The format of this data is understood by the application which stores the data, and a file system filter
task_post_args = reqparse.RequestParser()
task_post_args.add_argument("tasks",type=str,help="Tasks is required",required=True)
task_post_args.add_argument("Summery",type=str,help="Summery is required",required=True)

#^ print all data
class TodoList(Resource):
    def get(self):
        return todos

#^ Print data by id
class Todo(Resource):
  #! get data by id
    def get(self, todo_id):
        return todos[todo_id]
  #! post data by id   
    def post(self,todo_id):
        args = task_post_args.parse_args()
        if todo_id in todos:
            abort(409, "Task ID already taken")
        todos[todo_id] = {"tasks": args["tasks"],"Summery":args["Summery"] } 
        return todos[todo_id]

api.add_resource(Todo, '/todos/<int:todo_id>')
api.add_resource(TodoList,'/todos/')
if __name__ == '__main__':
         app.run(debug=True)
