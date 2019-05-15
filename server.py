from flask import Flask, render_template, status
app = Flask(__name__)
import mypalindrome

@app.route("/api/palindrome/")
def palindrome():
  is_palindrome = mypalindrome.help()
  if is_palindrome:
		return status.HTTP_200_OK
	else:
		return status.HTTP_406_NOT_ACCEPTABLE

@app.route('/')
def index():
	return render_template('index.html')
