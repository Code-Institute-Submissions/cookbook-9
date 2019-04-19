import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
# from bson.obecjtid import ObjectId

app = Flask (__name__)
app.config["MONGO_DBNAME"]= 'cookbook'
app.config["MONGO_URI"]= 'mongodb://admin:cjm014jp@ds129593.mlab.com:29593/cookbook'

mongo = PyMongo(app)

def write_to_file(filename, data):
    """handle the process of writing data to text files"""
    with open(filename, "a") as file:
        file.writelines(data)

@app.route('/', methods=["GET", "POST"])
def index():
    """gives users a chance to enter their username so that they can add delete and edit their own recipes, also althoughs new users to set up usernames"""
    
    if request.method == "POST":
        with open("data/users.txt", "r") as file:
            lines = file.read().split()
            
        if request.form["username"] in lines:
            user =  request.form["username"] + "/control_panel"
            return redirect(user)
        else:
            return "<h3>No username found</h3>"
            
    return render_template("index.html")
    
@app.route('/newuser', methods=["GET", "POST"])
def add_user():
    if request.method == "POST":
        with open("data/users.txt", "r") as file:
            lines = file.read().split()
            
        if request.form["new_user"] in lines:
            return "<h3>username in use</h3>"
        else:
            write_to_file("data/users.txt", request.form["new_user"] + "\n")
            user =  request.form["new_user"] + "/control_panel"
            return redirect(user)
    return render_template("newuser.html")


@app.route('/<username>/control_panel')
def control_panel(username):
    return render_template("control_panel.html",username=username,
    recipes=mongo.db.recipes.find())

@app.route('/<username>/add_recipe')
def add_recipe(username):
    return render_template('add_recipe.html',username=username,
                           countries=mongo.db.cuisine.find())

@app.route('/<username>/get_recipe')
def get_recipe(username):
    return render_template('get_recipe.html',username=username,
                           recipes=mongo.db.recipes.find())
                           
@app.route('/<username>/return_recipe', methods=['GET','POST'])
def return_recipe(username):
    recipes = mongo.db.recipes
    cuisine = request.form.get("COO")
    mainIngredient = request.form.get("main")
    ingredients = request.form.get("ingredients")
    allergies = request.form.get("allergies")
    results = recipes.find({"$or": [{"cuisine": cuisine}, 
                          {"allergies": allergies}, 
                          {"mainIngredient": mainIngredient}, 
                          {"ingredients": ingredients}]})
    return render_template('recipe.html',username=username,
                          results=results)
                           
    
@app.route('/<username>/insert_recipe', methods=['POST'])
def insert_recipe(username):
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('add_recipe', username=username))

@app.route('/<username>/recipe')
def recipe(username):
    return render_template('recipe.html',username=username,
                           recipe=mongo.db.recipes.find())

    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)