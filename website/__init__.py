from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
import psycopg2
from flask_login import LoginManager
import os
import threading
import sys
from flask_limiter import Limiter
from flask_wtf.csrf import CSRFProtect
from flask_talisman import Talisman
from datetime import timedelta
from werkzeug.middleware.proxy_fix import ProxyFix

limiter = Limiter()

db = SQLAlchemy()

csrf = CSRFProtect()




def create_app():
    app = Flask(__name__)
    app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_port=1, x_prefix=1)

    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY') 

    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=180)
    postgres_host = os.getenv('PG_HOST')
    postgres_port = os.getenv('PG_PORT')
    DB_NAME = os.getenv('PG_DATABASE')
    postgres_sslmode = os.getenv('PG_SSLMODE')
    User = os.getenv('PG_User')
    sslCert = os.getenv('sslCert')
    sslKey = os.getenv('sslKey')
    sslRootCert = os.getenv('sslRootCert') 

    ssl_args = {
        'connect_args' :  { "sslmode": postgres_sslmode,
                            "sslcert": sslCert,
                            "sslkey": sslKey,
                            "sslrootcert":sslRootCert
                          }
                }
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://{user}:@{server}:{port}/{db}".format(user=User,
    server=postgres_host, db=DB_NAME, port=postgres_port)
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = ssl_args
    db.init_app(app)

    limiter.init_app(app)
    csrf.init_app(app)
    #talisman = Talisman(app, content_security_policy=csp)

    
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import Usuarios,Rol

    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return Usuarios.query.get(int(id))
    
    @app.after_request
    def remove_server_header(response):
        response.headers['Server'] = 'Generic-Server'
        return response


    return app


 
def create_database(app):
    #if not path.exists('website/' + DB_NAME):
    with app.app_context():
        db.create_all()
    print('Created Database!')
