from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension
from .stories import story1


app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.route("/")
def ask_questions():
    """Generate and show from to ask words."""
    prompts = story.prompts
    return render_template("questions.html", prompts=prompts)

@app.route("/story")
def show_story():
    """show story results"""
    text = story.generate(request.args)
    return render_template("story.html", text=text)

