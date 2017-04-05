from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def check():
    if request.method == 'GET':
        return render_template('main.html')
    if request.method == 'POST':
        query = request.form['query']
        print(query)
        return render_template('results.html', factuality = str(do_check(query)))
    else:
        return "ERROR METHOD NOT ALLOWED\n"    

def do_check(query):
    #DO PROCESSING
    return "true" in query

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(50000))
