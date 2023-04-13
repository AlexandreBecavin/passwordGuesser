from flask import Flask
from flask import render_template
from flask import request
from merge import Merge

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/data', methods=['POST'])
def data():
    wordArray = [] 
    for counter, data in enumerate(request.form.getlist('text')):
        wordArray.append(data)
    for counter, data in enumerate(request.form.getlist('date')):
        wordArray.append(data)
        
    merge = Merge(wordArray, True, True)
    return merge._passwords

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)