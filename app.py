from flask import Flask, jsonify, request, render_template, Response, request
import serial
import time
import arduino
app = Flask(__name__)

ser = serial.Serial('COM3',9600,timeout=1.0)
time.sleep(3)
ser.reset_input_buffer()
print('serial ok')

def printOn():
    ser.write("1111\n".encode('utf-8'))
def printOff():
    ser.write("1001\n".encode('utf-8'))


@app.route('/')
def hello_world():  # put application's code here
    return 'It works'

@app.route('/app', methods = ['GET','POST'])
def run_application():
    if request.method == 'POST':
        if 'on' in request.form.to_dict():
            printOn()

        if 'off' in request.form.to_dict():
            printOff()

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
