from flask import Flask, render_template, redirect, request
import serial

RECEIVER_COM = ""
SENDER_COM = ""

BAUD_RATE = 1200

app = Flask(__name__)


@app.route('/comselector', methods=['GET', 'POST'])
def comselector():
    if request.method == 'POST':
        receiverCOM = request.form['receiverCOM']
        senderCOM = request.form['senderCOM']
        print(receiverCOM, senderCOM)


    return render_template('comselector.html')


@app.route('/', methods=['GET', 'POST'])
def index():
    return redirect('/comselector')


if __name__ == '__main__':
    app.run('127.0.0.1', port=8000, debug=True)
