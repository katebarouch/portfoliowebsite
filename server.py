from flask import (Flask, render_template, request, flash, session,
                   redirect, jsonify, url_for)
from model import connect_to_db, db, User, Plants
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
def homepage_game():
    """Show Homepage"""
    return render_template("homepage_game.html")

@app.route('/contact')
def faq():
    """Show Contact Info"""
    return render_template("contact.html")

@app.route('/portfolio')
def portfolio():
    """Show Links"""
    return render_template("portfolio.html")

if __name__ == "__main__":
    connect_to_db(app)
    app.run(port=3000)
