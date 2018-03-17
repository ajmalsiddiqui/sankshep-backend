'''
This contains the Flask server-side code for the application
'''

# Summarization services
from services.summarizers import gensimTextRank
from services.scrapers import getCaptionText, addStops

from flask import Flask, request, json

app = Flask(__name__)

@app.route('/')
def hello():
	return "Hello"

@app.route('/summarize', methods = ['POST'])
def summarize():
	data = request.get_json()
	text = data['text']
	title = data['title']
	summary = gensimTextRank(text, title)
	response = {
		'summary': summary
	}
	return json.dumps(response)

@app.route('/youtube', methods = ['POST'])
def summarize_youtube():
	data = request.get_json()
	youtube_url = data['url']
	# content = getCaptionText(youtube_url)
	content = addStops(getCaptionText(youtube_url))
	# print(content)
	summary = gensimTextRank(content, 'dummy')
	response = {
		'summary': summary
	}
	return json.dumps(response)



print(__name__)
if __name__ == "__main__":
	app.run(debug=True)