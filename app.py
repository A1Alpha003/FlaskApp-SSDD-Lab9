from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///firstapp.db'
db = SQLAlchemy(app)

# User model
class Users(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(100))
    lname = db.Column(db.String(100))
    email = db.Column(db.String(120))

    def __repr__(self):
        return f'{self.sno} - {self.fname}'

# Home page: display users + add new
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Add new user
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        new_user = Users(fname=fname, lname=lname, email=email)
        db.session.add(new_user)
        db.session.commit()
        return redirect('/')

    allpeople = Users.query.all()
    return render_template('index.html', allpeople=allpeople)

# Delete user
@app.route('/delete/<int:sno>', methods=['POST'])
def delete(sno):
    user_to_delete = Users.query.get_or_404(sno)
    db.session.delete(user_to_delete)
    db.session.commit()
    return redirect('/')

# Update user
@app.route('/update/<int:sno>', methods=['GET', 'POST'])
def update(sno):
    user = Users.query.get_or_404(sno)

    if request.method == 'POST':
        user.fname = request.form['fname']
        user.lname = request.form['lname']
        user.email = request.form['email']
        db.session.commit()
        return redirect('/')

    return render_template('update.html', user=user)

if __name__ == "__main__":
    app.run(debug=True)
