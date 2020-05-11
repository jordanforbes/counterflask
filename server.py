from flask import Flask, render_template, redirect, session
app= Flask(__name__)
app.secret_key="dont tell "



@app.route('/')
def counter():
    if 'counter' in session:
        session['counter']= int(session['counter'])+1
    else:
        session['counter']=0
    return render_template('index.html')
    
@app.route('/double')
def jump():
    session['counter']= int(session['counter'])+1
    return redirect('/')

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)
