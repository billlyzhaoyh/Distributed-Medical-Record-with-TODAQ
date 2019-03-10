from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm
from werkzeug.utils import secure_filename
import os
from flask_table import Table, Col

UPLOAD_FOLDER = '/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

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
class ItemTable(Table):
    name = Col('Name')
    description = Col('Description')

# Get some objects
class Item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
items = [Item('Name1', 'Description1'),
         Item('Name2', 'Description2'),
         Item('Name3', 'Description3')]

table = ItemTable(items)
# # Or, equivalently, some dicts
# items = [dict(name='Name1', description='Description1'),
#          dict(name='Name2', description='Description2'),
#          dict(name='Name3', description='Description3')]


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
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


if __name__ == '__main__':
    app.run(debug=True)
