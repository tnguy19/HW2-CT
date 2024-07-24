from flask import Flask, jsonify, make_response
import os
import time
from flask import request


app = Flask(__name__)

@app.route('/')
def hello():
    response = make_response(
        {
            'response': 'Hello, World!',
            'status': 200
        }
    )
    return response

@app.route('/repeat')
def repeat():
        input_val = request.args.get('input', '')
        return jsonify(
                response=input_val,
                status = 200
        )
    
@app.route('/health')
@app.route('/healthcheck')
def health():
        return jsonify(body='OK',
        status=200)

@app.route('/hang')
def hang():
        while True:
                time.sleep(1)

if __name__ == '__main__':
    # By default flask is only accessible from localhost.
    # Set this to '0.0.0.0' to make it accessible from any IP address
    # on your network (not recommended for production use)
    app.run(host='0.0.0.0', port = os.getenv('PORT'), debug=True, threaded=False)


