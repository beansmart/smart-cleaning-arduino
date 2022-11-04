from flask import Flask, jsonify, request, render_template, Response, request
import serial
import time

from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['DEBUG'] = True
Bootstrap(app)

ser = serial.Serial('COM3', 9600, timeout=1.0)
time.sleep(3)
ser.reset_input_buffer()
if ser.readable():
    print('serial ok')


def printOn():
    ser.write("1111\n".encode('utf-8'))


def printOff():
    print('1111')
    ser.write("1001\n".encode('utf-8'))


@app.route('/')
def hello_world():  # put application's code here
    return render_template('main.html')


@app.route('/app', methods=['GET', 'POST'])
def run_application():
    if request.method == 'POST':
        if 'arm_on' in request.form['status']:
            printOn()
        if 'arm_off' in request.form['status']:
            printOff()
    return render_template('main.html')


if __name__ == '__main__':
    app.run()
