
from flask import (
	Flask,
	render_template,
	jsonify
)
from flask_jwt_simple import JWTManager
from datetime import timedelta

import config.config_secrets as config_secrets


# init Flask app instance
app = Flask(
	__name__,
	static_folder='../client/dist/static',
	template_folder='../client/dist'
)
# jwt setup
app.config['JWT_SECRET_KEY'] = config_secrets.JWT_SECRET_KEY
# TODO: change the expire duration to something more suitable (1 week?)
app.config['JWT_EXPIRES'] = timedelta(days=1)
jwt = JWTManager(app)



# register api routes
from api.web.user_auth_api import user_auth_api
from api.web.user_api import user_api
from api.web.typing_test_api import typing_test_api
app.register_blueprint(user_auth_api, url_prefix='/api/user-auth')
app.register_blueprint(user_api, url_prefix='/api/user')
app.register_blueprint(typing_test_api, url_prefix='/api/typing-test')


# serve index for non-API calls
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
	return render_template('index.html')


# run the app if executed as main file to python interpreter
if __name__ == '__main__':
	app.run(host='0.0.0.0', port=80)



