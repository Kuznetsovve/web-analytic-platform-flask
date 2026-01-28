from flask import render_template
import json

def init_about(app):
    @app.route('/about', methods= ['GET', 'POST'])
    def about():
        with open('app/data/about.json', 'r', encoding='utf-8') as f:
            data = json.load(f)

        return render_template(template_name_or_list='about.html', data=data)