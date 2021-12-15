from flask import Blueprint, render_template, redirect, request, url_for, jsonify, session
from flask.templating import render_template
from application import app
from application import db
# from application import studentCollection
from bson.objectid import ObjectId


@app.route('/', methods = ['GET', 'POST'])
def index():
    return render_template('index.html')



@app.route('/home')
def home():
    # data = studentCollection.find({})
    data = db.student.find({})
    total_number = data.count(with_limit_and_skip=True)
    return render_template('home.html', students = data, total_number = total_number)

    

@app.route('/add_student', methods = ['POST'])
def add_student():
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    date_of_birth = request.form['dob']
    address = request.form['address']
    fphone = request.form['fphone']
    mphone = request.form['mphone']
    # studentCollection.insert_one({'Firstname' : firstname, 'Lastname': lastname, 'Date_Of_Birth' : date_of_birth, "Address":address, "Father_No":fphone, "Mother_No":mphone})
    db.student.insert_one({'Firstname' : firstname, 'Lastname': lastname, 'Date_Of_Birth' : date_of_birth, "Address":address, "Father_No":fphone, "Mother_No":mphone})
    
    # session['show_modal'] = True
    return redirect(url_for('home'))



@app.route('/edit/<Firstname>', methods = ['GET','POST'])
def edit(Firstname):
    # data = studentCollection.find_one({'Firstname':Firstname})
    data = db.student.find_one({'Firstname':Firstname})
    return render_template('edit.html', student=data)


@app.route('/edit_student/<Firstname>', methods = ['POST'])
def edit_student(Firstname):
    updatedFirstname = request.form['firstname']
    updatedLastname = request.form['lastname']
    updatedDate_of_birth = request.form['dob']
    updatedAddress = request.form['address']
    updatedFphone = request.form['fphone']
    updatedMphone = request.form['mphone']
    # studentCollection.update_one({'Firstname': Firstname}, {'$set' : {'Firstname': updatedFirstname, 'Lastname': updatedLastname, 'Date_Of_Birth': updatedDate_of_birth, 'Address' : updatedAddress, "Father_No": updatedFphone, "Mother_No" : updatedMphone }})
    db.student.update_one({'Firstname': Firstname}, {'$set' : {'Firstname': updatedFirstname, 'Lastname': updatedLastname, 'Date_Of_Birth': updatedDate_of_birth, 'Address' : updatedAddress, "Father_No": updatedFphone, "Mother_No" : updatedMphone }})
    return redirect(url_for('home'))



@app.route('/delete_student/<Firstname>')
def delete_student(Firstname):
    # studentCollection.find_one_and_delete({'Firstname': Firstname})
    db.student.find_one_and_delete({'Firstname': Firstname})
    return redirect(url_for('home'))
    





