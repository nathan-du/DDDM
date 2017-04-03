from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def check():
    if request.method == 'GET':
        return render_template('main.html')
    if request.method == 'POST':
        data = request.form
        return render_template('results.html', factuality = do_check(data))
    else:
        return "ERROR METHOD NOT ALLOWED"    

def do_check(statement):
    #DO PROCESSING
    return True

if __name__ == '__main__':
    app.run()