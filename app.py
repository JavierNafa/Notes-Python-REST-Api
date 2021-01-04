from os import getenv
from flask import Flask
from flask_cors import CORS
from src.routes import user, login, note
from src.middlewares import schema_validator, error_handler, auth

app = Flask(__name__)
CORS(app=app)
app.config['ENV'] = getenv('ENV')


app.before_request_funcs = {
    'user': [schema_validator.validate],
    'login': [schema_validator.validate, auth.verify_user],
    'note': [auth.verify_token, schema_validator.validate]
}

app.register_blueprint(user.user_blueprint, url_prefix='/user')
app.register_blueprint(login.login_blueprint, url_prefix='/login')
app.register_blueprint(note.note_blueprint, url_prefix='/note')

app.register_error_handler(Exception, error_handler.handle_errors)
