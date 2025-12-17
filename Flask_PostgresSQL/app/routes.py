from flask import Blueprint, render_template, request, redirect, url_for, flash
from sqlalchemy.exc import SQLAlchemyError
from .models import User
from werkzeug.security import generate_password_hash
from . import db

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/create', methods=['POST'])
def create():
    fullname = request.form.get('fullname', '', type=str).strip()
    email = request.form.get('email', '', type=str).strip()
    password = request.form.get('password', '', type=str).strip()
    if not fullname or not email or not password:
        flash('All fields are required!', 'warning')
        return redirect(url_for('main.index'))
    user = User(fullname=fullname, email=email, password=password)
    try:
        user.validate()
    except ValueError as e:
        flash(str(e), 'danger')
        return redirect(url_for('main.index'))
    user.password = generate_password_hash(user.password)
    try:
        db.session.add(user)
        db.session.commit()
        flash('User created successfully!', "success")
    except SQLAlchemyError as e:
        db.session.rollback()
        flash(str(e), 'danger')
    return redirect(url_for('main.index'))

@bp.route('/update/<int:id>', methods=['POST', 'GET'])
def update(id):
    user = User.query.get_or_404(id)

    if request.method == 'POST':
        user.fullname = request.form.get('fullname', '', type=str).strip()
        user.email = request.form.get('email', '', type=str).strip()
        user.password = request.form.get('password', '', type=str).strip()
        if not user.fullname or not user.email or not user.password:
            flash('All fields are required!', 'warning')
            return redirect(url_for('main.update', id=id))
        try:
            user.validate()
        except ValueError as e:
            flash(str(e), 'danger')
            return redirect(url_for('main.update', id=id))
        user.password = generate_password_hash(user.password)
        try:
            db.session.add(user)
            db.session.commit()
            flash('User updated successfully!', "success")
        except SQLAlchemyError as e:
            db.session.rollback()
            flash(str(e), 'danger')
        return redirect(url_for('main.users'))

    return render_template('update.html', user=user)

@bp.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    user = User.query.get_or_404(id)
    try:
        db.session.delete(user)
        db.session.commit()
        flash('User deleted successfully!', 'success')
    except SQLAlchemyError as e:
        db.session.rollback()
        flash(str(e), 'danger')
    return redirect(url_for('main.users'))

@bp.route('/users')
def users():
    users = User.query.all()
    return render_template('users.html', users=users)

@bp.route('/about')
def about():
    return render_template('about.html')
