from flask import Flask, request, jsonify,send_file,send_from_directory
import os
from werkzeug.utils import secure_filename
from werkzeug.datastructures import ImmutableDict
import json

app = Flask(__name__)

upload_folder= "uploads"

@app.route("/get/<id>", methods=["GET"])
def get_demo(id):
    print(id)
    print(request.args)
    print(request.args.get("demo"))
    return 'ok'

@app.route("/get/file/<filename>", methods=["GET"])
def get_file(filename):
    return send_from_directory("downloads",filename)

@app.route("/post/json", methods=["POST"])
def post_json():
    print(request.json) # json obj
    print(request.args) # [key-value]
    for k,v in request.args.items():
        print(f'{k}:{v}')
    return 'ok'

@app.route("/post/file", methods=["POST"])
def post_file():
    if 'json_data' in request.files:
        jsondata = json.load(request.files['json_data'])
        print(jsondata)

    if 'upload_file' in request.files:
        f = request.files['upload_file']
        filename = secure_filename(f.filename)
        f.save(os.path.join(upload_folder,filename))
    return 'ok'



if __name__ == "__main__":
    app.run(port=5001)