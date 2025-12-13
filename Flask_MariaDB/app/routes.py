from flask import Blueprint, render_template, request, redirect, url_for, flash
from sqlalchemy.exc import SQLAlchemyError
from .models import Contact
from . import db

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/create', methods=['POST'])
def create():
    fullname = request.form.get('fullname', '', type=str).strip()
    email = request.form.get('email', '', type=str).strip()
    phone = request.form.get('phone', '', type=str).strip()
    if not fullname or not email or not phone:
        flash('All fields are required!', 'warning')
        return redirect(url_for('main.index'))
    contact = Contact(fullname=fullname, email=email, phone=phone)
    try:
        contact.validate()
    except ValueError as e:
        flash(str(e), 'danger')
        return redirect(url_for('main.index'))
    try:
        db.session.add(contact)
        db.session.commit()
        flash('Contact created successfully!', "success")
    except SQLAlchemyError as e:
        db.session.rollback()
        flash(str(e), 'danger')
    return redirect(url_for('main.index'))

@bp.route('/update/<int:id>', methods=['POST', 'GET'])
def update(id):
    contact = Contact.query.get_or_404(id)

    if request.method == 'POST':
        contact.fullname = request.form.get('fullname', '', type=str).strip()
        contact.email = request.form.get('email', '', type=str).strip()
        contact.phone = request.form.get('phone', '', type=str).strip()
        if not contact.fullname or not contact.email or not contact.phone:
            flash('All fields are required!', 'warning')
            return redirect(url_for('main.update', id=id))
        try:
            contact.validate()
        except ValueError as e:
            flash(str(e), 'danger')
            return redirect(url_for('main.update', id=id))
        try:
            db.session.add(contact)
            db.session.commit()
            flash('Contact updated successfully!', "success")
        except SQLAlchemyError as e:
            db.session.rollback()
            flash(str(e), 'danger')
        return redirect(url_for('main.contacts'))

    return render_template('update.html', contact=contact)

@bp.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    contact = Contact.query.get_or_404(id)
    try:
        db.session.delete(contact)
        db.session.commit()
        flash('Contact deleted successfully!', 'success')
    except SQLAlchemyError as e:
        db.session.rollback()
        flash(str(e), 'danger')
    return redirect(url_for('main.contacts'))

@bp.route('/contacts')
def contacts():
    contacts = Contact.query.all()
    return render_template('contacts.html', contacts=contacts)

@bp.route('/about')
def about():
    return render_template('about.html')
