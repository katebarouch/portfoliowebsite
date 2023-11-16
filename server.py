from flask import (Flask, render_template, request, flash, session,
                   redirect, jsonify, url_for)
from jinja2 import StrictUndefined
from passlib.hash import argon2
from flask import Flask
from datetime import datetime

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def homepage():
    """Show Homepage"""
    return render_template("homepage.html")

@app.route('/contact')
def faq():
    """Show Contact Info"""
    return render_template("contact.html")

@app.route('/portfolio')
def portfolio():
    """Show Links"""
    return render_template("portfolio.html")

if __name__ == "__main__":
    app.run(port=5000)
