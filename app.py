from flask import Flask, render_template_string, request, redirect
import os

app = Flask(__name__)

votes = {"Red Cow": 0, "Narnija": 0}

template = """
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Birthday Vote 🎉</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background: linear-gradient(135deg, #f9c5d1, #fddde6);
      text-align: center;
      padding: 50px;
    }
    h1 {
      font-size: 2.5em;
    }
    form {
      margin: 20px 0;
    }
    button {
      background-color: #ff69b4;
      color: white;
      border: none;
      padding: 15px 30px;
      font-size: 1.2em;
      margin: 10px;
      cursor: pointer;
      border-radius: 10px;
    }
    button:hover {
      background-color: #ff1493;
    }
    .results {
      margin-top: 40px;
    }
  </style>
</head>
<body>
  <h1>Bane and Sean invite you to a crazy, fun birthday party! 🎂🎈</h1>
  <p>We need your help to choose where to celebrate:</p>
  <form method="POST">
    <button name="vote" value="Red Cow">Red Cow</button>
    <button name="vote" value="Narnija">Narnija</button>
  </form>
  <div class="results">
    <h2>Current Votes:</h2>
    <p>Red Cow: {{ votes["Red Cow"] }}</p>
    <p>Narnija: {{ votes["Narnija"] }}</p>
  </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        vote = request.form.get("vote")
        if vote in votes:
            votes[vote] += 1
        return redirect("/")
    return render_template_string(template, votes=votes)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
