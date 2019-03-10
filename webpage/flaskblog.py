from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm
from werkzeug.utils import secure_filename
import os
import sys
from flask_table import Table, Col
import retrieve_record
import requests

UPLOAD_FOLDER = '/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

api_key='82572e09-1a47-40e4-a018-22b6daa4e53f'
Alice_id='de946eab-7f5a-4323-9867-7f1190fb1f5a'

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

posts = [
    # {
    #     'author': 'Coreyyyy Schafer',
    #     'title': 'Blog Post 1',
    #     'content': 'First post content',
    #     'date_posted': 'April 20, 2018'
    # },
    # {
    #     'author': 'Jane Doe',
    #     'title': 'Blog Post 2',
    #     'content': 'Second post content',
    #     'date_posted': 'April 21, 2018'
    # }
]

# Declare your table
# Declare your table
class ItemTable(Table):
    date = Col('Date')
    symptoms=Col('Symptom')
    diagnosis=Col('Diagnosis')
    prescription=Col('Prescription')


# Get some objects
class Item(object):
    def __init__(self,date,symptom,diagnosis,prescription):
        self.date = date
        self.symptom = symptom
        self.diagnosis = diagnosis
        self.prescription = prescription

record=retrieve_record.retrieve_record(api_key,Alice_id)

items=[]

for i in range(len(record)):
    if bool(record[i]):
        items.append(record[i])



table = ItemTable(items)




@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/seeing")
def seeing():
    return render_template('seeing.html', title='Seeing')

@app.route("/qr")
def qr():
    return render_template('qr.html', title='QR', qr = "localhost"+url_for('static', filename='qrcode.jpg'))

@app.route("/record")
def record():
    # Populate the table

    return render_template('record.html', title='Record', table = table.__html__())


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # myFile = secure_filename(form.image.file.filename)
        # file_path = os.path.join(app.config['UPLOAD_FOLDER'], myFile)
        # form.image.file.save(file_path)

        # image_data = request.FILES[form.image.name].read()
        # open(os.path.join(UPLOAD_PATH, form.image.data), 'w').write(image_data)

        flash(f'Account created for {form.name.data}!', 'success')
        print(type(form.symptom.data))

        url = 'https://api.todaqfinance.net/transactions'

        user_id = '456f8dbc-7755-4ab9-b159-b47468f8c866'
        receiver_id = '456f8dbc-7755-4ab9-b159-b47468f8c866'
        file_id = '966885ed711d009460a645c66054d3bb2987787f18d2cb1bb41c94e735352a8c'
        Hash_img="None"
        Doctor_public_key="None"
        Doctor_verified_msg="None"

        payload = "{\n\t\"data\": {\n\t\"attributes\":{\n\t\t\"metadata\":{\n    \t\t\"date\":\""+form.date.data+"\",\n    \t\t\"prescription\":\""+form.prescription.data+"\",\n    \t\t\"diagnosis\":\""+form.diagnosis.data+"\",\n    \t\t\"symptoms\":\""+form.symptom.data+"\" \n   \t}\n \t}, \n\t\t\"verification\":{\n\t\t\t\"Hashed_Image\":\"" + Hash_img + "\", \n\t\t\t\"Doctor_public_key\":\"" + Doctor_public_key + "\",\n\t\t\t\"Doctor_verified_msg\":\"" + Doctor_verified_msg + "\"},    \t\"relationships\":{\n    \t\t\"sender\":{\n    \t\t\t\"data\": {\n\t    \t\t\t\"type\":\"account\",\n    \t\t\t\t\"id\":\"" + user_id + "\"\n    \t\t\t}\n    \t\t},\n    \t\t\"recipient\":{\n    \t\t\t\"data\": {\n\t    \t\t\t\"type\":\"account\",\n    \t\t\t\t\"id\":\"" + user_id + "\"\n    \t\t\t}\n    \t\t},\n    \t\t\"files\":{\n    \t\t\t\"data\":[\n    \t\t\t\t{\n    \t\t\t\t\t\"type\":\"file\",\n\t\t    \t\t\t\"id\":\"" + file_id + "\"\n    \t\t\t\t}\n\t\t\t\t]\n    \t\t}\n    \t}\n    }\n}"

        headers = {
            'Content-Type': 'application/json',
            'x-api-key': '82572e09-1a47-40e4-a018-22b6daa4e53f'
        }
        response = requests.request('POST', url, headers=headers, data=payload, allow_redirects=False)




        return redirect(url_for('home'))


    return render_template('register.html', title='Register', form=form)

print("asad")

if __name__ == '__main__':
    print(":asdsa")
    app.run(debug=True, port=8000 )
