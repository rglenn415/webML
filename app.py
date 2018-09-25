import sys
from flask import (Flask,render_template,jsonify,request)
from ML import model


app = Flask(__name__, template_folder = "./views")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/postData', methods=['POST'])
def process_data():
    print(request.json['selectedFeature'], file=sys.stdout)
    model(request.json)
    return jsonify({})

if __name__ == '__main__':
    app.run(debug = True)