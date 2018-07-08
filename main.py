from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

def is_email(string):

    atsign_index = string.find('@')
    atsign_present = atsign_index >= 0
    if not atsign_present:
        return False
    else:
        domain_dot_index = string.find('.', atsign_index)
        domain_dot_present = domain_dot_index >= 0
        return domain_dot_present

'''@app.route("/welcome", methods=['GET', 'POST'])
def welcome():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        verify = request.form['verify password']
        
    username = request.form['username']
        
    

    if len(check_username) < 3 or len(check_username) > 20:
        error = "Your username has to be between 3 and 20 characters long"
        return redirect("/" + error)

    if not is_email(email):
        error = email + '" is not a valid email address'
        return redirect('/' + error)
        
    if password != verify:
        error = 'Your passwords do not match'
        return redirect('/' + error)
        
    if check_username or check_password or check_verify_password is ' ':
        error = "You must fill in all required fields"
        return redirect("/" + error)

    else:
    return render_template(
        'welcome.html',
        username=username
        )
'''
@app.route("/welcome", methods=['GET', 'POST'])
def validate():

    check_username = request.form['username']
    check_password = request.form['password']
    check_verify_password = request.form["verify password"]
    check_email = request.form["email"]

    if "@" not in check_email:
        email_error = "You must have a single '@' and '.' in your emial"
        '''return redirect("/?error=" + email_error)'''

    if check_password != check_verify_password:
        password_again_error = "Your passwords do not match"
        '''return redirect("/?error=" + password_again_error)'''
    
    if len(check_username) < 3 or len(check_username) > 20:
        username_error = "Your username has to be between 3 and 20 characters long"
        '''return redirect("/?error=" + username_error)'''
    
    if ' ' in check_username:
        error = "You can't have a space in your username"
        '''return redirect("/?error=" + error)'''
    
    if check_username or check_password or check_verify_password is ' ':
        error = "You must fill in all required fields"
        '''return redirect("/?error=" + error)'''

    if not is_email(check_email):
        email_error = 'is not a valid email address'
        '''return redirect('/?error=' + email_error)'''

    else:

        return render_template(
            'welcome.html',
            username=username
            )

@app.route("/") 
def index():
    error= request.args.get("error")

    return render_template(
        'edit.html',
        error=error,
    )


app.run()