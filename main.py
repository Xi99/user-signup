from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True


@app.route("/", methods=['POST'])
def validate():

    check_username = request.form['username']
    print(check_username)
    if len(check_username) < 3:
        return "Your username is either too short or too long"

@app.route("/")
def index():
    error= request.args.get("error")

    return render_template(
        'edit.html',
        error=error,
    )


app.run()