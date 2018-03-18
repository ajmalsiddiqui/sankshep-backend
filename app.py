'''
This contains the Flask server-side code for the application
'''

# Summarization services
from services.summarizers import gensimTextRank
from services.scrapers import getCaptionText, addStops
from services.translate import translateSummary

from flask import Flask, request, json
from werkzeug import secure_filename
import os


# UPLOAD_FOLDER = '/tmp/'
UPLOAD_FOLDER = './files'
ALLOWED_EXTENSIONS = set(['txt', 'py', 'wav'])

# Utility function


def allowed_file(filename):
    print(filename)
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def hello():
    return "Hello"


@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.get_json()
    text = data['text']
    title = data['title']
    keywords, summary = gensimTextRank(text, title)
    response = {
        'summary': summary.replace('\n', '<br />'),
        'keywords': keywords,
        'status': 200
    }
    return json.dumps(response)


@app.route('/youtube', methods=['POST'])
def summarize_youtube():
    data = request.get_json()
    youtube_url = data['url']
    content = getCaptionText(youtube_url)
    if(len(content.split('. ')) < 10):
        content = addStops(content)
    # content = addStops(getCaptionText(youtube_url))
    # print(content)
    keywords, summary = gensimTextRank(content, 'dummy')
    response = {
        'summary': summary.replace('\n', '<br />'),
        'keywords': keywords,
        'status': 200
    }
    return json.dumps(response)


@app.route('/translate', methods=['POST'])
def translate():
    fail_resp = {
        'status': 400,
        'message': 'Ensure that text and lang arguments are provided in request'
    }
    data = request.get_json()
    if 'text' not in data or 'lang' not in data:
        return json.dumps(fail_resp)
    content = translateSummary(data['lang'], data['text'])
    succ_resp = {
        'content': content.replace('\n', '<br />'),
        'status': 200
    }
    return json.dumps(succ_resp)


@app.route("/txtfile", methods=['GET', 'POST'])
def index():
    print('hello')
    if request.method == 'POST':

        file = request.files['file']
        print("got file")
        if file and allowed_file(file.filename):
            print("saving")
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            with open('./files/' + filename, 'r') as f:
                content = f.read()
                keywords, summary = gensimTextRank(content, 'dummy')
                os.remove('./files/' + filename)

    # return """
    # <!doctype html>
    # <title>Upload new File</title>
    # <h1>Upload new File</h1>
    # <form action="" method=post enctype=multipart/form-data>
    #   <p><input type=file name=file>
    #      <input type=submit value=Upload>
    # </form>
    # <p>%s</p>
    # """ % "<br>".join(os.listdir(app.config['UPLOAD_FOLDER'],))

        succ_resp = {
            'status': 200,
            'keywords': keywords,
            'summary': summary.replace('\n', '<br />')
        }
        return json.dumps(succ_resp)

# Route doesn't work


@app.route('/audio', methods=['POST'])
def summarize_audio():
    if request.method == 'POST':
        file = request.files['file']
    print("got file")
    if file and allowed_file(file.filename):
        print("saving")
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))


print(__name__)
if __name__ == "__main__":
    app.run(debug=True)
