from flask import (Flask, render_template, request, flash, session,
                   redirect, jsonify, url_for)
from model import connect_to_db, db, User, Plants
import crud
from jinja2 import StrictUndefined
from passlib.hash import argon2
from flask import Flask
from datetime import datetime
import chatgpt_list_maker

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

# Store the current month and the number of uses
current_month = datetime.now().month
use_count = 0
max_uses = 50


@app.route('/')
def homepage():
    """Show Homepage"""
    return render_template("homepage.html")

@app.route('/faq')
def faq():
    """Show FAQs"""
    return render_template("faq.html")

@app.route('/users', methods=['POST'])
def create_user():
    """Create a new user."""
    email = request.form.get("email")
    password = request.form.get("password")
    hashed = argon2.hash(password)

    user = crud.get_user_by_email(email)
    if user:
        flash("This email is already associated with an account, please login with password.") 
    else:
        user = crud.create_user(email, hashed)
        flash("Account created successfully, and you can now login.")
    return redirect('/#begin')

@app.route('/login', methods=['POST'])
def login():
    """Login user"""
    email = request.form.get("email")
    password = request.form.get("password")
    user = crud.get_user_by_email(email)

    if user:
        if argon2.verify(password, user.password):
            session['user_id'] = user.user_id
            flash('Logged in!')
            return redirect('/create')
        else:
            flash("Wrong Password")
            return redirect(url_for('homepage') + '#begin')
    else:
        flash("Wrong username.")
        return redirect(url_for('homepage') + '#begin')

@app.route('/create')
def create():

    if 'user_id' in session:
    
        global  use_count, current_month

        # Check if the current month has changed
        if datetime.now().month != current_month:
            # Reset the use count for the new month
            current_month = datetime.now().month
            use_count = 0

        if use_count < max_uses:
            # Increment the use count
            use_count += 1
            return render_template("create.html")
        else:
            # Access limit reached, return an error or redirect to another page
            return "Access limit reached for this month."
    
    else:

        return render_template("no_user.html")
    

@app.route('/create', methods = ['POST'])
def get_info():

    shape = request.form.get("shape")
    dimensions = request.form.get("dimensions")
    garden_type = request.form.get("garden_type")
    pets = request.form.get("pets")
    favorite_colors = request.form.get("favorite_colors")
    special_goals = request.form.get("special_goals")
    number_of_plants = int(request.form.get("number_of_plants"))
    plant_hardiness_zone = request.form.get("plant_hardiness_zone")

    # Start the prompt
    prompt = (f"A list of {number_of_plants} plants that thrive in a {plant_hardiness_zone} plant hardiness zone in a {garden_type} garden. ")

    # Check if pets exists, and if so, add the appropriate text
    if pets:
        prompt += (f"They should be non-toxic to {pets}. ")

    # Check if special_goals exists, and if so, add the appropriate text
    if special_goals:
        prompt += (f"They should be mostly {special_goals}. ")

    # Check if favorite_colors exists, and if so, add the appropriate text
    if favorite_colors:
        prompt += (f"Most should mostly have the colors {favorite_colors}.")

    print(prompt)


    # call on python algorithms to generate list
    generated_list = chatgpt_list_maker.chatgpt(prompt)

    # create list in database
    user = session['user_id']
    plant_list = crud.create_plant_list(user, generated_list, prompt)

    return redirect(f'/finalproduct/{plant_list.plants_list_id}')

# @app.route('/gallery')
# def view_garden_gallery():
#     # view gallery specific to user
#     if 'user_id' in session:
#         user = session['user_id']
#         gardens = Garden.query.filter(Garden.user_id == user).all()
#         return render_gardens("gallery.html", gardens=gardens)
#     else:
#         return render_template("no_user.html")

@app.route('/finalproduct/<plants_id>')
def view_product(painting_id):
    
    #pull up garden info
    plants = Plants.query.filter(Plants.plants_id == plants_id).first()
    prompt = plants.prompt
    plants_list = plants.plants_list
    plants_id = plants.id

    return render_template('finalproduct.html', prompt = prompt, plants_list = plants_list, plants_id=plants_id)

@app.route('/shop')
def shop():

    return render_template("shop.html")

@app.route('/logout')
def logout():
    session.clear()
    flash("You are logged out.") 
    return redirect('/#begin')

if __name__ == "__main__":
    connect_to_db(app)
    app.run(port=3000)
