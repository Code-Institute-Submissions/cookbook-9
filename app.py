import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask (__name__)
app.config["MONGO_DBNAME"]= 'cookbook'
app.config["MONGO_URI"]= 'mongodb://admin:cjm014jp@ds129593.mlab.com:29593/cookbook'

mongo = PyMongo(app)

def write_to_file(filename, data):
    """handle the process of writing data to text files"""
    with open(filename, "a") as file:
        file.writelines(data)
        
@app.route('/', methods=["GET", "POST"])
@app.route('/index', methods=["GET", "POST"])
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
                           recipes=mongo.db.recipes.find(), countries=mongo.db.cuisine.find())
                           
@app.route('/<username>/return_recipe', methods=['GET','POST'])
def return_recipe(username):
    recipes = mongo.db.recipes
    
    if request.form.get("COO") is not None:
        cuisine = request.form.get("COO")
    else: cuisine = { '$exists':True, '$ne': [] }
    
    if request.form.get("main") != "":
        mainIngredient = request.form.get("main")
    else: mainIngredient = { '$exists':True, '$ne': [] }
    
    if request.form.get("allergies") != "":
        allergies = {"$ne": request.form.get("allergies")}
    else: allergies = { '$exists':True, '$ne': [] }
    
    if request.form.get("ingredients") != "":
        ingredients = {"$regex": ".*" + request.form.get("ingredients") + ".*"}
    else: ingredients = { '$exists':True, '$ne': [] }

    results = recipes.find({"$and": 
                         [  {"cuisine":cuisine }, 
                            {"mainIngredient": mainIngredient},
                            {"allergies": allergies},
                            {"ingredients": ingredients},
                          ]})
 
                          
    return render_template('recipe.html',username=username,
                          results=results, recipes=recipes)
    
@app.route('/<username>/insert_recipe', methods=['POST'])
def insert_recipe(username):
    recipes = mongo.db.recipes
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('add_recipe', username=username))

@app.route('/<username>/recipe')
def recipe(username):
    return render_template('recipe.html',username=username,
                           recipes=mongo.db.recipes.find())


@app.route('/<username>/edit_recipe/<recipeID>')
def edit_recipe(username, recipeID):
    the_recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipeID)})
    return render_template('update.html', recipe=the_recipe, username=username, countries=mongo.db.cuisine.find())

@app.route('/<username>/update_recipe/<recipeID>', methods=['POST'])
def update_recipe(username, recipeID):
    recipes = mongo.db.recipes
    recipes.update({'_id': ObjectId(recipeID)},
    {
        'recipeName':request.form.get('recipeName'),
        'mainIngredient':request.form.get('Main_Ingredient'),
        'allergies': request.form.get('Allergies'),
        'author': request.form.get('Author'),
        'cuisine':request.form.get('Cuisine'),
        'ingredients':request.form.get('ingredients'),
        'method':request.form.get('instructions')
    })
    return render_template('control_panel.html',username=username,
                           recipe=mongo.db.recipes.find())

@app.route('/<username>/delete_recipe/<recipeID>')
def delete_recipe(username, recipeID):
    recipes = mongo.db.recipes
    recipes.remove({'_id': ObjectId(recipeID)})
    return render_template('control_panel.html',username=username,
                           recipe=mongo.db.recipes.find())
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)