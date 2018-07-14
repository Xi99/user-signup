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

@app.route('/')
def index():
    return render_template('edit.html')


@app.route("/welcome/<username>", methods=['GET', 'POST'])
def welcome(username=None):
    print('gotta UUsername woot')
    print(username)

    return render_template(
        'welcome.html',
        username=username,
        )



@app.route("/submit", methods=['GET', 'POST']) 
def submit():
    print(request.form) 
    if request.method == 'GET':
        #error = request.args.get("error")
        return render_template(
            'edit.html',
            )

    elif request.method == 'POST':
        check_username = request.form['username']
        check_password = request.form['password']
        check_verify_password = request.form["verify password"]
        check_email = request.form["email"]
        
        password_error = ''
        email_error = ''
        username_error = ''
        none_error = ''


        if check_password is ' ':
            password_error = "Your passwords can't be blank"

        if check_password != check_verify_password:
            password_error = "Your passwords do not match"
            
        if len(check_username) < 3 or len(check_username) > 20:
            username_error = "Your username has to be between 3 and 20 characters long and have no space"
            
        if check_username and check_password and check_verify_password and check_email is ' ':
            none_error = "You must fill in all required fields"
            
        if not is_email(check_email):
            email_error = 'That is not a valid email address'
        
       
        if ' ' in check_username:
            username_error = "Your username has to be between 3 and 20 characters long and have no space"

        if not username_error and not password_error and not email_error:
            return redirect('/welcome/' + request.form['username'])
        else:
            return render_template('edit.html', username=check_username, email=check_email, username_error=username_error, email_error=email_error, password_error=password_error, none_error=none_error)

    
        
        
                    


app.run()