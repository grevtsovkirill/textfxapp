import base64

from flask import Flask, request, jsonify, make_response
from flask_cors import CORS

# configuration
DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

VAR = ''

@app.route("/", methods=['GET','POST'])
def hello():
    global VAR
    response_object = {'status': 'success'}
    if request.method == 'POST':
        data = request.get_data()
        msg = data.decode("utf-8")
        var = msg + " - 1"
        VAR = var
        print(var)
    else:
        response_object['txt'] = VAR
    print(response_object)
    return response_object

@app.route('/upload', methods=['GET','POST'])
def uploadImage():
    if request.method == 'POST':
        base64_png =  request.form['image']
        code = base64.b64decode(base64_png.split(',')[1])
        image_decoded = Image.open(BytesIO(code))
        image_decoded.save(Path(app.config['UPLOAD_FOLDER']) / 'image.png')
        return make_response(jsonify({'result': 'success'}))
    else:
        return make_response(jsonify({'result': 'invalid method'}), 400)

if __name__ == "__main__":
    app.run()
