from flask import Flask, render_template, session, redirect  
app = Flask(__name__)                     
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes


@app.route('/')                           
def visits():
    if "count" in session:
        session["count"] = session["count"] +1
    else:
        session["count"] = 1
    return render_template('index.html')  



@app.route("/reset", methods=["POST"])
def reset():
    session.clear()
    return redirect("/")

@app.route("/add2", methods=["POST"])
def add():
    session["count"] = session["count"] +1
    return redirect("/")


if __name__=="__main__":
    app.run(debug=True)                   

