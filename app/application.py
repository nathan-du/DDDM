from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def check():
    if request.method == 'GET':
        return "THIS IS THE HOME PAGE\n"
    if request.method == 'POST':
        data = request.form
        truth = do_check(data)
        return "THIS IS THE RESULTS PAGE: " + str(truth) + "\n"
    else:
        return "ERROR METHOD NOT ALLOWED\n"    

def do_check(statement):
    #DO PROCESSING
    return True

if __name__ == '__main__':
    app.run()
