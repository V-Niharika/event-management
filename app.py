from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# simple in-memory event list
events = []

@app.route("/")
def index():
    return render_template("index.html", events=events)

@app.route("/add", methods=["GET", "POST"])
def add_event():
    if request.method == "POST":
        title = request.form["title"]
        date = request.form["date"]
        desc = request.form["description"]
        events.append({"title": title, "date": date, "desc": desc})
        return redirect(url_for("index"))
    return render_template("add_event.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
