from flask import Flask, request, jsonify
from flask_cors import CORS

# configuration
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

VAR = []

@app.route("/", methods=['GET','POST'])
def hello():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        data = request.get_data()
        msg = data.decode("utf-8")
        var = msg + " - 1"
        print(var)
        response_object['txt'] = var
    else:
        response_object['txt'] = '0'
    print(response_object)
    return response_object


if __name__ == "__main__":
    app.run()
