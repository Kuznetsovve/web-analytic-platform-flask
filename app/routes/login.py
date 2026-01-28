from flask import render_template, redirect, url_for, flash
from flask_login import current_user, login_user, login_required, logout_user
from app.models import Admin
from app.forms.login_form import LoginForm

def init_login(app):
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if current_user.is_authenticated:
            return redirect(url_for('profile'))
        form = LoginForm()
        if form.validate_on_submit():
            user = Admin.query.filter_by(username=form.username.data).first()
            if user is None or not user.check_password(form.password.data):
                flash('Неправильный логин или пароль')
                return redirect(url_for('login'))
            login_user(user, remember=form.remember.data)
            return redirect(url_for('profile'))
        return render_template('login.html', title='Войти', form=form)

    @app.route('/profile')
    @login_required
    def profile():
        return render_template('profile.html', title='Профиль', user=current_user)

    @app.route('/logout')
    @login_required
    def logout():
        logout_user()
        return redirect(url_for('index'))