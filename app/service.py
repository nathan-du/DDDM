from flask import Flask, request, jsonify, render_template
import os
import findTable as ft

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def check():
    if request.method == 'GET':
        return render_template('home3.html')
    else:
        return "ERROR METHOD NOT ALLOWED\n"

@app.route('/test', methods = ['GET', 'POST'])
def test():
    if request.method == 'GET':
        query = request.args.get("query")
        print (query)
        result = ft.findTable(query)
        print (result)
        return jsonify(result)
    if request.method == 'POST':
        query = request.form['query']
        print(query)
        return jsonify({'result': query,'tasks': query})
    else:
        return "ERROR METHOD NOT ALLOWED\n"  

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(50000))
