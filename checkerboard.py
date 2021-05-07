from flask import Flask, render_template
app = Flask(__name__)    
@app.route('/')          
def checkerboard():
    return render_template("index.html")
@app.route('/<int:fir>')
def checker(fir):
    return render_template("index2.html", fir = fir)
@app.route('/<int:fir>/<int:sec>')
def checky(fir,sec):
    return render_template("index3.html", fir = fir, sec = sec)

if __name__=="__main__":   
    app.run(debug=True)    
