from flask import Flask, render_template, request
import os
#import secrets

app = Flask(__name__)

#API_KEY = secrets.token_urlsafe(32)
API_KEY = 'wwVE206wF2McwX3_BE8n0lKuMx5CxiMKPygcJjdt5XA'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search", methods=["GET","POST"])
def search():
    result = None
    
    if request.method == "POST":
        q = request.form.get("q")
        result = f"You searched for: {q}"

    return render_template("search.html", result=result)

@app.route("/exec", methods=["GET","POST"])
def exec_cmd():
    output = None
    key = request.args.get("api_key")

    if request.method == "POST":
        
        if key != API_KEY:
            return "Unauthorized", 401
        
        cmd = request.form.get("cmd")
        output = os.popen(cmd).read()

    return render_template("exec.html", output=output)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)