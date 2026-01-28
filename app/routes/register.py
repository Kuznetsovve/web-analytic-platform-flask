from app import db
from app.forms.register_form import RegistrationForm
from flask import render_template, redirect, url_for, flash
from flask_login import current_user
from app.models import Admin

def init_register(app):
    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if current_user.is_authenticated:
            return redirect(url_for('index'))
        form = RegistrationForm()
        if form.validate_on_submit():
            user = Admin(username=form.username.data)
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            flash('Вы успешно зарегистрировались')
            return redirect(url_for('login'))
        return render_template('register.html', title='Register', form=form)