# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 09:33:23 2019

@author: saras
"""



##TASK 1 - create your app

#from flask import Flask
#
#
#app = Flask("MyApp") #Creates app object. Flask is the function, my app is the function input, returned result if the function will be saved in the variable app.
#@app.route("/") #a decorator -tells you the path in the web app where you want to run your functions. Allows you to execute code and funtions at a particular location. Here its the webpage / -the top level index page. Decorator is not a function but sits above one. 
#def hello(): #creating function
#    return "Hello World"
#app.run(debug=True) #app.run -makes sure flask runs your app. debug=True doesn't actually debug but tells you where the problems are



##TASK 2 - Run your app

#from flask import Flask
#
#app = Flask("MyApp") 
#@app.route("/") 
#def hello(): 
#    return "Yay I'm working! Hello and welcome!"
#app.run(debug=True) 



## TASK 3 - Using the render_template function

#from flask import Flask, render_template #render_template - allows flask to "serve" template (in Flask template is a HTML file)
#
#app = Flask("MyApp") 
#@app.route("/") 
#def hello(): 
#    return "Yay I'm working! Hello and welcome!"
#app.run(debug=True) 



## TASK 4 - add a template

#created a new folder called Templates
#created a new file called hello.html



## TASK 5 - update your file

#from flask import Flask, render_template
#
#app = Flask("MyApp") 
#@app.route("/") 
#def hello(): 
#    return "Yay I'm working! Hello and welcome!"
#
#@app.route("/<name>")
#def hello_someone(name):
#    return render_template("hello.html", name=name.title())  #returns Hello Name!
#
#app.run(debug=True) 



## TASK 6 - get information from the user

#from flask import Flask, render_template, request
#
#app = Flask("MyApp") 
#@app.route("/") 
#def hello(): 
#    return "Yay I'm working! Hello and welcome!"
#
#@app.route("/<name>")
#def hello_someone(name):
#    return render_template("hello.html", name=name.title())
#
#@app.route("/signup", methods=["POST"])
#def sign_up():
#    form_data = request.form
#    print (form_data["email"])
#    return "All OK"
#
#app.run(debug=True)   



##HOMEWORK - add another input field

from flask import Flask, render_template, request

app = Flask("MyApp") 
@app.route("/") 
def hello(): 
    return "Yay I'm working! Hello and welcome!"

@app.route("/<name>")
def hello_someone(name):
    return render_template("hello.html", name=name.title())

@app.route("/signup", methods=["POST"])
def sign_up():
    form_data = request.form
    print (form_data["email"])
    return "All OK"

@app.route("/greetingcard/<gbname>")
def greetingcard(gbname):
    return render_template("goodbye.html", gbname=gbname.title()) #prints Goodbye and good luck with your new role Gbname!

app.run(debug=True)