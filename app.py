'''
This contains the Flask server-side code for the application
'''

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
	return "Hello"

print(__name__)
if __name__ == "__main__":
	app.run(debug=True)