from flask import Flask, request, jsonify, render_template
import os
from parseSentence import parseSentence as ps

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def check():
    if request.method == 'GET':
        return render_template('main.html')
    if request.method == 'POST':
        query = request.form['query']
        print(query)
        return render_template('demo.html', factuality = str(ps(query)))
    else:
        return "ERROR METHOD NOT ALLOWED\n"

@app.route('/test', methods = ['GET', 'POST'])
def test():
    if request.method == 'GET':
        query = request.args.get("query")
        print (query)
        return jsonify({'tasks': query})
    if request.method == 'POST':
        query = request.form['query']
        print(query)
        return jsonify({'tasks': query})
    else:
        return "ERROR METHOD NOT ALLOWED\n"  

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(50000))
