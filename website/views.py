# all the code other than the authenticating user goes here
# Blue print allows us to create multiple VIEW files seperatley and organise them and use it here

from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint('views',__name__) # def blue print naming views 
 
# this function runs whenever we go in type '/' in url and the it goes back to the main page which is home here
# handles adding of note
@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    # In the home page if its a post request , it receives the note validates it and  adds it to the data base
    if request.method == 'POST':
        note = request.form.get('note')
        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')
    # if its a get reqest, it shows the home page
    return render_template("home.html", user=current_user)

# handles deleting of note in home page 
@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)   #gets the note id from DB
    if note:                        # if note Exist deleting it and committing it
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})              #Being a post request it needs to return something.. so we return a empty string