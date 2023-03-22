from flask import Flask, render_template, request
import re


app = Flask(__name__,static_folder='static')




@app.route('/', methods=['POST','GET'])
def matc():
    if request.method=="POST":
        regex = request.form['regex']
        text=request.form['text']
        matches = re.findall(regex,text)
       
        return render_template('home.html', matches=matches , text=text,regex=regex)
    else:
        return render_template('home.html')
    
    
    
  







if __name__ == '__main__':
    app.run(debug=True)


