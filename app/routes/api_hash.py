from werkzeug.security import generate_password_hash

def init_api_hash(app):
    @app.route('/api/hash/<string>')
    def api_hash(string):
        hash_str = generate_password_hash(string)
        return {"request": string, "result": hash_str}
