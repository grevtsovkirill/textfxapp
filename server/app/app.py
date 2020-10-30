from flask import Flask, request, jsonify
from flask_cors import CORS

# configuration
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


@app.route("/", methods=['GET','POST'])
def hello():
    data = request.data
    return data

    # return "Hello, World!"


if __name__ == "__main__":
    app.run()
