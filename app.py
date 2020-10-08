from __future__ import print_function
from flask import Flask, render_template, request
import sys
app = Flask(__name__)


@app.route('/')
def main():
    return render_template('app.html')


@app.route('/send', methods=['POST'])
def send(sum=sum):
    if request.method == 'POST':
        num1 = request.form['num1']
        num2 = request.form['num2']
        operation = request.form['operation']

        if operation == 'add':

            sum = float(num1) + float(num2)
            print(sum, file=sys.stdout)
            return render_template('app.html', sum=sum)

        elif operation == 'subtract':
            sum = float(num1) - float(num2)
            print(sum,file=sys.stdout)
            return render_template('app.html', sum=sum)

        elif operation == 'multiply':
            sum = float(num1) * float(num2)
            print(sum,file=sys.stdout)
            return render_template('app.html', sum=sum)

        elif operation == 'divide':
            print(sum,file=sys.stdout)
            sum = float(num1) / float(num2)
            return render_template('app.html', sum=sum)
        else:
            return render_template('app.html')


if __name__ == ' __main__':
    app.debug = True
    app.run()
