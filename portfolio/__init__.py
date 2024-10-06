from flask import Flask,render_template

app = Flask(__name__)
projects = [
    {
        "name": "Habit tracking app with Python and MongoDB",
        "thumb": "img/habit-tracking.png",
        "hero": "img/habit-tracking-hero.png",
        "categories": ["Python", "web"],
        "slug": "habit-tracking",
        "prod": "test",
    },
    {
        "name": "Movie watchlist with Python and MongoDB",
        "thumb": "img/personal-finance.png",
        "hero": "img/personal-finance.png",
        "categories": ["Python", "web"],
        "slug": "",
    },
    {
        "name": "C# development project --soon--",
        "thumb": "img/rest-api-docs.png",
        "hero": "img/rest-api-docs.png",
        "categories": ["C#",".NET"],
        "slug": "",
    },
]
@app.route("/")
def home():
    return render_template ("home.html",projects=projects)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")
