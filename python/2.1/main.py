from flask import Flask
from flask_restful import Resource, Api, reqparse, abort

from db import db

app = Flask(__name__)
api = Api(app)

def non_empty_string(s):
    # ensures variable is of type string and that it is not empty
    if not isinstance(s, str):
        raise ValueError('Must be of type string.')
    if not s:
        raise ValueError('String cannot be empty.')
    return s

parser_add = reqparse.RequestParser(bundle_errors=True)
parser_add.add_argument('task', required=True, type=non_empty_string, help='{error_msg}')
parser_add.add_argument('done', required=True, choices=(0, 1), type=int, help='Bad choice: {error_msg}.')

parser_update = reqparse.RequestParser()
parser_update.add_argument('task', required=False, type=non_empty_string, help='{error_msg}')
parser_update.add_argument('done', required=False, choices=(0, 1), type=int, help='Bad choice: {error_msg}.')

def unknown_id(id):
    abort(404, message=f'No task with id {id}.')

class Mock(Resource):
    def get(self):
        """ Resets database to the initial state.
        """
        db.mock()
        return {'status': 'done'}

class ShowAall(Resource):
    def get(self):
        """ Returns all tasks.
        """
        res = db.show(None)
        return {'message': res}

    def post(self):
        """ Adds new task.
        """
        args = parser_add.parse_args()
        id = db.add(args.task, args.done)
        return ({'message': f'Task added with id {id}.'}, 201)

class Task(Resource):
    def delete(self, task_id):
        """ Delete single task.
        """
        res = db.delete(task_id)
        if res:
            unknown_id(task_id)
        else:
            return {'message': 'Deleted'}

    def get(self, task_id: int):
        """ Returns single task.
        """
        res = db.show(task_id)
        if res[0] is None:
            unknown_id(task_id)
        else:
            return {'message': res}

    def put(self, task_id: int):
        """ Updates existing task.
        """
        args = parser_update.parse_args()
        res = db.update(task_id, args)
        if res == -1:
            unknown_id(task_id)
        elif res == -2:
            return ({'message': 'No information for update'}, 204)
        else:
            return {'message': f'Task {task_id} updated.'}

api.add_resource(Mock, '/mock')
api.add_resource(ShowAall, '/tasks')
api.add_resource(Task, '/tasks/<task_id>')

if __name__ == '__main__':
    # as this is a recruitement task i leave debug for visibility
    app.run(debug=True, host='0.0.0.0')