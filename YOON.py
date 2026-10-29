
from flask import Flask, render_template,request

Baby = Flask(__name__)

@Baby.route("/")
def home():
    return render_template("index.html")

@Baby.route("/page")
def page():
    return render_template("page.html")

@Baby.route("/l")
def latter():
    return render_template("latter.html")

@Baby.route("/12" ,methods=["GET","POST"])
def mom():
    message=""
    if request.method=="POST":
        birthday=request.form.get("birthday","")
        message="Happy Birthday "+birthday
    return render_template("mom.html",message=message)

if __name__ == "__main__":
    Baby.run(debug=True)
