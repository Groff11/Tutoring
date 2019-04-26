from flask import Flask, render_template
app = Flask(__name__)
import mypalindrome

@app.route("/api/palindrome/")
def palindrome():
  return mypalindrome.help()

@app.route('/')
def index():
	return render_template('./index.html')
