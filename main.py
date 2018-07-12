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

@app.route("/welcome", methods=['GET', 'POST'])
def validate():

    username = request.form['username']

    return render_template(
        'welcome.html',
        username=username,
        )

@app.route("/", methods=['GET', 'POST']) 
def index():

      

    #.join or append here for them to show up next to field
    
    if request.method == 'GET':
        error = request.args.get("error")
        new_password_error = ''
        new_username_error = ''
        new_email_error = ''

        return render_template(
            'edit.html',
            error=error
            )
    elif request.method == 'POST':
        error = request.args.get("error")
        check_username = request.form['username']
        check_password = request.form['password']
        check_verify_password = request.form["verify password"]
        check_email = request.form["email"]
       
        if check_password != check_verify_password:
            password_error = "Your passwords do not match"
            return redirect("/?error=" + error)
        if len(check_username) < 3 or len(check_username) > 20:
            error = "Your username has to be between 3 and 20 characters long and have no space"
            return redirect("/?error=" + error)
        if ' ' in check_username:
            error = "Your username has to be between 3 and 20 characters long and have no space"
            return redirect("/?error=" + error)
        if check_username or check_password or check_verify_password is ' ':
            error = "You must fill in all required fields"
            
        if not is_email(check_email):
            error = 'That is not a valid email address'
            return redirect("/?error=" + error)
  

    else:
            
        return redirect('/welcome')
        '''return render_template(
        'welcome.html',
        )'''
        
            
    #if no errors:
    #    return redirect('/welcome')

    
    


app.run()