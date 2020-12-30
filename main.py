from flask import Flask, jsonify, render_template,request
from flask_cors import CORS
from flask_restful import Api, Resource, reqparse
import mysql_connector as sql
app = Flask(__name__, static_folder="dist/static", template_folder="dist")
CORS(app)
api = Api(app)

conn = sql.start_connection()
cur = sql.create_table(conn,"task_table")


parser = reqparse.RequestParser() 
parser.add_argument('id', type=str) 
parser.add_argument('task_name', type=str)
parser.add_argument('is_check', type=str) 
#get, post, put, deleteリクエストがあったときの処理をそれぞれ書く
class test(Resource):
    #parser = reqparse.RequestParser()
    # add_argumentでパラメータを取得できます
    # この辺はflask_restfulの公式ドキュメントに色々乗ってるのでそっち見た方がよさげ
    #parser.add_argument("message")
    def get(self):
        return sql.select(cur)
    def post(self):
        args = parser.parse_args()
        print(args.values()) 
        #insert(cur)
api.add_resource(test, "/api")


#@app.route('/', defaults={'path': ''})
@app.route('/')
def get_vue():
    return render_template('index.html')


if __name__ == "__main__":
    app.run( debug=True, host='0.0.0.0')