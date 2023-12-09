from flask import Flask, request
from pymongo import MongoClient
import bleach

app = Flask(__name__)

# MongoDB setup
client = MongoClient('mongodb_uri')  # Replace 'mongodb_uri' with your MongoDB URI
db = client['your_database']  # Replace 'your_database' with your database name
tasks_collection = db['tasks']

@app.route('/')
def hello():
    return 'Hello, test!'

@app.route('/task', methods=['POST'])
def create_task():
    data = request.get_json()

    # Sanitize inputs
    date = bleach.clean(data.get('date'))
    time = bleach.clean(data.get('time'))
    objective = bleach.clean(data.get('objective'))
    tags = [bleach.clean(tag) for tag in data.get('tags', [])]

    # Construct the task document
    task_document = {
        "taskname": {
            "task date/time": f"{date} {time}",
            "task flags": tags,
            "task objectives": objective
        }
    }

    # Save the task document in MongoDB
    tasks_collection.insert_one(task_document)

    return 'Task created successfully'

if __name__ == '__main__':
    app.run()