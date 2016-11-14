from flask import Flask
from flask import render_template

app = Flask("__name__")
#app.debug=True

@app.route("/")
def hello():
    return render_template("holiday.html")

@app.route("/<name>/")
#@app.route("/<name>/hello/goodbye")
def hello_someone(name):
    return render_template("holiday.html", name=name.title())
#	return "Hello {0}!".format(name.title())

#@app.route("/signup", methods=['POST'])
#def signup ():
#	form_data = request.form
#	print form_data['name']
#	print form_data['email']
#	return "ALL OK"
#render_template
app.run()
