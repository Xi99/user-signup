from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True


@app.route("/", methods=['POST'])
def validate():

    check_username = request.form['username']
    check_password = request.form['password']
    check_verify_password = request.form["verify password"]
    check_email = request.form["email"]

    
    if "@" not in check_email:
        error = "You must have a single @ in your emial"
        return redirect("/?error=" + error)

    if check_password is not check_verify_password:
        error = "Your passwords do not match"
        return redirect("/?error=" + error)
    
    if len(check_username) < 3 or len(check_username) > 20:
        error = "Your username is either too short or too long"
        return redirect("/?error=" + error)
    
    if check_username or check_password or check_verify_password is ' ':
        error = "You must fill in all required fields"
        return redirect("/?error=" + error)
    
@app.route("/") 
def index():
    error= request.args.get("error")

    return render_template(
        'edit.html',
        error=error,
    )


app.run()