import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    msg = '<br/>'.join(
        '{}={}'.format(k, v)
        for k, v in sorted(os.environ.iteritems()))
    return msg

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
