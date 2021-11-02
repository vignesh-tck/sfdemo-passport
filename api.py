from flask import Flask
from flask import request
from flask_restful import Resource, Api, reqparse
import boto3
import json
from genson import SchemaBuilder
import configparser

app = Flask(__name__)

@app.route('/')
def hello():
    return "hello world!"

@app.route('/get_schema')
def get(self):
    config = configparser.ConfigParser()
    config.read('Config.ini')
    s3 = boto3.resource(
    service_name='s3',
    region_name='us-east-2',
    aws_access_key_id=config['DEFAULT']['aws_access_key_id'],
    aws_secret_access_key=config['DEFAULT']['aws_secret_access_key']
    )
    doc_name = request.args.get('doc_name')
    content_object = s3.Object('claimsrepo', doc_name)
    file_content = content_object.get()['Body'].read().decode('utf-8')
    json_content = json.loads(file_content)
    builder = SchemaBuilder()
    builder.add_object(json_content)
    return builder.to_schema()


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
