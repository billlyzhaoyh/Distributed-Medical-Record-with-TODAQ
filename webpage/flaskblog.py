from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm
from werkzeug.utils import secure_filename
import os
from flask_table import Table, Col
import retrieve_record
import display_drug


UPLOAD_FOLDER = '/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

api_key='82572e09-1a47-40e4-a018-22b6daa4e53f'
Alice_id='456f8dbc-7755-4ab9-b159-b47468f8c866'
mr_id='966885ed711d009460a645c66054d3bb2987787f18d2cb1bb41c94e735352a8c'

#drug file
drug_file=['c0971fb6dff9da8b71ab2380740a83b768e11c7390a64fbea5956875267171a3','a4e1a2fe7ef7a13210d3fb4102790d9b94df98de59bd6e8666cce091c09ac295']

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

record=retrieve_record.retrieve_record(api_key,mr_id)

items=[]

for i in range(len(record)):
    if bool(record[i]):
        items.append(record[i])



table = ItemTable(items)

#drug table
class ItemTable1(Table):
    drug = Col('Drug History')

    

# Get some objects
class Item1(object):
    def __init__(self,drug_history):
        self.drug = drug
        

drug=display_drug.display_drug_file(api_key,drug_file)

items1=[]

for i in range(len(drug)):
    if bool(drug[i]):
        items1.append({'drug':drug[i]})



table1 = ItemTable1(items1)



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

    return render_template('record.html', title='Record', table = table.__html__(),table1 = table1.__html__())


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
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


if __name__ == '__main__':
    app.run(debug=True)
