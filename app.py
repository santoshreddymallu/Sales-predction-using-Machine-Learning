from flask import Flask,render_template,redirect,request,url_for
import pickle
import joblib

app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def predction():
    if request.method =="POST":
        
        year=int(request.form['year'])
        code=int(request.form['code'])
        month=int(request.form['month'])
        day=int(request.form['day'])
        week=int(request.form['week'])

        new_values = [[year,code,month,day,week]]
        model=joblib.load("lr_model.pkl")
        pred=model.predict(new_values)

        return render_template("predction.html",results=pred)

    return render_template("predction.html")



if __name__=="__main__":
    app.run(debug=True)
