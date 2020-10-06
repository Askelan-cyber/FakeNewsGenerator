from flask import Flask, render_template
  
app = Flask(__name__) 
  
@app.route("/")
def home_view():
    #return '<h1>Newsgenerator</h1>'
    return render_template('test.html')
