from flask import Flask
from flask import render_template, redirect, url_for, flash
from app import db
from flask_login import current_user
from app.models import User
from app.forms import createAccount
#from app.forms import registrationForm not yet created

app = Flask(__name__)
app.config['SECRET_KEY'] = 'some-key'

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = createAccount()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
if __name__ == '__main__':
    app.run(debug=True)