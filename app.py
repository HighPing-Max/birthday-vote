from flask import Flask, render_template_string, request, redirect, url_for, session
import os

app = Flask(__name__)
app.secret_key = "tajni_kljuc"  # Needed for session

votes = {"Red Cow 🐄": 0, "Narnija 🦁": 0}

vote_template = """
<!doctype html>
<html lang="sr">
<head>
  <meta charset="utf-8">
  <title>Rođendansko Glasanje 🎉</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background: linear-gradient(135deg, #ffffff, #cce6ff); /* White and blue */
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
      background-color: #007BFF;
      color: white;
      border: none;
      padding: 15px 30px;
      font-size: 1.2em;
      margin: 10px;
      cursor: pointer;
      border-radius: 10px;
    }
    button:hover {
      background-color: #0056b3;
    }
    .results {
      margin-top: 40px;
    }
  </style>
</head>
<body>
  <h1>Bane i Sean vas pozivaju na ludu i zabavnu rođendansku žurku! 🎂🎈</h1>
  <p>Pomozi nam da izaberemo gde ćemo da slavimo:</p>
  <form method="POST">
    <button name="vote" value="Red Cow 🐄">Red Cow 🐄</button>
    <button name="vote" value="Narnija 🦁">Narnija 🦁</button>
  </form>
  <div class="results">
    <h2>Trenutni Rezultati:</h2>
    <p>Red Cow 🐄: {{ votes["Red Cow 🐄"] }}</p>
    <p>Narnija 🦁: {{ votes["Narnija 🦁"] }}</p>
  </div>
</body>
</html>
"""

thank_you_template = """
<!doctype html>
<html lang="sr">
<head>
  <meta charset="utf-8">
  <title>Hvala na glasanju 🎉</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background: linear-gradient(135deg, #ffffff, #cce6ff);
      text-align: center;
      padding: 50px;
    }
    h1 {
      font-size: 2.5em;
    }
    p {
      font-size: 1.2em;
    }
    a {
      display: inline-block;
      margin-top: 20px;
      font-size: 1em;
      text-decoration: none;
      background-color: #007BFF;
      color: white;
      padding: 10px 20px;
      border-radius: 8px;
    }
    a:hover {
      background-color: #0056b3;
    }
  </style>
</head>
<body>
  <h1>Hvala što si glasao! ✅</h1>
  <p>Vidimo se na žurci 14.06.2025 🎉</p>
  <a href="/">Nazad na početnu</a>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        vote = request.form.get("vote")
        if vote in votes:
            votes[vote] += 1
            session["voted"] = True
        return redirect(url_for("thank_you"))
    return render_template_string(vote_template, votes=votes)

@app.route("/thank-you")
def thank_you():
    if not session.get("voted"):
        return redirect(url_for("index"))
    return render_template_string(thank_you_template)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
