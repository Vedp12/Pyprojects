# Exended and updated version of restapi
import os
from flask import Flask
from flask_restful import Resource, Api, marshal_with, reqparse, abort, fields
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

#! data base added with name of  sql.db
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, "misql.db")
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_PATH}"
db = SQLAlchemy(app)

#! DB model created 
class ToDoModel(db.Model):
    __tablename__ = "to_do_model"
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(200))
    summary = db.Column(db.String(500))
with app.app_context():from datetime import timedelta

   db.create_all()


#* A file or directory can contain a reparse point, which is a collection of user-defined data. The format of this data is understood by the application which stores the data, and a file system filter
#^ Set config for Post request
task_post_args = reqparse.RequestParser()
task_post_args.add_argument("task", type=str, help="Task is required", required=True)
task_post_args.add_argument("summary", type=str, help="Summary is required", required=True)

#^ Set config for update request
task_update_args = reqparse.RequestParser()
task_update_args.add_argument("task", type=str)
task_update_args.add_argument("summary", type=str)

resource_fields = {
        'id':fields.Integer,
        'task': fields.String,
    'summary':fields.String,
        }


#^ print all data
class TodoList(Resource):
    def get(self):
        tasks = ToDoModel.query.all()
        todos = {}
        for task in tasks:
            todos[task.id] = {"task": task.task, "summary": task.summary}
        return todos


#^ Fetch Data by id

class ToDo(Resource):
    #! get data by id
    @marshal_with(resource_fields)
    def get(self, todo_id):
        task = ToDoModel.query.filter_by(id=todo_id).first()
        if not task:
            abort(404, message="Could not find tasks with that id")
        return task
 

    #! post data by id   
    @marshal_with(resource_fields)
    def post(self,todo_id):
        args = task_post_args.parse_args()
        task = ToDoModel.query.filter_by(id=todo_id).first()
        if task:
            abort(409,message="Task id is taken")
        todo = ToDoModel(id=todo_id, task=args['task'], summary=args['summary'])
        db.session.add(todo)
        db.session.commit()
        return todo,201


    #! put data by id
    @marshal_with(resource_fields)    
    def put(self, todo_id):
        args = task_update_args.parse_args()
        task = ToDoModel.query.filter_by(id=todo_id).first()
        if not task:
            abort(404, message="Task does't exist, cannot update")
        if args['task']:
            task.task = args['task']
        if args['summary']:
            task.summary = args['summary']
        db.session.commit()
        return task

    #! delete data by id 
    def delete(self,todo_id):
        task = ToDoModel.query.filter_by(id=todo_id).first()
        if not task:
            abort(404, message="Task does not exist, cannot delete")
        db.session.delete(task)
        db.session.commit()
        return 'Tasks deleted', 204

api.add_resource(ToDo, '/todos/<int:todo_id>')
api.add_resource(TodoList,'/todos/')

if __name__ == '__main__':
         app.run(debug=True)
