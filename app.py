from flask import Flask
app = Flask(__name__)

@app.route('/user/<username>')
def show_user(username):
  #returns the username
  return 'Username: %s' % username

if __name__ == '__main__':
	app.run(host="0.0.0.0", debug=True)
