from flask import Flask, render_template, request, flash, redirect
from inputform import InputForm
import secrets

app = Flask(__name__)
app.config["SECRET_KEY"] = "Mg#i8t!@Rd6"

shortened_urls = []


@app.route("/", methods=["GET", "POST"])
def home():
    form = InputForm()

    if request.method == "POST":
        if form.validate_on_submit():

            destination_url = form.url.data  # ✅ FIXED
            id = secrets.token_urlsafe(5)

            shortened_urls.append({"destination_url": destination_url, "id": id})

            form.url.data = ""  # ✅ FIXED

            flash(f"Short URL: {request.base_url}{id}", category="success")

        else:
            flash("Invalid URL!", category="error")  # ✅ FIXED

    return render_template("index.html", form=form)


@app.route("/<id>")
def redirect_user(id):
    for shortened_url in shortened_urls:
        if id == shortened_url["id"]:
            return redirect(shortened_url["destination_url"])

    return "URL not found ❌"


if __name__ == "__main__":
    app.run(debug=True)
