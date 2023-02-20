from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    return redirect ('/dojos')


# get dojos from db route
@app.route('/dojos')
def all_dojos():
    return render_template('index.html', all_dojos = dojo.get_all())

#add dojos route

@app.route('/dojo/create', methods=["POST"])
def create_dojo():
    Dojo.save(request.form)
    return redirect ('/dojos')


@app.route('/dojo/<int:id>')
def show_dojo(id):
    data = {
        "id": id
    }
    return render_template('dojo.html', dojo=Dojo.get_one_with_ninjas(data))