import os
from flask_api import FlaskAPI
from instance.config import app_config
from flask import request, jsonify, abort

def create_new_app(app_config_name):
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')



    #import the blueprints and register them on the app
    from app.views import auth_blueprints, rqst_blueprints 
    app.register_blueprint(auth_blueprints)
    app.register_blueprint(rqst_blueprints )


    #custom error messages
    @app.errorhandler(404)
    def request_not_found(error=None):
        err_messages = {
                'status': 404,
                'err_messages': 'Ops! Not Found: ' + request.url ,
                'soft_note': 'Confirm and try again :-)'
        }
        response = jsonify(err_messages)
        response.status_code = 404

        return response
    @app.errorhandler(405)
    def request_not_allowed(error=None):
        err_messages = {
                'status': 405,
                'err_messages': 'Ops! Method not allowed in: ' + request.url ,
                'soft_note': 'Confirm and try again:-)'
        }
        response = jsonify(err_messages)
        response.status_code = 405

        return response

    @app.errorhandler(500)
    def requested_server_error(error=None):
        err_messages = {
                'status': 500,
                'err_messages': 'OOPS!! something went wrong in: ' + request.url
        }
        response = jsonify(err_messages)
        response.status_code = 500

        return response
    return app
