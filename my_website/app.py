from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "your_secret_key_here"  # needed for flash messages

@app.route("/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        # Basic validation
        if not username or not email or not password or not confirm_password:
            flash("Please fill out all fields.", "error")
        elif password != confirm_password:
            flash("Passwords do not match.", "error")
        else:
            flash(f"Registration successful! Welcome, {username}.", "success")
            return redirect(url_for("register"))

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
