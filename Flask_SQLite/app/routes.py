from flask import Blueprint, render_template, request, redirect, url_for, flash
from . import db
from .models import Task

bp = Blueprint("main", __name__)

@bp.route("/")
def index():
    tasks = Task.query.all()
    return render_template("index.html", tasks=tasks)

@bp.route("/create", methods=["POST"])
def create():
    content = request.form.get('content', '', type=str).strip()
    if not content:
        flash("Task content required!", "warning")
        return redirect(url_for('main.index'))
    task = Task(content=content)
    try:
        db.session.add(task)
        db.session.commit()
    except Exception:
        db.session.rollback()
        flash("Could not save task!", "danger")
    return redirect(url_for('main.index'))

@bp.route("/done/<int:id>", methods=["POST"])
def done(id):
    task = Task.query.get_or_404(id)
    task.done = True
    try:
        db.session.commit()
    except Exception:
        db.session.rollback()
    return redirect(url_for('main.index'))

@bp.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    task = Task.query.get_or_404(id)
    try:
        db.session.delete(task)
        db.session.commit()
    except Exception:
        db.session.rollback()
    return redirect(url_for('main.index'))
