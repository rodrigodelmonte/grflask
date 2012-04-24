import os
from flask import Flask
from flask import render_template
from flask import url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

with app.test_request_context():
    url_for('static', filename='style.css')

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
