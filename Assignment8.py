from flask import Flask, render_template, request

app= Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Assignment 8"

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        return f"Registered Successfully! Name: {name}, Email: {email}"

    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True)