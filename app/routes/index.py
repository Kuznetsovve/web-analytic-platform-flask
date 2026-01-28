from flask import render_template

def init_index(app):
    @app.route('/', methods= ['GET', 'POST'])
    @app.route('/index', methods=['GET', 'POST'])
    @app.route('/home', methods=['GET', 'POST'])
    def index():
        return render_template(template_name_or_list="index.html")