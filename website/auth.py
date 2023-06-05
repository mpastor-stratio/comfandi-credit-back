import re
from functools import wraps
from flask import Blueprint, render_template, request, flash, redirect, url_for, abort
from .models import Usuarios, Listasrestrictivas, Rol
from werkzeug.security import generate_password_hash, check_password_hash

from . import db
from flask_login import login_user, login_required, logout_user, current_user
from . import limiter
from .forms import SignUpForm
import bleach


from flask_wtf.csrf import CSRFProtect
from flask_csp.csp import csp_header


csp = {
    'default-src': 
        "'self'",
    'img-src': 
        '\'self\' data:',
    'style-src': 
        '\'self\' \'unsafe-inline\' https://fonts.googleapis.com/ https://unpkg.com/ https://cdn.jsdelivr.net/',
    'script-src': '\'self\' \'unsafe-inline\' https://code.jquery.com/ https://cdn.jsdelivr.net/ https://cdnjs.cloudflare.com/',
    'font-src': '\'self\' https://fonts.googleapis.com/ https://cdn.jsdelivr.net/ https://unpkg.com/' ,
    'connect-src': '\'self\''
}

auth = Blueprint('auth', __name__)

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if current_user.rol_id != 1:
            abort(403)
        return f(*args, **kwargs)
    return decorated_function

def validate_user_credentials(email, password):
    user = Usuarios.query.filter_by(email=email).first()
    if not user:
        return "Email no existe"

    if not check_password_hash(user.password, password):
        return "Password Incorrecto, por favor intenta nuevamente."

    return None

def is_valid_password(password):
    has_upper = re.search(r'[A-Z]', password)
    has_lower = re.search(r'[a-z]', password)
    has_digit = re.search(r'\d', password)
    has_special = re.search(r'~[!@#$%^&*(),.?":{}|<>]', password)
    return has_upper and has_lower and has_digit and has_special

@auth.route('/login', methods=['GET', 'POST'])
@csp_header(csp)
@limiter.limit("5 per minute")  # Ajusta el límite según sea necesario
def login():
    if request.method == 'POST':
        email = bleach.clean(request.form.get('email'))
        password = request.form.get('password')

        error_message = validate_user_credentials(email, password)
        if error_message:
            flash(error_message, category='error')
        else:
            user = Usuarios.query.filter_by(email=email).first()
            login_user(user, remember=True)
            return redirect(url_for('views.home'))

    return render_template("login2.html", user=current_user)

@auth.route('/logout')
@csp_header(csp)
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/listas', methods=['GET', 'POST'])
@csp_header(csp)
@login_required
def listas():
    if request.method == 'POST' and 'search-titulares' in request.form :
        search_titulares= request.form.get('search-titulares')
        titular_n = Listasrestrictivas.query.filter_by(Id_Afiliado=search_titulares).all()
        print(titular_n)
        print(search_titulares)
        print(current_user)
        return render_template("index.html", user=current_user, query_titular=titular_n, search_t =search_titulares )
        
    if request.method == 'POST' and 'search-deudor' in request.form :
        search_deudor= request.form.get('search-deudor')
        deudor_n = Listasrestrictivas.query.filter_by(Id_Afiliado=search_deudor).all()
        print(deudor_n)
        print(search_deudor)
        return render_template("index.html", user=current_user, query_deudor=deudor_n, search_d = search_deudor )
    print(current_user.id == 1)
    return render_template("index.html", user=current_user)



@auth.route('/sign-up', methods=['GET', 'POST'])
@csp_header(csp)
@login_required
@admin_required
def sign_up():
    if request.method == 'POST':
        email = bleach.clean(request.form.get('email'))
        firstName = bleach.clean(request.form.get('firstName'))
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        role_id = request.form.get('rol_id')

        user_n = Usuarios.query.filter_by(email=email).first()

        if user_n:
            flash('El Email ya existe', category='error')
        elif len(email) < 4:
            flash('El Email debe tener más de 3 caracteres.', category='error')
        elif len(firstName) < 2:
            flash('El primer nombre debe tener más de 1 caracter.', category='error')
        elif password1 != password2:
            flash('El Password no es el mismo en la confirmación.', category='error')
        elif len(password1) < 7:
            flash('El Password debe contener al menos 14 caracteres.', category='error')
        elif not is_valid_password(password1):
            flash('El Password debe contener al menos una mayuscula, una minuscula, un dígito, y al menos un caracter especial.', category='error')
        else:
            # add user to database
            new_user = Usuarios(email=email, rol_id=role_id, first_name=firstName,
                                password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!', category='success')
            return render_template("signup.html", user=current_user)

    return render_template("signup.html", user=current_user)
