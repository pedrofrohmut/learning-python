from flask import Blueprint, render_template, request, flash
from flask.json import jsonify
from flask_login import login_required, current_user
import json

from .models import Note
from . import db


views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note_content = request.form.get('noteContent') or ""
        if len(note_content) < 2:
            flash('Note is too short!', category='error')
            return render_template('home.html', user=current_user)
        new_note = Note(content=note_content, user_id=current_user.id)
        db.session.add(new_note)
        db.session.commit()
        flash('Note added', category='success')
    return render_template("home.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():
    data = json.loads(request.data)
    noteId = data['noteId']
    note = Note.query.get(noteId)
    if note and note.user_id == current_user.id:
        db.session.delete(note)
        db.session.commit()
        return jsonify({})