from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("register.html")
@app.route("/register", methods=["POST"])
def register():
    name = request.form["name"]
    roll = request.form["roll"]
    email = request.form["email"]
    phone = request.form["phone"]
    gender = request.form["gender"]
    course = request.form["course"]
    address = request.form["address"]
    return render_template(
        "success.html",
        name=name,
        roll=roll,
        email=email,
        phone=phone,
        gender=gender,
        course=course,
        address=address
    )
if __name__ == "__main__":
    app.run(debug=True)
