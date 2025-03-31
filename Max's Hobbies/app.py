from flask import Flask, request, render_template, redirect, send_file, session

app = Flask(__name__)
app.secret_key="supersecretkey"

flag1="CTF{Nostalgic_Euphoria}"
flag2="CTF{Michael_is_Happy_Now}"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home", methods=["POST"])
def home():
    username=request.form.get("username","").strip()
    hobby=request.form.get("hobby","").strip()
    welcome="Greeting from the grounds of Michael's life!"
    if not username or not hobby: 
        return "Error: Both fields are required!",400
    
    session["hobby"]=hobby

    return render_template("home.html", username=username, hobby=hobby, welcome=welcome)

@app.route("/<hobby>")
def Flag1(hobby):
    half_flag1="CTF{Nostalgic_"
    stored_hobby = session.get("hobby")
    if stored_hobby and stored_hobby.lower()==hobby.lower():
        return render_template("Flag1a.html", hobby=hobby, half_flag=half_flag1)
    else:
        return "Not this!", 403
    
@app.route("/score", methods=["POST"])
def Flag1_Checks():
    points="GREAT! I SEE YOU EARNED 50 POINTS! SUBMIT FLAG 2 TO WIN YOUR DESERVING POINTS!"
    total_points="Awesome! You have successfully completed this challenge & have scored all the 100 Points!"
    msg="HINT : Despite its obvious presence, we often overlook what is right before our eyes!\n"
    Flag1=request.form.get("flag","").strip()
    Flag2=request.form.get("flag","").strip()
    if Flag1==flag1:
        return render_template("Flag1b.html", points=points, msg=msg, flag2=flag2)
    elif Flag2==flag2:
        return render_template("final_score.html", total_points=total_points)
    else:
        return "ERROR: WRONG FLAG ENTERED!",400
        
@app.route("/exit", methods=["POST"])
def exit_challenge():
    return render_template("exit.html")

if __name__== "__main__":
    app.run(debug=True, port=8000)