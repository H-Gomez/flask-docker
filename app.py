from flask import Flask

# Creates a Flask application named app.
app = Flask(__name__)

# A route which will display the welcome message via a HTML template
@app.route('/')
def hello_world():
    message = 'Server working...'
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')