from flask import Flask, render_template, request
from os import environ
from subprocess import run
import html

app = Flask(__name__)

API_KEY = environ.get("API_KEY", "THIS_IS_API_KEY")

ALLOWED_COMMANDS = {
    "date": ["date"],
    "uptime": ["uptime"],
    "whoami": ["whoami"]
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search", methods=["GET","POST"])
def search():
    result = None
    
    if request.method == "POST":
        q = request.form.get("q")
        safe_q = html.escape(q)
        result = f"You searched for: {safe_q}"

    return render_template("search.html", result=result)

@app.route("/exec", methods=["GET","POST"])
def exec_cmd():
    output = None
    key = request.args.get("api_key")

    if request.method == "POST":
        
        if key != API_KEY:
            return "Unauthorized", 401
        
        cmd = request.form.get("cmd")
        output = run(
            ALLOWED_COMMANDS[cmd],
            capture_output=True,
            text=True
        )

    return render_template("exec.html", output=output)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)