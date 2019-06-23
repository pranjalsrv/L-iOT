from flask import Flask, redirect, render_template, request, session, url_for
from flask_dropzone import Dropzone
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
from serial_receiver import serial_receive
from serial_transmitter import serial_transmit
import os

PORT = "COM8"
BAUD_RATE = 9600

app = Flask(__name__)
dropzone = Dropzone(app)

app.config['SECRET_KEY'] = 'supersecretkeygoeshere'

# Dropzone settings
app.config['DROPZONE_UPLOAD_MULTIPLE'] = False
app.config['DROPZONE_ALLOWED_FILE_CUSTOM'] = True
app.config['DROPZONE_ALLOWED_FILE_TYPE'] = 'image/*'
app.config['DROPZONE_REDIRECT_VIEW'] = 'results'

# Uploads settings
app.config['UPLOADED_PHOTOS_DEST'] = os.getcwd() + '/uploads'

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)  # set maximum file size, default is 16MB


@app.route('/', methods=['GET', 'POST'])
def index():
    # set session for image results
    if "file_urls" not in session:
        session['file_urls'] = []
    # list to hold our uploaded image urls
    file_urls = session['file_urls']

    # handle image upload from Dropszone
    if request.method == 'POST':
        file_obj = request.files
        for f in file_obj:
            file = request.files.get(f)

            # save the file with to our photos folder
            filename = photos.save(
                file,
                name=file.filename
            )

            # append image urls
            file_urls.append(photos.url(filename))

        session['file_urls'] = file_urls
        return "uploading..."
    # return dropzone template on GET request
    return render_template('index.html')


@app.route('/results', methods = ['GET','POST'])
def results():
    if request.method == 'POST':
        #ENTER CODE TO SEND TO ARDUINO
        print('sending to arduino')


    # redirect to home if no images to display
    if "file_urls" not in session or session['file_urls'] == []:
        return redirect(url_for('index'))

    # set the file_urls and remove the session variable
    file_urls = session['file_urls']
    print(file_urls[0])
    print('uploads/'+file_urls[0].split('/')[-1])
    session.pop('file_urls', None)

    return render_template('results.html', file_urls=file_urls)


@app.route('/sendtext', methods=['GET', 'POST'])
def sendtext():
    if request.method == 'POST':
        serial_transmit(PORT, BAUD_RATE, request.form['sendermessage'])
    return render_template('sendtext.html')

@app.route('/receivetext', methods=['GET', 'POST'])
def receivetext():


@app.route('/receiver', methods=['GET', 'POST'])
def receiver():
    return "<p>RECEIVING</p>"


app.run(host='127.0.0.1', port=8080, debug=True)