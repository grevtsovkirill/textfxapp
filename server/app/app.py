from flask import Flask, request, jsonify
from flask_cors import CORS

# configuration
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

TXT = [{
        'in_text': 'place text here'
    }]


@app.route("/", methods=['GET','POST'])
def hello():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        TXT.append({'in_text': post_data.get('in_text')})
    else:
        response_object['msg'] = TXT
    return jsonify(response_object)
    # return "Hello, World!"


if __name__ == "__main__":
    app.run()
