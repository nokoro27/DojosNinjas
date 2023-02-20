from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import dojo, ninja

#Routes

@app.route('/ninjas')
def add_ninja():
    return render_template('ninja.html', dojos=dojo.Dojo.read_all())

@app.route('/ninja/create', methods=['POST'])
def create_ninja():
    ninja.Ninja.save(request.form)
    data_id = request.form['dojo_id']
    return redirect(f"/dojo/{data_id}")