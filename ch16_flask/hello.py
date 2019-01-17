# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 09:33:23 2019

@author: saras
"""

from flask import Flask, render_template, request
app = Flask("MyApp") 
#creates the object Flask



@app.route("/") 
#python decorator creates new route in webpage / -the top level
def index():
    #creating function
    return "<h1>Welcome - finally I am working!!!!</h1>"



@app.route("/contact/me")
def contact():
    return "Find me on LinkedIn"
#trying two forward slashes


@app.route("/portfolio")
def portfolio():
    test1="check"
    return test1
#trying a variable
    

@app.route("/name/<name>")
def hello_someone(name):
    return render_template("hello.html", name=name.title())
#prints Hello Name!
 
    
@app.route("/greetingcard/<gbname>")
def greetingcard(gbname):
    return render_template("goodbye.html", gbname=gbname.title())
#prints Goodbye and good luck with your new role Gbname!


@app.route("/about")
def about():
    return render_template("about.html", title="about")

@app.route("/confirmation", methods=["POST"])
def confirmation():
    form_data = request.form
    email = form_data["email"]
    result="All ok"
    return render_template("confirmation.html", title="Form confirmation", **locals())

    
#@app.route("/journey")
#def my_journey():
    
#@route("path/to/sheet.css")
#<a href="sheet.css"=>"
    #example of linking to stylesheet  once the css file is in the route it can be accessed

    
app.run(debug=True) 
#calling run on the app object