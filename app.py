from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
from flask_sqlalchemy import SQLAlchemy

import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/team")
def team():
    return render_template("team.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Default to 5000 if no PORT is set
    app.run(host="0.0.0.0", port=port)
