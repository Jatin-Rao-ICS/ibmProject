from typing import Dict
from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
import uuid
from nltk_model import get_endpoint

app = Flask(__name__)
api = Api(app)

# id = uuid.uuid1()
# #id = id.hex[0:2]
# print(id)

data = "As a user, I want to identify persons in videos, and receive related information about them."
PROJECT = get_endpoint(data,"swagger(6).yaml")

# PROJECT = {
#   '1': {'name': 'name', 'desc': 'desc', 'story': 'story'},
# }
# print(PROJECT)
print(PROJECT)
parser = reqparse.RequestParser()

class Project(Resource):
      def post(self):
        parser.add_argument("name")
        parser.add_argument("desc")
        args = parser.parse_args()
        project_id = int(max(PROJECT.keys())) + 1
        project_id = '%i' % project_id
        PROJECT[project_id] = {
          "name": args["name"],
          "desc": args["desc"],
        }
        return PROJECT[project_id], 201

        # if request.method == 'POST':
        #     params = request.json
        #     projectId = params['projectId']

class ProjectID(Resource):
      def get(self, project_id):
          if project_id not in PROJECT:
            return "Not found", 404
          else:
            return PROJECT[project_id]   

class UserStory(Resource):
      def post(self, project_id):
        parser.add_argument("story")
        args = parser.parse_args()
        project_id = int(max(PROJECT.keys())) + 1
        project_id = '%i' % project_id
        PROJECT[project_id] = {
          "story": args["story"],
        }
        return PROJECT[project_id], 201      

      def get(self, project_id):
          if project_id not in PROJECT:
            return "Not found", 404
          else:
            return PROJECT[project_id] 

class TestCases(Resource):
      def get(self, project_id):
          if project_id not in PROJECT:
            return "Not found", 404
          else:
            data = "These are all the testcase ids"
            return jsonify({'data': data})

api.add_resource(Project, '/project/')
api.add_resource(ProjectID, '/project/<project_id>')
api.add_resource(UserStory, '/project/<project_id>/story/')
api.add_resource(TestCases, '/project/<project_id>/testCases/')

# if __name__ == "__main__":
#   app.run(debug=True)

# for endpoint in PROJECT:
#   print(endpoint)
  # print(PROJECT[endpoint][0])
  # print(PROJECT[endpoint][1])