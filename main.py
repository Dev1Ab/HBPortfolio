from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = 'i know you youre like, when shit dont go your way you need me to fix it!'

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/blog-home")
def blog():
    return render_template("blog_home.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/milky_way")
def milky_way():
    return render_template("milky_way.html")


@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")


if __name__ == '__main__':
    app.run(debug=True)